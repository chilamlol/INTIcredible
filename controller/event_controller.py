from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from datetime import datetime
import json
from token_verifier import *

# recommender system
import pandas as pd
from pandas import json_normalize
import math
from sklearn.model_selection import train_test_split
from database.db_config import mysql
from model_evaluator import ModelEvaluator, PopularityRecommender

# dummy data
import random


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


# log transformation to smooth the distribution
def smooth_user_preference(x):
    return math.log(1 + x, 2)


def get_items_interacted(user_id, interactions_df):
    # Get the user's data and merge in the movie information.
    interacted_items = interactions_df.loc[user_id]['eventId']
    return set(interacted_items if type(interacted_items) == pd.Series else [interacted_items])


def get_timestamp():

    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    ts = datetime.timestamp(dt)

    return ts


# add events
@app.route('/event/add', methods=['POST'])
@is_admin
def add_event():
    try:
        _json = request.json

        _name = _json['name']
        _description = _json['description']
        _image = _json['image']
        _registerLink = _json['registerLink']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _status = _json['status']

        # save edits
        sql = "INSERT INTO tbl_event(name, description, image, registerLink, startDate, endDate, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"

        data = (_name, _description, _image, _registerLink, _startDate, _endDate, _status)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Event added successfully!')
            resp.status_code = 201
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all events
@app.route('/event')
@token_required
def show_all_event():
    try:
        sql = "SELECT * FROM tbl_event"
        rows = readAllRecord(sql)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# List all upcoming events
@app.route('/event/upcoming/<int:day>')
@token_required
def show_all_upcoming_event(day):
    try:
        if day < 0:
            return bad_request()

        sql = "SELECT * FROM tbl_event WHERE status = 1 AND DATEDIFF(NOW(), startDate)"

        # If day = 0, then print all upcoming events
        if day == 0:
            sql += " <= %s"
        # Else print upcoming events within day given
        else:
            day = -abs(day)
            sql += " BETWEEN %s AND 0 "

        print(sql)
        rows = readAllRecord(sql, day)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific event
@app.route('/event/<int:eventId>')
@token_required
def show_event(eventId):
    try:
        sql = "SELECT * FROM tbl_event WHERE eventId=%s"

        row = readOneRecord(sql, eventId)

        if not row:
            return not_found()

        # Convert date time format for output
        row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
        row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update event
