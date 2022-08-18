import React from 'react'
import { useState } from 'react';
import axios from 'axios';
import AddInput from './AddInput';

const TemplateQuiz = ({question, setQuestion, rightAnswerReply,setRightAnswerReply, 
    wrongAnswerReply, setWrongAnswerReply, sendQuiz, ...props }) => {


 return(
     <>
     <form onSubmit={sendQuiz}>
     <div className="formSection bg-grey">


     <label htmlFor="question">Вопрос задания</label>
          <input 
          type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          ></input>

    <label htmlFor="rightAnswerReply">Сообщение при правильном вводе</label>
          <input 
          type="text"
          required
            value={rightAnswerReply}
            onChange={(e) => setRightAnswerReply(e.target.value)}
          ></input>

        <label htmlFor="wrongAnswerReply">Сообщение при неправильном вводе</label>
          <input 
          type="text"
          required
            value={wrongAnswerReply}
            onChange={(e) => setWrongAnswerReply(e.target.value)}
          ></input>



        {props.children}

        <button type="submit" className="form-button"> СОЗДАТЬ ЗАДАНИЕ</button>
        </div>

    </form>
     </>
 );
 }

export default TemplateQuiz