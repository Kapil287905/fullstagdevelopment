import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import Base from "./Base"


export default function Product(){

    let [products,setProducts]=useState([]);
    const [searchTerm,setSearchTerm,]=useState('');

    async function fetchproduct() {
        let response=await fetch('https://dummyjson.com/products')
        let data=await response.json()
        console.log(data)
        setProducts(data.products)
    }
    useEffect(()=>{
        fetchproduct()
    },[])

    const show_search=async()=>{
        if(searchTerm.trim()==='') return;
        const response=await fetch(`https://dummyjson.com/products/search?q=${searchTerm}`)
        const data=await response.json();
        setProducts(data.products)
        console.log(data)
    }

    const fetchelectronics=async()=>{
        const response=await fetch('https://dummyjson.com/products/category/laptops')
        const data=await response.json();
        setProducts(data.products)
    }

    const fetchmobile=async()=>{
        const response=await fetch('https://dummyjson.com/products/category/smartphones')
        const data=await response.json();
        setProducts(data.products)
    }

    return(
        <>
        <Base searchTerm={searchTerm} setSearchTerm={setSearchTerm} onSearch={show_search}/>
        <div className="container mt-2 mb-3">
            <a href="#smartphones" onClick={fetchmobile}>Mobile</a>&nbsp;&nbsp;
            <a href="#laptops" onClick={fetchelectronics}>Electronics</a>&nbsp;&nbsp;
            <a href="#">Shoes</a>&nbsp;&nbsp;
            <a href="#">Cloths</a>&nbsp;&nbsp;
        </div>
        <div className="container mt-3">            
            <div className="row mb-5">
                {
                    products && products.map((p,index)=>{
                        return(
                            <div className="col-md-3 mb-3" key={p.id}>
                                <div className="card" style={{width: 18+"rem"}}>
                                <img src={p.thumbnail} className="card-img-top" alt={p.title}/>
                                <div className="card-body">
                                    <h5 className="card-title">{p.title}</h5>
                                    <p className="card-text">{p.description}</p>
                                    <p className="card-text">Price:{p.price}</p>
                                    <Link to={`/productdetails/${p.id}`} className="btn btn-primary">View More</Link>
                                </div>
                                </div>
                            </div>
                        )
                    })
                }
            </div>
        </div>
        </>
    )

}