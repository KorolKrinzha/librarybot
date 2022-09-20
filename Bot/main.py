import string
import time
import telebot
import logging
import random
import json
import bot_tools.qr_code_recognition
from API import main as api
from telebot import types

import API.main

bot = telebot.TeleBot('5302892924:AAHxwt87L2JPbXsFtQyVayP5VtX6SVvD5Kk')

logger = logging.getLogger(__name__)
text_question_data = {
    "quiz_id": "001_2bb9e34ba27248f5973a2ecdd105f1ed",
    "quiz_type": "text",
    "question": "Вопрос? Прав. ответ: ав",
    "right_answer_reply": "Отлично! Правильный ответ.",
    "wrong_answer_reply": "Попробуй еще раз",
    "right_answers": ["ав"]
}
qr_question_data = {
    "quiz_id": "001_2bb9e34ba27248f5973a2ecdd105f1ed",
    "quiz_type": "qr",
    "question": "Вопрос? Прав. Ответ: qr с текстом cryptic qr",
    "right_answer_reply": "Отлично! Правильный ответ.",
    "wrong_answer_reply": "Попробуй еще раз1",
    "qr_text": "cryptic qr"
}
choose_question_data = {
    "quiz_id": "001_93c8a389b8f54e85837fcefef26065f6",
    "quiz_type": "choose",
    "question": "Здесь вопрос Прав. ответ: аааа",
    "right_answer_reply": "Отлично! Правильный ответ.",
    "wrong_answer_reply": "Попробуй еще раз2",
    "right_answers": ["аааа"],
    "wrong_answers": ["а"]
}
current_quiz = {}
all_answers = {}  # для выбора вариантов ответа
user_answers = []  # для выбора вариантов ответа
chosen_answers = {}  # для выбора вариантов ответа
all_questions = [qr_question_data,text_question_data]
current_quiz_number = {}  #
total_points = {}  #


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    if not api.api_getuser(user_id):
        registration(user_id, last_name, first_name, user_name)
    current_quiz_number[message.from_user.id] = 0
    total_points[message.from_user.id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Квиз")
    btn2 = types.KeyboardButton("О боте")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Приветствуем тебя в боте для Библиотеки ВШЭ".format(
                         message.from_user), reply_markup=markup)


def cleaner(message):
    current_quiz_number[message.from_user.id] = 0
    total_points[message.from_user.id] = 0
    all_answers[message.from_user.id] = None
    user_answers.clear()
    chosen_answers[message.from_user.id] = None


@bot.message_handler(
    func=lambda message: message.text in ["О боте", "Главное меню", "Квиз", "Начать квиз", "Следующий вопрос", "Пройти заново"])
def func(message):
    if message.text == "О боте":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Главное меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Бла-бла-бла", reply_markup=markup)
    elif message.text == "Квиз":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать квиз")
        btn2 = types.KeyboardButton("Главное меню")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Выбирай:", reply_markup=markup)
    elif message.text == "Главное меню":
        cleaner(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Квиз")
        btn2 = types.KeyboardButton("О боте")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Приветствуем тебя в боте для Библиотеки ВШЭ".format(
                             message.from_user), reply_markup=markup)
    elif message.text == "Начать квиз" or message.text == "Следующий вопрос":
        # quizes = api.show_all()
        quiz_transition(message)
    elif message.text == "Пройти заново":
        cleaner(message)
        quiz_transition(message)


def registration(user_id, last_name, first_name, user_name):
    api.api_adduser(user_id, last_name, first_name, user_name)


