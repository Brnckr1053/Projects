import React, { useEffect, useState } from 'react'
import axios from 'axios';
import ProductForm from '../components/ProductForm';
import { useParams, useHistory } from "react-router-dom";
    
const Update = (props) => {
    // const { id } = useParams();
    // const [title, setTitle] = useState('');
    // const [price, setPrice] = useState('');
    // const [description, setDescription] = useState('');
    const { id } = useParams();
    const history = useHistory();
    const [product, setProduct] = useState();
    const [loaded, setLoaded] = useState(false);
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/products/' + id)
            .then(res => {
                // setTitle(res.data.title);
                // setPrice(res.data.price);
                // setDescription(res.data.description);
                setProduct(res.data);
                setLoaded(true);
            })
    }, []);
    
    const updateProduct = product => {
        // e.preventDefault();
        axios.put('http://localhost:8000/api/products/' + id, product
        // {
            // title,
            // price,
            // description
        // }
        )
            .then((res) => console.log(res), history.push('/products/' +id))
            // .catch(err => console.error(err));
    }
    
    return (
        <div>
            <h1>Update a Product</h1>
            {loaded && (
                <>
                    <ProductForm
                        onSubmitProp={updateProduct}
                        initialTitle={product.title}
                        initialPrice={product.price}
                        initialDescription={product.description}
                    />
                </>

            )}
            {/* <form onSubmit={updateProduct}>
                <p>
                    <label>Title : </label><br />
                    <input type="text" 
                    name="title" 
                    value={title} 
                    onChange={(e) => { setTitle(e.target.value) }} />
                </p>
                <p>
                    <label>Price : </label><br />
                    <input type="number" 
                    name="price"
                    value={price} 
                    onChange={(e) => { setPrice(e.target.value) }} />
                </p>
                <p>
                    <label>Description : </label><br />
                    <input type="text" 
                    name="description" 
                    value={description} 
                    onChange={(e) => { setDescription(e.target.value) }} />
                </p>
                <input type="submit"  href='/products/'/>
            </form> */}
        </div>
    )
}
    
export default Update;

