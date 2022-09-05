import React, { useState } from 'react'
import CreateQuizChoice from '../components/CreateQuizChoose'
import CreateQuizText from '../components/CreateQuizText'

const CreateQuiz = () => {
  const [quizType,setQuizType]  = useState('')

  const handleType = (e) =>{
    setQuizType(e.target.value)
}



  return (
    <>
    <button onClick={handleType} value="quiz_choose" className='quizTypeButton'>Выбор правильного ответа</button>
    <button onClick={handleType} value="quiz_text" className='quizTypeButton'>Ответ текстом</button>
    <button onClick={handleType} value="quiz_qr" className='quizTypeButton'>Скан QR</button>

        {(

          ()=>{
            switch(quizType){
              case 'quiz_choose':
                return (<>
                <CreateQuizChoice/>
                </>)
              
              case 'quiz_text':
                return (<>
                <CreateQuizText/>
                </>)
              
              case 'quiz_qr':
                return (<>
                </>)

              default:
                  return(<>
                  <p>Выберите тип квиза, который вы хотите создать</p>
                  </>)

            }
          }
        )()}
            </>
    
  )
}

export default CreateQuiz