import json
from DB_tools import DB_JSON, DB_JSON_NONULL, DB_COMMIT, DB_FETCH_ONE, DB_CHECK_EXISTENCE, DB_COMMIT_MULTIPLE, create_id



def check_admin(session_token):
    return True

def add_user(user_id, lastname, firstname, username):
    return


# СОЗДАНИЕ ИВЕНТА
def add_quiz(quiz_type, quiz_data):
    create_quiz_type = {
    'quiz_qr':add_quiz_qr,
    'quiz_choose': add_quiz_choose,
    'quiz_text': add_quiz_text
    }
    
    create_quiz_type[quiz_type](quiz_data=quiz_data)
    
    return



def add_quiz_choose(quiz_data):
    quiz_id = create_id()
    DB_COMMIT(""" 
              INSERT INTO hse_quiz (quiz_id,quiz_type, question, right_answer_reply, wrong_answer_reply) 
              VALUES (%(quiz_id)s, %(quiz_type)s, %(question)s, %(right_answer_reply)s, %(wrong_answer_reply)s);
              """, {'quiz_id':quiz_id,
                    'quiz_type': 'quiz_choose',
                    'question':quiz_data['question'],
                    'right_answer_reply': quiz_data['right_answer_reply'],
                    'wrong_answer_reply': quiz_data['wrong_answer_reply']})
    
    choose_insert_values = [(quiz_id, quiz_data['option_text'][i], quiz_data['option_correct'][i])  for i in range(len(quiz_data['option_text'])) ]

    DB_COMMIT_MULTIPLE("""
              INSERT INTO quiz_choose (quiz_id, option_text, option_correct)  VALUES
              (%s,%s, %s)""", choose_insert_values)
    print(choose_insert_values)
    


    return


def add_quiz_qr(quiz_data):
    return

def add_quiz_text(quiz_data):
    quiz_id = create_id()
    DB_COMMIT(""" 
              INSERT INTO hse_quiz (quiz_id,quiz_type, question, right_answer_reply, wrong_answer_reply) 
              VALUES (%(quiz_id)s, %(quiz_type)s, %(question)s, %(right_answer_reply)s, %(wrong_answer_reply)s);
              """, {'quiz_id':quiz_id,
                    'quiz_type': 'quiz_text',
                    'question':quiz_data['question'],
                    'right_answer_reply': quiz_data['right_answer_reply'],
                    'wrong_answer_reply': quiz_data['wrong_answer_reply']})
    
    text_insert_values = [(quiz_id, correct_text)  for correct_text in quiz_data['correct_text'] ]
    

    
    DB_COMMIT_MULTIPLE("""
              INSERT INTO quiz_text (quiz_id, correct_text)  VALUES
              (%s,%s)""", text_insert_values)
    
        
            
    return




