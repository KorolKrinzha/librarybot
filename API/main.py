import time 
from functools import wraps
from flask import Flask, request, send_from_directory, abort, Response
import mysql.connector
import env
import json

from DB_calls import check_admin, add_user, check_quiz_type, show_quiz, add_quiz



app = Flask(__name__)


def admin_role(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            session_token = request.cookies['session_token']
            if check_admin(session_token): return f(*args, **kwargs)
            else: return abort(403)
        except Exception as e: 
            print(e)
            return abort(403)
    return wrap


@app.route("/api", methods=['GET'])
def api():
    return "Hello from API"


@app.route("/api/adduser",methods=['POST'])
def api_adduser():
    add_user(user_id,lastname,firstname,username)
    
    return


@app.route("/api/quiz/<quiz_id>")
def api_quiz(quiz_id):
    
    quiz_data = show_quiz(quiz_id)
    Response(
        response=quiz_data,
        status=200,
        mimetype='application/json')

    return quiz_data

# АДМИНКА
@app.route("/api/admin/createquiz", methods=['POST'])
# @admin_role
def api_admin_createquiz():
    post_data = request.data
    data_json = json.loads(post_data.decode('utf-8'))
    quiz_type = data_json['quiz_type']
    print(quiz_type)
    
    try:
        add_quiz(quiz_type, data_json)
    except Exception as error: print(error, "!!!!")
    return ''

@app.route("/api/admin/deletequiz", methods=['POST'])
@admin_role
def api_admin_deletequiz(quiz_id):
    return


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')

