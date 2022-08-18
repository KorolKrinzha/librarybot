import React from 'react'

const AddInput = ({correctText,setCorrectText}) => {

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
    



  return (<>
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

  
  </>  )
}

export default AddInput