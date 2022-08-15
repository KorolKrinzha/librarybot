// Формат отображения квизов в формате json

// выбор единственного правильного варианта ответа
// В боте отображаются и right_answers, и wrong_answers, но только выбор переменной из right_answers  считается правильным
const quiz_choose_single = {
  quiz_id: "3",
  question: "Лучшее время для бодрствования",
  right_answer_reply: "Правильный ответ!",
  wrong_answer_reply: "Неправильно(",
  right_answers: ["5 утра"],
  wrong_answers: ["12 дня", "11 вечера"],
};

// то же, что и json выше, но ответов может быть несколько
const quiz_choose_multiple = {
  quiz_id: "2",
  question: "Лучшие дни недели",
  right_answer_reply: "Правильный ответ!",
  wrong_answer_reply: "Неправильно(",
  right_answers: ["Пятница", "Четверг"],
  wrong_answers: ["Среда", "Вторник", "Понедельник"],
};

// квиз, на который надо ответить вводом текста. Остальные введенные слова считаются неверными
const quiz_write_text = {
  quiz_id: "1",
  question: "Любимая еда Артема",
  right_answer_reply: "Да!",
  wrong_answer_reply: "Неправильный ответ",
  right_answers: ["пепси кола", "бургер", "бургер", "апельсин"],
};

// в переменной qr_text отображен текст, он должен совпадать с текстом QR-кода
const quiz_scan_qr = {
  quiz_id: "4",
  question: "Просканируй вот этот QR код",
  right_answer_reply: "Ты его нашел! Молодец!",
  wrong_answer_reply: "Пожаулйста, просканируй его еще раз",
  qr_text: "text displayed in qr code",
};
