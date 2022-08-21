import React from 'react'
import { useCallback } from 'react'
import { useRef } from 'react'
import { useState } from 'react'
import ShowSingleQuiz from '../components/QuizPopup'
import useScrollQuiz from '../hooks/useScrollQuiz'
import "../styles/style.css"

const ShowQuizes = () => {
    const [pageNumber, setPageNumber] = useState(1)
    const [quizType, setQuizType] = useState('all')

    const {
        quizes,
        hasMore,
        loading,
        error,
        quizesInfo
    } = useScrollQuiz(pageNumber, quizType)


    const observer = useRef()
    const lastQuizElement = useCallback(node=>{
        if (loading) return
        if (observer.current) observer.current.disconnect()
        observer.current = new IntersectionObserver(entries => {
            if (entries[0].isIntersecting && hasMore){
                // если последний объект доходит до конца страницы, мы добавляем еще страницу
                // тем самым pageNumber изменяется, вызывая useEffect с запросом от axios
                setPageNumber(prevPageNumber => prevPageNumber+1)
                console.log('visible')
            }
        })
        if (node) observer.current.observe(node)
    },[loading,hasMore])

    


    const handleType = (e) =>{
        setQuizType(e.target.value)
        setPageNumber(1)
    }




  return (
      <>
    <button onClick={handleType} value="all" className='quizTypeButton'>Все</button>
    <button onClick={handleType} value="quiz_choose" className='quizTypeButton'>Выбор правильного ответа</button>
    <button onClick={handleType} value="quiz_text" className='quizTypeButton'>Ответ текстом</button>
    <button onClick={handleType} value="quiz_qr" className='quizTypeButton'>Скан QR</button>


    {quizes.map((quiz,index)=>{
        if (quizes.length === index+1){
        return (<>       
        <div className='quizlist-singleItem'>
        <ShowSingleQuiz key={quiz} quiz_id={quiz} quiz_type={quizesInfo[index][0]} question={quizesInfo[index][1]}/>
        <div ref={lastQuizElement} key={`${quiz}_ref`}></div>

        </div>
        </>

        )

        }else{
        return (
            <div className='quizlist-li'>
         <ShowSingleQuiz key={quiz} quiz_id={quiz} quiz_type={quizesInfo[index][0]} question={quizesInfo[index][1]}/>
         </div>
        )
        }
        
    
    })}
    <div>{loading ? "Загрзука..." : null}</div>
    <div> {error ? "Error!":null}</div>
    </>

  )
}

export default ShowQuizes