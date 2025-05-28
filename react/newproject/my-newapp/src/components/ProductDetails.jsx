import {  useEffect,useState } from "react"
import {useParams} from "react-router-dom"

export default function ProductDetails(){
    const {id}=useParams()
    let [products,setProducts]=useState(null)
    async function fetchproductdetails() {
        let response=await fetch(`https://dummyjson.com/products/${id}`)
        let data=await response.json()
        console.log(data)
        setProducts(data)
    }
    useEffect(()=>{
        fetchproductdetails()
    },[id])

    if(!products){
        return <div>Loading....</div>
    }

    return(
        <>
            <div>
                <h1>ProductDetail</h1>
                <h5 className="cardtitle">{products.title}</h5>
                <p className="catd-text">{products.description}</p>
                <p className="catd-text">Price:{products.price}</p>
            </div>
        </>
    )
}