# ПОКАЗ ИВЕНОВ
def show_quiz(quiz_id):
    quiz_type = check_quiz_type(quiz_id)
    show_quiz_type = {
    'quiz_qr':show_quiz_qr,
    'quiz_choose': show_quiz_choose,
    'quiz_text': show_quiz_text

    }
    
    return show_quiz_type[quiz_type](quiz_id)

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
        SELECT hse_quiz.question, hse_quiz.prize, hse_quiz.right_answer_reply, hse_quiz.wrong_answer_reply, quiz_text.* 
        FROM  hse_quiz  JOIN quiz_text ON quiz_text.quiz_id = hse_quiz.quiz_id WHERE 
        quiz_text.quiz_id = %(quiz_id)s; 
        """, {'quiz_id':quiz_id})
    
    
    
    quiz_data_text = {
        'quiz_id': quiz_data[0]['quiz_id'],
        'question': quiz_data[0]['question'],
        'right_answer_reply': quiz_data[0]['right_answer_reply'],
        'wrong_answer_reply': quiz_data[0]['wrong_answer_reply'],
        'right_answers': [quiz_data_item['correct_text'] for quiz_data_item in quiz_data]
        
    }
    if quiz_data[0]['prize']!=None: quiz_data_text['prize'] = quiz_data[0]['prize']
    
    quiz_data_text = json.dumps(quiz_data_text,ensure_ascii=False)
    
    return quiz_data_text

def show_quiz_qr(quiz_id):
    quiz_data = DB_JSON(
        """ 
        SELECT hse_quiz.question, hse_quiz.prize, hse_quiz.right_answer_reply, hse_quiz.wrong_answer_reply, quiz_qr.* 
        FROM  hse_quiz  JOIN quiz_qr ON quiz_qr.quiz_id = hse_quiz.quiz_id WHERE quiz_qr.quiz_id = %(quiz_id)s;

        """,{'quiz_id':quiz_id})
    
    quiz_data_qr = {
        'quiz_id': quiz_data[0]['quiz_id'],
        'question': quiz_data[0]['question'],
        'right_answer_reply': quiz_data[0]['right_answer_reply'],
        'wrong_answer_reply': quiz_data[0]['wrong_answer_reply'],
        'qr_text': quiz_data[0]['qr_text'],

        
    }
    if quiz_data[0]['prize']!=None: quiz_data_qr['prize'] = quiz_data[0]['prize']
    
    quiz_data_qr = json.dumps(quiz_data_qr,ensure_ascii=False)

    
    return quiz_data_qr

def show_quiz_choose(quiz_id):
    quiz_data = DB_JSON(
        """ 
        SELECT hse_quiz.question, hse_quiz.prize, hse_quiz.right_answer_reply, hse_quiz.wrong_answer_reply, quiz_choose.* 
        FROM  hse_quiz  JOIN quiz_choose ON quiz_choose.quiz_id = hse_quiz.quiz_id WHERE quiz_choose.quiz_id = %(quiz_id)s;
        """, 
        {'quiz_id':quiz_id}
        )
    
    quiz_data_choose = {
        'quiz_id': quiz_data[0]['quiz_id'],
        'question': quiz_data[0]['question'],
        'right_answer_reply': quiz_data[0]['right_answer_reply'],
        'wrong_answer_reply': quiz_data[0]['wrong_answer_reply'],
        'right_answers': [quiz_data_item['option_text'] for quiz_data_item in quiz_data if  quiz_data_item['option_correct']],
        'wrong_answers': [quiz_data_item['option_text'] for quiz_data_item in quiz_data if  not quiz_data_item['option_correct']]

        
    }
    if quiz_data[0]['prize']!=None: quiz_data_choose['prize'] = quiz_data[0]['prize']
    
    quiz_data_choose = json.dumps(quiz_data_choose,ensure_ascii=False)

    
    return quiz_data_choose

def show_all():
     
    quizes = DB_JSON(""" 
SELECT hse_quiz.quiz_id, 
hse_quiz.quiz_type, 
hse_quiz.right_answer_reply, 
hse_quiz.wrong_answer_reply, 
hse_quiz.prize,
quiz_choose.option_text, 
quiz_choose.option_correct, 
quiz_text.correct_text, 
quiz_qr.qr_text 
FROM hse_quiz LEFT JOIN quiz_choose on hse_quiz.quiz_id=quiz_choose.quiz_id 
LEFT JOIN quiz_text on hse_quiz.quiz_id = quiz_text.quiz_id left JOIN quiz_qr on hse_quiz.quiz_id=quiz_qr.quiz_id;
                   """, {})
    return quizes

def show_all_preview(quiz_type, pagenumber):
    quizes_preview = {}
    pagenumber = int(pagenumber)
    quizes_per_page = 10
    offset = (10*(pagenumber-1))-(pagenumber-1)
    limit = pagenumber*quizes_per_page
    print(limit)
    print(pagenumber)
    print(offset)
    if quiz_type=="all" and len(quiz_type)>0:
        quizes_preview = DB_JSON("""
                                SELECT quiz_id, quiz_type, question FROM hse_quiz LIMIT %(limit)s OFFSET %(offset)s;
                                """, {'limit': limit,
                                      'offset': offset})
    else:
        quizes_preview = DB_JSON(""" 
                                 SELECT quiz_id, quiz_type, question FROM hse_quiz WHERE quiz_type=%(quiz_type)s LIMIT %(limit)s OFFSET %(offset)s;
                                 """, {'quiz_type':quiz_type,
                                       'limit': limit,
                                       'offset': offset})
        
    
    quizes_count = DB_FETCH_ONE("""
                                SELECT COUNT(*) FROM hse_quiz;
                                """, {})
    
    return {'quizes':quizes_preview, 'count':quizes_count[0]}