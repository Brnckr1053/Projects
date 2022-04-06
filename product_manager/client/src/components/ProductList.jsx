import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams, Link } from "react-router-dom";
import DeleteButton from './DeleteButton'
    
const ProductList = (props) => {
    // const [products, setProducts] = useState([]);


    // useEffect(() => {
    //     axios.get('http://localhost:8000/api/products')
    //         .then(res => setProducts(res.data));
    // }, [])
    
    const removeFromDom = productId => {
        props.setProducts(props.products.filter(product => product._id != productId))
    }

    return (
        
            
            
                <div>
                    <label>Title : </label>
                    {props.products.map( (product, i) => {
                        return (
                            <p key={i}>
                                <Link to={'/products/'  + product._id}><p>{product.title}</p></Link>
                                <Link to={"/products/" + product._id + "/edit"}><span>Edit</span></Link> |
                                <DeleteButton productId={product._id} successCallback={()=>removeFromDom(product._id)}/>
                            </p>
                        )
                    })}
                    
                
                </div>
        
    );
}
    
export default ProductList;

