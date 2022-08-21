import React from 'react'
import Popup from './Popup'
import { useState } from 'react'
import SingleQuiz from './SingleQuiz'

const ShowSingleQuiz = ({quiz_id, quiz_type, question}) => {
    const [singleQuizPopupOpen, setSingleQuizPopupOpen] = useState(false)




  return ( <>
    <div className='quizlist-singleItem'
    onClick={()=>{
        setSingleQuizPopupOpen(!singleQuizPopupOpen)
        
    }
    }>
        {singleQuizPopupOpen ? <p className='quiz-view-active'>{question}</p> : <p className='quiz-view-inactive'>{question}</p>}

       
    </div>
        {singleQuizPopupOpen && <Popup title={`Просмотр квиза`} setModalOpen={setSingleQuizPopupOpen}>
            <SingleQuiz quiz_type={quiz_type} quiz_id={quiz_id}/> </Popup>}
    </>
  )
}

export default ShowSingleQuiz