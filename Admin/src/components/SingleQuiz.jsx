import React from 'react'
import { useState } from 'react'
import axios from 'axios'
import { useEffect } from 'react'


const SingleQuiz = ({quiz_id, quiz_type}) => {

    const [rightAnswerReply, setRightAnswerReply] = useState('')
    const [wrongAnswerReply, setWrongAnswerReply] = useState('')
    const [specificInfo, setSpecificInfo] = useState([])


    useEffect(()=>{
        axios.get('/api/admin/quiz_with_type',{
            params:{
                quiz_id: quiz_id,
                quiz_type: quiz_type,

            }

        }).then((response)=>{
            console.log(response)
            setRightAnswerReply(response.data.right_answer_reply)
            setWrongAnswerReply(response.data.wrong_answer_reply)
            switch(quiz_type){
                case 'quiz_choose': 
                    console.log(response.data)
                    break
                case 'quiz_text':
                    console.log(response.data)
                    break
                case 'quiz_qr':
                    console.log(response.data)

                    break
                default:
                    setSpecificInfo(['Ошибка в получении данных.'])
            }
        })
    },[])


  return ( <>     
   <label>Сообщение при правильном ответе</label>
    <p>{rightAnswerReply}</p>

    <label>Сообщение при неверном ответе</label>
    <p>{wrongAnswerReply}</p>

    </>

  )
}

export default SingleQuiz