import pandas as pd
import random

# Top-N accuracy metrics consts
EVAL_RANDOM_SAMPLE_NON_INTERACTED_ITEMS = 50


def get_items_interacted(user_id, interactions_df):
    # Get the user's data and merge in the movie information.
    interacted_items = interactions_df.loc[user_id]['eventId']
    return set(interacted_items if type(interacted_items) == pd.Series else [interacted_items])


def verify_hit_top_n(item_id, recommended_items, topn):
    try:
        index = next(i for i, c in enumerate(recommended_items) if c == item_id)
    except Exception:
        index = -1
    hit = int(index in range(0, topn))
    return hit, index


class ModelEvaluator:

    def __init__(self, interactions_test_indexed_df, interactions_train_indexed_df,
                 interactions_full_indexed_df, event_df):
        self.interactions_test_indexed_df = interactions_test_indexed_df
        self.interactions_train_indexed_df = interactions_train_indexed_df
        self.interactions_full_indexed_df = interactions_full_indexed_df
        self.event_df = event_df

    def get_not_interacted_items_sample(self, user_id, sample_size, seed=42):
        interacted_items = get_items_interacted(user_id, self.interactions_full_indexed_df)
        all_items = set(self.event_df['eventId'])
        non_interacted_items = all_items - interacted_items

        random.seed(seed)
        non_interacted_items_sample = random.sample(non_interacted_items, sample_size)
        return set(non_interacted_items_sample)

    def evaluate_model_for_user(self, model, user_id):
        # Getting the items in test set
        interacted_values_testset = self.interactions_test_indexed_df.loc[user_id]
        if type(interacted_values_testset['eventId']) == pd.Series:
            user_interacted_items_testset = set(interacted_values_testset['eventId'])
        else:
            user_interacted_items_testset = set([int(interacted_values_testset['eventId'])])
        interacted_items_count_testset = len(user_interacted_items_testset)

        # Getting a ranked recommendation list from a model for a given user
        user_recs_df = model.recommend_items(user_id,
                                             items_to_ignore=get_items_interacted(user_id,
                                                                                  self.interactions_train_indexed_df),
                                             topn=10000000000)

        hits_at_5_count = 0
        hits_at_10_count = 0
        # For each item the user has interacted in test set
        for item_id in user_interacted_items_testset:
            # Getting a random sample (100) items the user has not interacted
            # (to represent items that are assumed to be no relevant to the user)
            non_interacted_items_sample = self.get_not_interacted_items_sample(user_id,
                                                                               sample_size=EVAL_RANDOM_SAMPLE_NON_INTERACTED_ITEMS,
                                                                               seed=item_id % (2 ** 32))
            # Combining the current interacted item with the 100 random items
            items_to_filter_recs = non_interacted_items_sample.union(set([item_id]))

            # Filtering only recommendations that are either the interacted item or from a random sample of 100 non-interacted items
            valid_recs_df = user_recs_df[user_recs_df['eventId'].isin(items_to_filter_recs)]
            valid_recs = valid_recs_df['eventId'].values
            # Verifying if the current interacted item is among the Top-N recommended items
            hit_at_5, index_at_5 = verify_hit_top_n(item_id, valid_recs, 5)
            hits_at_5_count += hit_at_5
            hit_at_10, index_at_10 = verify_hit_top_n(item_id, valid_recs, 10)
            hits_at_10_count += hit_at_10

        # Recall is the rate of the interacted items that are ranked among the Top-N recommended items,
        # when mixed with a set of non-relevant items
        recall_at_5 = hits_at_5_count / float(interacted_items_count_testset)
        recall_at_10 = hits_at_10_count / float(interacted_items_count_testset)

        user_metrics = {'hits@5_count': hits_at_5_count,
                        'hits@10_count': hits_at_10_count,
                        'interacted_count': interacted_items_count_testset,
                        'recall@5': recall_at_5,
                        'recall@10': recall_at_10}
        return user_metrics

    def evaluate_model(self, model):
        user_metrics_list = []
        for userProcessed, userId in enumerate(list(self.interactions_test_indexed_df.index.unique().values)):
            user_metrics_dict = self.evaluate_model_for_user(model, userId)
            user_metrics_dict['_user_id'] = userId
            user_metrics_list.append(user_metrics_dict)

        detailed_results_df = pd.DataFrame(user_metrics_list) \
            .sort_values('interacted_count', ascending=False)

        global_recall_at_5 = detailed_results_df['hits@5_count'].sum() / float(
            detailed_results_df['interacted_count'].sum())
        global_recall_at_10 = detailed_results_df['hits@10_count'].sum() / float(
            detailed_results_df['interacted_count'].sum())

        # The Top-N accuracy metric choosen was Recall@N which evaluates whether
        # the interacted item is among the top N items (hit)
        # in the ranked list of 101 recommendations for a user.
        global_metrics = {'modelName': model.get_model_name(),
                          'recall@5': global_recall_at_5,
                          'recall@10': global_recall_at_10}
        return global_metrics, detailed_results_df, userProcessed


class PopularityRecommender:
    MODEL_NAME = 'Popularity'

    def __init__(self, popularity_df):
        self.popularity_df = popularity_df

    def get_model_name(self):
        return self.MODEL_NAME

    def recommend_items(self, user_id, items_to_ignore=[], topn=10, verbose=False):
        # Recommend the more popular items that the user hasn't seen yet.
        recommendations_df = self.popularity_df[~self.popularity_df['eventId'].isin(items_to_ignore)] \
            .sort_values('eventStrength', ascending=False) \
            .head(topn)

        return recommendations_df
