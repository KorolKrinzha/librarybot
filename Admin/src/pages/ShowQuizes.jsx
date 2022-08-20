import React from 'react'
import { useCallback } from 'react'
import { useRef } from 'react'
import { useState } from 'react'
import useScrollQuiz from '../hooks/useScrollQuiz'
import "../styles/style.css"

const ShowQuizes = () => {
    const [pageNumber, setPageNumber] = useState(1)
    const [quizType, setQuizType] = useState('all')

    const {
        quizes,
        hasMore,
        loading,
        error
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
            }
        })
        if (node) observer.current.observe(node)
    },[loading,hasMore])

    


    const handleType = (e) =>{
        setQuizType(e.target.value)
        setPageNumber(1)
        console.log(e.target.value)
    }




  return (
      <>
    <button onClick={handleType} value="all">Все</button>
    <button onClick={handleType} value="quiz_choose">Выбор правильного ответа</button>
    <button onClick={handleType} value="quiz_text">Ответ текстом</button>
    <button onClick={handleType} value="quiz_qr">Скан QR</button>


    {quizes.map((quiz,index)=>{
        if (quizes.length === index+1){
        return <div key={quiz} ref={lastQuizElement} className='display-1'>{quiz}</div>
        }else{
        return <div key={quiz} className='display-1'>{quiz}</div>
        }
    })}
    <div>{loading ? "Loading..." : null}</div>
    <div> {error ? "Error!":null}</div>
    </>

  )
}

export default ShowQuizes