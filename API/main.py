import time 
from functools import wraps
from flask import Flask, request, send_from_directory, abort, Response, jsonify
import mysql.connector
import env
import json

from DB_calls import check_admin, add_user, check_quiz_type,  add_quiz, show_all, show_all_preview, show_quiz_with_type, show_quiz_no_type, delete_quiz



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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

# ПРОВЕРКА API
@app.route("/api", methods=['GET'])
def api():
    return "Hello from API"

# ТЕЛЕГРАМ КЛИЕНТ

# ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ - ТЕЛЕГРАМ КЛИЕНТ
@app.route("/api/adduser",methods=['POST'])
def api_adduser():
    add_user(user_id,lastname,firstname,username)
    
    return

# ПОКАЗ ИВЕНТА - ТЕЛЕГРАМ КЛИЕНТ
@app.route("/api/quiz/<quiz_id>")
def api_quiz(quiz_id):
    
    quiz_data = show_quiz_no_type(quiz_id)
    Response(
        response=quiz_data,
        status=200,
        mimetype='application/json')

    return quiz_data

# АДМИН КЛИЕНТ

# ДОБАВЛЕНИЕ ИВЕНТА ЛЮБОГО УСТАНОВЛЕННОГО ТИПА - АДМИН КЛИЕНТ
@app.route("/api/admin/createquiz", methods=['POST'])
# @admin_role
def api_admin_createquiz():
    post_data = request.data
    data_json = json.loads(post_data.decode('utf-8'))
    quiz_type = data_json['quiz_type']
    
    try:
        add_quiz(quiz_type, data_json)
    except Exception as error: print(error)
    return ''


@app.route("/api/admin/quiz_with_type", methods=['GET'])
def api_admin_quiz_with_type():
    quiz_type = request.args.get('quiz_type')
    quiz_id = request.args.get('quiz_id')
    quiz_data = show_quiz_with_type(quiz_id, quiz_type)

    
    return Response(response=quiz_data,
                    status=200,
                    mimetype='application/json')

# !!! УДАЛЕНИЕ КВИЗА - АДМИН КЛИЕНТ
@app.route("/api/admin/deletequiz", methods=['POST'])
def api_admin_deletequiz():

    post_data = request.data
    data_json = json.loads(post_data.decode('utf-8'))
    quiz_id = data_json['quiz_id']
    print(quiz_id, "11111")

    try:
        delete_quiz(quiz_id)
        return Response(status=200)
    except Exception as e:
        return Response(response=str(e),status=500)

# !!! ПОКАЗ ВСЕХ ИВЕНТОВ - АДМИН КИЕНТ
@app.route("/api/admin/showall", methods=['GET'])
def api_admin_showall():
    
    json_data = json.dumps(show_all(),  ensure_ascii=False)   
       
    return jsonify(quizes=json_data)

# ПРЕДПОКАЗ ВСЕХ ИВЕНТОВ С ИСПОЛЬЗОВАНИЕМ ПАГИНАЦИИ - АДМИН КЛИЕНТ  
@app.route("/api/admin/showpreview", methods=['GET'])
def api_admin_showpreview():
    quiz_type = request.args.get('quiz_type')
    page_number = request.args.get('page')
    
    quizes_data = show_all_preview(quiz_type=quiz_type,pagenumber=page_number)
    
    json_data = json.dumps(quizes_data['quizes'], ensure_ascii=False)
    
    
    
    return jsonify(quizes=json_data, count=quizes_data['count'], type=quiz_type)

if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')

