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
    'qr':show_quiz_qr(quiz_id),
    'one': show_quiz_one(quiz_id),
    'multiple': show_quiz_multiple(quiz_id),
    'text': show_quiz_text(quiz_id)

    }
    
    return show_quiz_type[quiz_type]

# ОПРЕДЕЛИТЬ ТИП КВИЗА - КАЖДЫЙ ХРАНИТСЯ В ОТДЕЛЬНОЙ БД
def check_quiz_type(quiz_id):
    return


def show_quiz_text(quiz_id):
    return

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
