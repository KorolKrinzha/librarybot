import React from 'react'
import { useState } from 'react';
import axios from 'axios';
import AddInput from './AddInput';
import TemplateQuiz from './TemplateQuiz';
import AddInputCheckboxes from './AddInputCheckboxes';

const CreateQuizChoice = () => {

    const sendQuizChoice = () =>
    {
        axios.post('/api/admin/createquiz',{
            quiz_type: 'quiz_choose',
            question: question,
            right_answer_reply: rightAnswerReply,
            wrong_answer_reply: wrongAnswerReply,
            option_text: text,
            option_correct: correct

        }).then((response)=>{
            console.log(response)
        })
        
    }

    const [text,setText]=useState([]);
    const [correct, setCorrect] = useState([])
    const [question, setQuestion] = useState('')
    const [rightAnswerReply, setRightAnswerReply] = useState('Отлично! Правильный ответ.')
    const [wrongAnswerReply, setWrongAnswerReply] = useState('Попробуй еще раз')




 return(
     <>
     <TemplateQuiz question={question} setQuestion={setQuestion} rightAnswerReply={rightAnswerReply} setRightAnswerReply={setRightAnswerReply}
     wrongAnswerReply={wrongAnswerReply} setWrongAnswerReply={setWrongAnswerReply} sendQuiz={sendQuizChoice}>


     </TemplateQuiz>

     <AddInputCheckboxes text={text} setText={setText} correct={correct} setCorrect={setCorrect}/>


     </>
 );
 }

export default CreateQuizChoice