def quiz_transition(message):
    if len(all_questions) <= current_quiz_number[message.from_user.id]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пройти заново")
        btn2 = types.KeyboardButton("Главное меню")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,
                         text="Поздравляем тебя с прохождением квиза!".format(
                             message.from_user), reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,
                         text=f'Всего у тебя: {total_points[message.from_user.id]} баллов!'.format(
                             message.from_user), reply_markup=markup)
    else:
        current_quiz[message.from_user.id] = all_questions[current_quiz_number[message.from_user.id]]
        if current_quiz[message.from_user.id]["quiz_type"] == "text":
            text_question(message, current_quiz[message.from_user.id])
        elif current_quiz[message.from_user.id]["quiz_type"] == "qr":
            qr_question(message, current_quiz[message.from_user.id])
        elif current_quiz[message.from_user.id]["quiz_type"] == "choose":
            choose_question(message)
        current_quiz_number[message.from_user.id] += 1


def text_question(message, data):
    total_points[message.from_user.id] += 200
    msg = bot.send_message(message.chat.id, text=data["question"].format(
        message.from_user), reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, text_answer)


def text_answer(message):
    if message.text in current_quiz[message.from_user.id]["right_answers"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Следующий вопрос")
        markup.add(btn1)
        bot.send_message(message.chat.id, text=str(current_quiz[message.from_user.id]["right_answer_reply"]).format(
            message.from_user), reply_markup=markup)
    else:
        total_points[message.from_user.id] -= 10
        msg = bot.send_message(message.chat.id,
                               text=str(current_quiz[message.from_user.id]["wrong_answer_reply"]).format(
                                   message.from_user))
        bot.register_next_step_handler(msg, text_answer)


def qr_question(message, data):
    total_points[message.from_user.id] += 200
    msg = bot.send_message(message.chat.id, text=data["question"].format(
        message.from_user), reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, qr_answer)


def qr_answer(message):
    if bot_tools.qr_code_recognition.photo(bot, message) == current_quiz[message.from_user.id]["qr_text"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Следующий вопрос")
        markup.add(btn1)
        bot.send_message(message.chat.id, text=str(current_quiz[message.from_user.id]["right_answer_reply"]).format(
            message.from_user), reply_markup=markup)
    else:
        total_points[message.from_user.id] -= 10
        msg = bot.send_message(message.chat.id,
                               text=str(current_quiz[message.from_user.id]["wrong_answer_reply"]).format(
                                   message.from_user))
        bot.register_next_step_handler(msg, qr_answer)


@bot.poll_answer_handler()
def handle_poll_answer(answer):
    user_answers.clear()
    user_answers.extend(answer.option_ids)  # это очень плохо


def choose_question(message):
    total_points[message.from_user.id] += 200
    all_answers[message.from_user.id] = (
                current_quiz[message.from_user.id]["right_answers"] + current_quiz[message.from_user.id][
            "wrong_answers"])
    random.shuffle(all_answers[message.from_user.id])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Далее")
    markup.add(btn)
    msg = bot.send_poll(message.chat.id, current_quiz[message.from_user.id]["question"],
                        all_answers[message.from_user.id],
                        allows_multiple_answers=True,
                        is_anonymous=False, reply_markup=markup)
    bot.register_next_step_handler(msg, choose_answer)


def choose_answer(message):
    # while user_answers[message.from_user.id] is None:
    #  time.sleep(2)
    bot.send_message(message.chat.id, text=str(user_answers).format(
        message.from_user))
    chosen_answers[message.from_user.id] = []
    for i in user_answers:
        chosen_answers[message.from_user.id].append(all_answers[message.from_user.id][int(i)])
    if sorted(chosen_answers[message.from_user.id]) == sorted(current_quiz[message.from_user.id]["right_answers"]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Следующий вопрос")
        markup.add(btn1)
        bot.send_message(message.chat.id, text=str(current_quiz[message.from_user.id]["right_answer_reply"]).format(
            message.from_user), reply_markup=markup)
    else:
        total_points[message.from_user.id] -= 10
        msg = bot.send_message(message.chat.id,
                               text=str(current_quiz[message.from_user.id]["wrong_answer_reply"]).format(
                                   message.from_user),
                               reply_markup=types.ReplyKeyboardRemove())
        choose_question(msg)


bot.polling(none_stop=True)