@app.route('/event/update/<int:eventId>', methods=['PUT'])
@is_admin
def update_event(eventId):
    try:
        _json = request.json

        _name = _json['name']
        _description = _json['description']
        _image = _json['image']
        _registerLink = _json['registerLink']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _status = _json['status']

        # save edits
        sql = " UPDATE tbl_event SET name=%s, description=%s, image=%s, " \
              " registerLink=%s, startDate=%s, endDate=%s, status=%s WHERE eventId=%s "

        data = (_name, _description, _image, _registerLink, _startDate, _endDate, _status, eventId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Event updated successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete Event
@app.route('/event/delete/<int:eventId>', methods=['DELETE'])
@is_admin
def delete_event(eventId):
    try:
        sql = "DELETE FROM tbl_event WHERE eventId=%s"

        if deleteRecord(sql, eventId) > 0:
            resp = jsonify(message='Event deleted successfully')
            resp.status_code = 200
            return resp

        return not_found
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Add event activity
@app.route('/event/add/event-activity', methods=['POST'])
# @token_required
def add_event_activity():
    try:
        _json = request.json

        _userId = _json['userId']
        _eventId = _json['eventId']
        _eventType = _json['eventType']

        sql = " INSERT INTO tbl_event_activity(timestamp, userId, eventId, eventType) " \
              " VALUES(%s, %s, %s, %s) "
        data = (int(get_timestamp()), _userId, _eventId, _eventType)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Event activity added successfully')
            resp.status_code = 201
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Event recommender
# insert dummy data to tbl event
@app.route('/event/generate-dummy/event/<int:amount>')
def generate_dummy_event_in_table(amount):
    sql = " INSERT INTO tbl_event(name, description, image, registerLink, startDate, endDate, status )" \
          " VALUES(%s, %s, %s, %s, NOW(), NOW(), 0)"

    data = ("dummyEvent", "dummy", "dummy", "dummy")
    # Insert to table
    for i in range(amount):
        createRecord(sql, data)

    resp = jsonify(message='Dummy data created')
    return resp


# Event recommender
# insert dummy data to tbl user
@app.route('/event/generate-dummy/user/<int:amount>')
def generate_dummy_event_for_tbl_user(amount):
    sql = " INSERT INTO tbl_user(username, password, activationStatus, userRoleId)" \
          " VALUES(%s, %s, 30, 1)"

    data = ("dummyName", "dummyPassword")
    # Insert to table
    for i in range(amount):
        createRecord(sql, data)

    resp = jsonify(message='Dummy data created')
    return resp


# Event recommender
# insert dummy data
@app.route('/event/generate-dummy/event-activity/<int:amount>')
def generate_dummy_event_for_event_activity(amount):
    sql = " SELECT DISTINCT userId FROM tbl_user "
    userIdJson = readAllRecord(sql)

    # Declare empty userId list
    userIdList = []

    for userId in userIdJson:
        userIdList.append(userId['userId'])

    sql = " SELECT DISTINCT eventId FROM tbl_event"
    eventIdJson = readAllRecord(sql)

    # Declare empty eventId list
    eventIdList = []

    for eventId in eventIdJson:
        eventIdList.append(eventId['eventId'])

    sql = " INSERT INTO tbl_event_activity (timestamp, userId, eventId, eventType) VALUES (%s, %s, %s, %s)"

    # Insert to table
    for i in range(amount):
        data = (int(get_timestamp()), random.choice(userIdList), random.choice(eventIdList), random.choice(['VIEW', 'JOIN']))

        createRecord(sql, data)

    resp = jsonify(message='Dummy data created')
    return resp


# list popular events sorted
@app.route('/event/popular')
#@token_required
def show_all_popular_event():
    try:
        sql = " SELECT DISTINCT te.*, tes.eventStrength FROM tbl_event te JOIN tbl_event_strength tes " \
              " ON te.eventId = tes.eventId WHERE te.status = 1 AND DATEDIFF(NOW(), te.startDate) <= 0 " \
              " ORDER BY tes.eventStrength DESC, tes.createdDate DESC LIMIT 10"
        rows = readAllRecord(sql)

        print(rows)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Event recommender
@app.route('/event/collaborative-filtering-recommender')
def recommender_with_collaborative_filtering():
    try:
        # Run SQL
        sql = "SELECT timestamp, eventType, eventId, userId FROM tbl_event_activity"
        rows = readAllRecord(sql)

        if not rows:
            return not_found()

        # Loads json into dataframe, interactions_df
        interactions_df = json_normalize(rows)

        sql = "SELECT * FROM tbl_event"
        rows = readAllRecord(sql)

        if not rows:
            return not_found()

        # Loads json into dataframe, event_df
        event_df = json_normalize(rows)

        # define event strength matrix
        event_type_strength = {
            'VIEW': 1.0,
            'JOIN': 3.0,
        }

        interactions_df['eventStrength'] = interactions_df['eventType'].apply(lambda x: event_type_strength[x])

        # Recommender systems have a problem known as user cold-start,
        # in which is hard do provide personalized recommendations for users with none or a very few number of consumed items,
        # due to the lack of information to model their preferences.

        # For this reason, we are keeping in the dataset only users with at leas 5 interactions.

        # Get total users
        users_interactions_count_df = interactions_df.groupby(['userId', 'eventId']).size().groupby('userId').size()

        # Get user with at least 5 interactions
        users_with_enough_interactions_df = users_interactions_count_df[users_interactions_count_df >= 5].reset_index()[
            ['userId']]

        # Get total interactions of users with at least 5 interactions
        interactions_from_selected_users_df = interactions_df.merge(users_with_enough_interactions_df,
                                                                    how='right',
                                                                    left_on='userId',
                                                                    right_on='userId')

        # Get unique user/item interactions
        interactions_full_df = interactions_from_selected_users_df \
            .groupby(['userId', 'eventId'])['eventStrength'].sum() \
            .apply(smooth_user_preference).reset_index()

        # Evaluation
        # Train the model, the ratio is 80:20 (train:test)
        interactions_train_df, interactions_test_df = train_test_split(interactions_full_df,
                                                                       stratify=interactions_full_df['userId'],
                                                                       test_size=0.20,
                                                                       random_state=42)

        # Indexing by userId to speed up the searches during evaluation
        interactions_full_indexed_df = interactions_full_df.set_index('userId')
        interactions_train_indexed_df = interactions_train_df.set_index('userId')
        interactions_test_indexed_df = interactions_test_df.set_index('userId')

        # print('# interactions on Train set: %d' % len(interactions_train_df))
        # print('# interactions on Test set: %d' % len(interactions_test_df))

        # Popularity model
        # Computes the most popular items
        item_popularity_df = interactions_full_df.groupby('eventId')['eventStrength'].sum().sort_values(
            ascending=False).reset_index()

        # Update to table
        conn = mysql.connect()
        cursor = conn.cursor()

        # creating column list for insertion
        cols = "`,`".join([str(i) for i in item_popularity_df.columns.tolist()])

        for i, row in item_popularity_df.iterrows():
            sql = "INSERT INTO `tbl_event_strength` (`" + cols + "`, createdDate) VALUES (" + "%s," * (
                        len(row) - 1) + "%s, NOW())"
            cursor.execute(sql, tuple(row))

            # the connection is not autocommit by default, so we must commit to save our changes
            conn.commit()

        # close connection
        conn.close()

        # Popularity Model
        popularity_model = PopularityRecommender(item_popularity_df)

        # Model Evaluator
        model_evaluator = ModelEvaluator(interactions_test_indexed_df,
                                         interactions_train_indexed_df,
                                         interactions_full_indexed_df,
                                         event_df)

        # Evaluating Popularity recommendation model
        pop_global_metrics, pop_detailed_results_df = model_evaluator.evaluate_model(popularity_model)

        pop_detailed_results_df.to_csv('static/collaborative_filtering_result.csv')

        # response code 200
        resp = jsonify(message='Evaluation completed', globalMetric=pop_global_metrics)

        return resp

    except Exception as e:
        print(e)
        return internal_server_error(e)
