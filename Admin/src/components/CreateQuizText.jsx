import React from 'react'
import { useState } from 'react';
import axios from 'axios';

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




    const handleAdd=()=>{
        const newArray=[...correctText,[]]
        setCorrectText(newArray)
    }
    const handleChange=(onChangeValue,i)=>{
     const inputdata=[...correctText]
     inputdata[i]=onChangeValue.target.value;
     setCorrectText(inputdata)
    }
    const handleDelete=(i)=>{
        const deleteVal=[...correctText]
        deleteVal.splice(i,1)
        setCorrectText(deleteVal)  
    }
    
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
     {/* ПОЛЯ ДЛЯ ДОБАВЛЕНИЯ ПРАВИЛЬНЫХ ОТВЕТОВ */}
     { correctText.length===0 ?
     <button onClick={()=>handleAdd()}>Добавить ответ</button> : null }
         {correctText.map((data,i)=>{
             return(
                <div>
                     <input value={data} onChange={e=>handleChange(e,i)} />
                     <button onClick={()=>handleDelete(i)}>x</button>
                     { i+1===correctText.length ? 
                     <button onClick={()=>handleAdd()} key={i}>Добавить ответ</button> : null}
                </div>
                
             )
         })}

        <button type="submit" className="form-button"> СОЗДАТЬ ЗАДАНИЕ</button>
        </div>

    </form>
     </>
 );
 }

export default CreateQuizText