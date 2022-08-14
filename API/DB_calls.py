import json
from DB_tools import DB_JSON, DB_COMMIT, DB_FETCH_ONE, DB_CHECK_EXISTENCE



def check_admin(session_token):
    return True

def add_user(user_id, lastname, firstname, username):
    return


# СОЗДАНИЕ ИВЕНТА
def add_event(event_type, quiz_data):
    create_quiz_type = {
        'one': 1,
        'multiple': 1,
        'qr':1,
        'text': 1
        
    }
    
    return

def add_event_one(quiz_data):
    return

def add_event_multiple(quiz_data):
    return

def add_event_qr(quiz_data):
    return

def add_event_text(quiz_data):
    return




# ПОКАЗ ИВЕНОВ
def show_quiz(quiz_id):
    quiz_type = check_quiz_type(quiz_id)
    show_quiz_type = {
    'quiz_qr':show_quiz_qr(quiz_id),
    'quiz_choose': show_quiz_multiple(quiz_id),
    'quiz_text': show_quiz_text(quiz_id)

    }
    
    return show_quiz_type[quiz_type]

# ОПРЕДЕЛИТЬ ТИП КВИЗА - КАЖДЫЙ ХРАНИТСЯ В ОТДЕЛЬНОЙ БД
def check_quiz_type(quiz_id):
    quiz_type = DB_FETCH_ONE(""" 
                 SELECT hse_quiz.quiz_type FROM hse_quiz WHERE quiz_id = %(quiz_id)s;
                 """, 
                 {'quiz_id':quiz_id})
    quiz_type = quiz_type[0]
    return quiz_type


def show_quiz_text(quiz_id):
    quiz_data = DB_JSON(
        """
        SELECT hse_quiz.question, hse_quiz.prize, hse_quiz.right_answer_reply, hse_quiz.wrong_answer_reply, `quiz_text`.* 
        FROM  hse_quiz  JOIN quiz_text ON quiz_text.quiz_id = hse_quiz.quiz_id WHERE 
        quiz_text.quiz_id = %(quiz_id)s; 
        """, {'quiz_id':quiz_id})
    
    
    
    quiz_data_text = {
        'quiz_id': quiz_data[0]['quiz_id'],
        'question': quiz_data[0]['question'],
        'right_answer_reply': quiz_data[0]['right_answer_reply'],
        'wrong_answer_reply': quiz_data[0]['wrong_answer_reply'],
        'correct_ansers': [quiz_data_item['correct_text'] for quiz_data_item in quiz_data]
        
    }
    if quiz_data[0]['prize']!=None: quiz_data_text['prize'] = quiz_data[0]['prize']
    
    quiz_data_text = json.dumps(quiz_data_text,ensure_ascii=False)
    
    return quiz_data_text

def show_quiz_qr(quiz_id):
    quiz_data = {
        'quiz_id':1,
        'quiz_type': 'qr',
    }
    return quiz_data

def show_quiz_one(quiz_id):
    
    return

def show_quiz_multiple(quiz_id):
    return
