import React from 'react'

const AddInputCheckboxes = ({text,setText, correct, setCorrect}) => {

    const handleAdd=()=>{
        const newArray=[...text,[]]
        setText(newArray)

        const newCheck = [...correct, []]
        setCorrect(newCheck)
    }
    const handleChange=(onChangeValue,i)=>{
     const inputdata=[...text]
     inputdata[i]=onChangeValue.target.value;
     setText(inputdata)
    }

    const handleChangeBox = (onChangeValue,i) =>{
        const inputdata = [...correct]
        inputdata[i] = onChangeValue.target.value
        setCorrect(inputdata)
    }


    const handleDelete=(i)=>{
        const deleteVal=[...text]
        deleteVal.splice(i,1)
        setText(deleteVal)  

        const deleteCheck = [...correct]
        deleteCheck.splice(i,1)
        setCorrect(deleteCheck)
    }
    



  return (<>
       {/* ПОЛЯ ДЛЯ ДОБАВЛЕНИЯ ПРАВИЛЬНЫХ ОТВЕТОВ */}
       
     <button onClick={()=>handleAdd()}>Добавить ответ</button> 
     <div>
         {text.map((data,i)=>{
             return(
                <div key={`text_${i}`}>
                     <input value={data} onChange={e=>handleChange(e,i)}  />
                </div>
                
             )
         })}

        {correct.map((checkData,i)=>{
                    return(
                        <div key={`check_${i}`} >
                            <input value={checkData} type='checkbox' onChange={e=>handleChangeBox(e,i)} />
                            <button onClick={()=>handleDelete(i)}>x</button>
                        </div>
                        
                    )
                })}

         


    </div>

  
  </>  )
}

export default AddInputCheckboxes