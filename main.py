import time
from functools import wraps
from flask import Flask, request, send_from_directory, abort, Response, jsonify
import mysql.connector
import env
import json
from DB_calls import add_user, show_quiz, check_answer, show_userscore
from DB_calls import add_quiz, delete_quiz
from DB_calls import show_all_users

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# def admin_role(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         try:
#             session_token = request.cookies['session_token']
#             if check_admin(session_token): return f(*args, **kwargs)
#             else: return abort(403)
#         except Exception as e:
#             print(e)
#             return abort(403)
#     return wrap

# Проверка API
@app.route("/api", methods=['GET'])
def api():
    return "Hello from API"

# ОБЫЧНЫЙ ПОЛЬЗОВАТЕЛЬ

# Добавление пользователя
@app.route("/api/adduser", methods=['POST'])
def api_adduser():

    user_id = request.args.get(key='user_id')
    lastname = request.args.get(key='lastname')
    firstname = request.args.get(key='firstname')
    username = request.args.get(key='username')

    try:
        add_user(user_id, lastname, firstname, username)
        return Response(
            response='Пользователь успешно зарегистрирован',
            status=200)

    except Exception as e:
        print(e)
        return Response(
            response='Ошибка при регистрировании пользователя',
            status=500)


# Показ квиза
@app.route("/api/quiz", methods=['GET'])
def api_quiz():
    quiz_id = request.args.get(key='quiz_id')
    try:
        return Response(
        response=show_quiz(quiz_id),
        status=200,
        mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(response='Ошибка при получении квиза', status=500)
        
    

# Проверка ответа на квиз пользователя
@app.route("/api/answer", methods=['POST'])
def api_answer():
    quiz_id = request.args.get(key='quiz_id')
    user_id = request.args.get(key='user_id')
    answer = request.args.get(key='answer')

    try:
        correct, reply = check_answer(quiz_id, quiz_type, user_id, answer)
        if correct:
            return Response(response=reply, status=200)
        else:
            return Response(response=reply, status=200)
    except BaseException:
        return Response(response='Ошибка при получении ответа', status=500)


# Просмотр счета
@app.route("/api/userscore", methods=['GET'])
def api_userscore():
    user_id = request.args.get(key='user_id')
    try:
        userscore = show_userscore(user_id)
        return Response(
            response=userscore,
            status=200,
            mimetype='application/json')
    except BaseException:
        return Response(response='Ошибка при получении данных', status=500)


# Вывод всех пользователей
@app.route("/api/admin/showusers", methods=['GET'])
def api_showusers():
    try:
        all_users = show_all_users()
        all_users = json.dumps(all_users)
        return Response(response=all_users,
                 status=200,
                 mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(response='Ошибка при получении пользователей', status=500)
    
    
    


# Добавление квиза
@app.route("/api/admin/createquiz", methods=['POST'])
def api_admin_createquiz():
    quiz_type = request.args.get(key='quiz_type')
    question = request.args.get(key='question') 
    right_answer_reply = request.args.get(key='right_answer_reply') 
    wrong_answer_reply = request.args.get(key='wrong_answer_reply') 
    prize = request.args.get(key='prize')  
    specifics = request.args.get(key='specifics')

    data_json = {
        'quiz_type': quiz_type,
        'question': question,
        'right_answer_reply': right_answer_reply,
        'wrong_answer_reply': wrong_answer_reply,
        'prize': prize,
        'specifics': specifics}

    if len(question)==0 or len(right_answer_reply)==0 or len(wrong_answer_reply)==0:
        return Response(response='Ошибка. Не указаны необходимые данные', status=500)

    try:
        add_quiz(quiz_type, data_json)
        return Response(response='Квиз успешно добавлен', status=200)
    except Exception as e:
        print(e)
        return Response(response='Ошибка при добавлении квиза', status=500)


# @app.route("/api/admin/quiz_with_type", methods=['GET'])
# def api_admin_quiz_with_type():
#     quiz_type = request.args.get('quiz_type')
#     quiz_id = request.args.get('quiz_id')
#     quiz_data = show_quiz_with_type(quiz_id, quiz_type)


#     return Response(response=quiz_data,
#                     status=200,
#                     mimetype='application/json')

# Удаление квиза
@app.route("/api/admin/deletequiz", methods=['POST'])
def api_admin_deletequiz():
    quiz_id = request.args.get(key='quiz_id')
    try:
        delete_quiz(quiz_id)
        return Response(response='Квиз успешно удален', status=200)
    except Exception as e:
        print(e)
        return Response(response='Ошибка при удалении квиза', status=500)

# # !!! ПОКАЗ ВСЕХ квизОВ - АДМИН КИЕНТ
# @app.route("/api/admin/showall", methods=['GET'])
# def api_admin_showall():

#     json_data = json.dumps(show_all(),  ensure_ascii=False)

#     return jsonify(quizes=json_data)


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0', port=6000)
