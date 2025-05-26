import { useEffect, useState } from "react"

export default function Product(){

    let [products,setProducts]=useState([])

    async function fetchproduct() {
        let response=await fetch('https://dummyjson.com/products')
        let data=await response.json()
        console.log(data)
        setProducts(data.products)
    }
    useEffect(()=>{
        fetchproduct()
    },[])

    return(
        <div className="container">
            <div className="row">
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
                                    <a href={`/productdetails/${p.id}`} className="btn btn-primary">View More</a>
                                </div>
                                </div>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )

}