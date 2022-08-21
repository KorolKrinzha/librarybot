import React from 'react'
import Popup from './Popup'
import { useState } from 'react'
import SingleQuiz from './SingleQuiz'

const ShowSingleQuiz = ({quiz_id, quiz_type, question}) => {
    const [singleQuizPopupOpen, setSingleQuizPopupOpen] = useState(false)




  return ( <>
    <div onClick={()=>{
        setSingleQuizPopupOpen(!singleQuizPopupOpen)
        
    }
    }>
        {question}
    </div>
        {singleQuizPopupOpen && <Popup title={`Просмотр квиза`} setModalOpen={setSingleQuizPopupOpen}>
            <SingleQuiz quiz_type={quiz_type} quiz_id={quiz_id}/> </Popup>}
    </>
  )
}

export default ShowSingleQuiz