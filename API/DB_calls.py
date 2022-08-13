def check_admin(session_token):
    return True

def add_user(user_id, lastname, firstname, username):
    return

def check_quiz_type(quiz_id):
    return

def show_quiz(quiz_id):
    quiz_type = check_quiz_type(quiz_id)
    show_quiz_type = {
    'QR':show_qr_quiz(quiz_id),
    'one_choice': show_one_choice_quiz(quiz_id),
    'multiple_choice': show_mult_choice_quiz(quiz_id)

    }
    
    return show_quiz_type[quiz_type]

# ПОКАЗ ИВЕНТОВ РАЗНЫХ ВИДОВ
def show_qr_quiz(quiz_id):
    quiz_data = {
        'quiz_id':1,
        'quiz_type': 'QR',
    }
    return quiz_data

def show_one_choice_quiz(quiz_id):
    
    return

def show_mult_choice_quiz(quiz_id):
    return
