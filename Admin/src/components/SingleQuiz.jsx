import React from 'react'
import { useState } from 'react'
import axios from 'axios'
import { useEffect } from 'react'
import { ReactComponent as CloseButton} from '../assets/deletebutton.svg' 



const SingleQuiz = ({quiz_id, quiz_type}) => {

    const [rightAnswerReply, setRightAnswerReply] = useState('')
    const [wrongAnswerReply, setWrongAnswerReply] = useState('')
    const [textInfo, setTextInfo] = useState([])
    const [rightAnswersForChoose, setRightAnswersForChoose] = useState([])
    const [wrongAnswersForChoose, setWrongAnswersForChoose] = useState([])
    const [qrText, setQrText] = useState('')



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
                    console.log(quiz_type)
                    setRightAnswersForChoose(response.data.right_answers)
                    setWrongAnswersForChoose(response.data.wrong_answers)
                    break
                case 'quiz_text':
                    console.log(quiz_type)
                    setTextInfo(response.data.right_answers)
                    break
                case 'quiz_qr':
                    setQrText(response.data.qr_text)


                    break
                default:
                    
            }
        })
    },[])

    const deleteQuiz = (e)=>{
        e.preventDefault()
        axios.post("/api/admin/deletequiz",{
            quiz_id:quiz_id,            
            withCredentials:true
        }).then((response)=>{
            if (response.status===200) window.location.reload();

        }).catch((error)=>{
            console.log(error)
        })

    }


    


  return ( <div className='quiz-view'>    
              <button className='svg-button mt-3'
            onClick={(e) => 
              deleteQuiz(e)
            }
          >
            <CloseButton/>
    </button> 
   <label>Сообщение при правильном ответе</label>
    <p>{rightAnswerReply}</p>

    <label>Сообщение при неверном ответе</label>
    <p>{wrongAnswerReply}</p>

    {(
        ()=>{
            switch(quiz_type){
                case 'quiz_choose': 
                return(<>
                <label>Правильные ответы</label>
                {rightAnswersForChoose.map((info, index)=>{
                    return (
                        <p key={index}>{info}</p>
                    )
                })}

                
                <label>Неверные ответы</label>
                {wrongAnswersForChoose.map((info, index)=>{
                    return (
                        <p key={index}>{info}</p>
                    )
                })}


                </>)
                
                
            case 'quiz_text':
                return(<>
                {console.log('switch activated')}
                <label>Правильные текстовые ответы</label>
                {textInfo.map((info, index)=>{
                    return (
                        <p key={index}>{info}</p>
                    )
                })}
    
                </>)
                
            case 'quiz_qr':
                return (<>
                    <label>Текст QR-кода</label>
                    <p>{qrText}</p>
                    </>)
    
            
            default:
                return (<>
                <p>Ошибка в получении данных</p></>)
    
            }
        }
    )()}

    
    </div>

  )
}

export default SingleQuiz