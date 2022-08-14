-- CREATE DATABASE libarybot;
-- USE libarybot;
CREATE TABLE hse_users (
	user_id VARCHAR(10) NOT NULL,
    lastname VARCHAR(300) NOT NULL,
    firstname VARCHAR(300) NOT NULL,
    username VARCHAR(300) NULL,
    PRIMARY KEY(user_id),
    UNIQUE (username)
);

CREATE TABLE hse_quiz(
	quiz_id VARCHAR(100) NOT NULL,
    quiz_type VARCHAR(100) NOT NULL,
    prize VARCHAR(200) NULL,
    question VARCHAR(200) NOT NULL,
    right_answer_reply VARCHAR(200) NULL,
    wrong_answer_reply VARCHAR(200) NULL,
    PRIMARY KEY (quiz_id)
    
);


CREATE TABLE user_completion (
	user_id VARCHAR(10) NOT NULL,
    quiz_id VARCHAR(100) NOT NULL,
    PRIMARY KEY(user_id, quiz_id),
    FOREIGN KEY (user_id) REFERENCES hse_users (user_id) ON UPDATE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES hse_quiz (quiz_id) ON UPDATE CASCADE
);

-- ТИПЫ КВИЗОВ
CREATE TABLE quiz_choose(
	choose_id SERIAL PRIMARY KEY,
	quiz_id VARCHAR(100) NOT NULL,
    option_text VARCHAR(200),
    option_correct BOOL,
    FOREIGN KEY (quiz_id) REFERENCES hse_quiz (quiz_id) ON UPDATE CASCADE
);



CREATE TABLE quiz_text (
	text_id SERIAL PRIMARY KEY,
	quiz_id VARCHAR(100) NOT NULL,
    correct_text VARCHAR(200),
    
    FOREIGN KEY (quiz_id) REFERENCES hse_quiz (quiz_id) ON UPDATE CASCADE
);

CREATE TABLE quiz_qr (
	quiz_id VARCHAR(100) NOT NULL,
    qr_text VARCHAR(200),
    PRIMARY KEY(quiz_id),
    FOREIGN KEY (quiz_id) REFERENCES hse_quiz (quiz_id) ON UPDATE CASCADE
    
);

-- МЕТРИКИ И ЛОГИ
CREATE TABLE user_logins(
	user_id VARCHAR(10) NOT NULL,
    login_time DATETIME,
    PRIMARY KEY(user_id),
    FOREIGN KEY (user_id) REFERENCES hse_users (user_id) ON UPDATE CASCADE
);

CREATE TABLE user_logs(
	user_id VARCHAR(10) NOT NULL,
    quiz_id VARCHAR(100) NOT NULL,
    prize VARCHAR(200) NULL,
    PRIMARY KEY(user_id, quiz_id),
	FOREIGN KEY (user_id) REFERENCES hse_users (user_id) ON UPDATE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES hse_quiz (quiz_id) ON UPDATE CASCADE
);


