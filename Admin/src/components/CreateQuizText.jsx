import React from 'react'
import { useState } from 'react';
import axios from 'axios';
import AddInput from './AddInput';

const CreateQuizText = () => {

    const sendQuizText = () =>
    {
        axios.post('/api/admin/createquiz',{
            quiz_type: 'quiz_text',
            question: question,
            right_answer_reply: rightAnswerReply,
            wrong_answer_reply: wrongAnswerReply,
            correct_text: correctText

        }).then((response)=>{
            console.log(response)
        })
        
    }

    const [correctText,setCorrectText]=useState([]);
    const [question, setQuestion] = useState('')
    const [rightAnswerReply, setRightAnswerReply] = useState('Отлично! Правильный ответ.')
    const [wrongAnswerReply, setWrongAnswerReply] = useState('Попробуй еще раз')




 return(
     <>
     <form onSubmit={sendQuizText}>
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



    <label>Правильные ответы</label>
    <AddInput  correctText={correctText} setCorrectText={setCorrectText}/>


        <button type="submit" className="form-button"> СОЗДАТЬ ЗАДАНИЕ</button>
        </div>

    </form>
     </>
 );
 }

export default CreateQuizText