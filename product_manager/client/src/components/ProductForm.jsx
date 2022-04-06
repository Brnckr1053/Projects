import React, { useState } from 'react'
import axios from 'axios';
export default (props) => {
    //keep track of what is being typed via useState hook
    const { initialTitle, initialPrice, initialDescription, onSubmitProp } = props;
    const [title, setTitle] = useState(initialTitle); 
    const [price, setPrice] = useState(initialPrice);
    const [description, setDescription] = useState(initialDescription);
    //handler when the form is submitted
    const onSubmitHandler = e => {
        //prevent default behavior of the submit
        e.preventDefault();
        //make a post request to create a new person

    //     axios.post('http://localhost:8000/api/products', {
    //         title,
    //         price,
    //         description
    //     })
    //         .then(res=>console.log(res))
    //         .catch(err=>console.log(err))
    // }
    //onChange to update title and price

        onSubmitProp({title, price, description});
    }

    return (
        <form onSubmit={onSubmitHandler}>
            <p>
                <label>Title : </label><br/>
                <input type="text" name="title" onChange={(e)=>setTitle(e.target.value)} value={title}/>
            </p>
            <p>
                <label>Price : </label><br/>
                <input type="number" name="price" onChange={(e)=>setPrice(e.target.value)} value={price}/>
            </p>
            <p>
                <label>Description : </label><br/>
                <input type="text" name="description" onChange={(e)=>setDescription(e.target.value)} value={description}/>
            </p>
            <input type="submit"/>
        </form>
    )
}

