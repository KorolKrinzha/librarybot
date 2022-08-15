import React from 'react'
import { useState } from 'react';
import axios from 'axios';

const CreateQuizText = () => {

    const sendQuizText = () =>
    {
        axios.post('/api/admin/createquiz',{
            quiz_type: quiztype,
            question: question,
            right_answer_reply: rightAnswerReply,
            wrong_answer_reply: wrongAnswerReply,
            correcttext: correctText

        }).then((response)=>{
            console.log(response)
        })
        
    }

    const [correctText,setCorrectText]=useState([]);
    const [quiztype, setQuiztype] = useState('quiz_text')
    const [question, setQuestion] = useState('')
    const [rightAnswerReply, setRightAnswerReply] = useState('')
    const [wrongAnswerReply, setWrongAnswerReply] = useState('')




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

     <label htmlFor="title">Вопрос задания</label>
          <input 
          required
          type="text"
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          ></input>

     
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

</form>
     </>
 );
 }

export default CreateQuizText