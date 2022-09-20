import time
from functools import wraps
from flask import Flask, request, send_from_directory, abort, Response, jsonify
import mysql.connector
import json
from API.DB_calls import check_admin, add_user, check_quiz_type, add_quiz, show_all, show_all_preview, \
    show_quiz_with_type, show_quiz_no_type, get_user

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def admin_role(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            session_token = request.cookies['session_token']
            if check_admin(session_token):
                return f(*args, **kwargs)
            else:
                return abort(403)
        except Exception as e:
            print(e)
            return abort(403)

    return wrap


@app.route("/api", methods=['GET'])
def api():
    return "Hello from API"


@app.route("/api/adduser", methods=['POST'])
def api_adduser(user_id, lastname, firstname, username):
    add_user(user_id, lastname, firstname, username)

    return

def api_getuser(user_id):
    return get_user(user_id)

@app.route("/api/quiz/<quiz_id>")
def api_quiz(quiz_id):
    quiz_data = show_quiz_no_type(quiz_id)
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

    try:
        add_quiz(quiz_type, data_json)
    except Exception as error:
        print(error, "!!!!")
    return ''


@app.route("/api/admin/quiz_with_type", methods=['GET'])
def api_admin_quiz_with_type():
    quiz_type = request.args.get('quiz_type')
    quiz_id = request.args.get('quiz_id')
    quiz_data = show_quiz_with_type(quiz_id, quiz_type)

    return Response(response=quiz_data,
                    status=200,
                    mimetype='application/json')


@app.route("/api/admin/deletequiz", methods=['POST'])
@admin_role
def api_admin_deletequiz(quiz_id):
    return


@app.route("/api/admin/showall", methods=['GET'])
def api_admin_showall():
    json_data = json.dumps(show_all(), ensure_ascii=False)

    return jsonify(quizes=json_data)


@app.route("/api/admin/showpreview", methods=['GET'])
def api_admin_showpreview():
    quiz_type = request.args.get('quiz_type')
    page_number = request.args.get('page')
    print(quiz_type, page_number)

    quizes_data = show_all_preview(quiz_type=quiz_type, pagenumber=page_number)

    json_data = json.dumps(quizes_data['quizes'], ensure_ascii=False)

    return jsonify(quizes=json_data, count=quizes_data['count'], type=quiz_type)


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')
