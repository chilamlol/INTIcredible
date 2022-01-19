def emailOTP(otp):
    html = '<div style="font-family: Helvetica,Arial,sans-serif;width:60%;overflow:auto;line-height:2">' \
           '<div style="margin:50px auto;width:70%;padding:20px 0">' \
           '<div style="border-bottom:1px solid #eee">' \
           '<a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">INTIcredibles</a>' \
           '</div>' \
           '<p style="font-size:1.1em">Hi,</p>' \
           '<p>Thank you for choosing INTIcredibles. Use the following OTP to complete your Sign Up procedures. OTP is valid for 5 minutes</p>' \
           '<h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">' + str(otp) + '</h2>' \
                                                                                                                                        '<p style="font-size:0.9em;">Regards,<br />INTIcredibles</p>' \
                                                                                                                                        '<hr style="border:none;border-top:1px solid #eee" />' \
                                                                                                                                        '<div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">' \
                                                                                                                                        '<p>INTIcredibles</p>' \
                                                                                                                                        '<p>IICS</p>' \
                                                                                                                                        '<p>Malaysia</p>' \
                                                                                                                                        '</div>' \
                                                                                                                                        '</div>' \
                                                                                                                                        '</div>'

    return html
