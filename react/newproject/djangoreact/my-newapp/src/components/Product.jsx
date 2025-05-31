import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Base from "./Base";
import axios from "axios";

export default function Product() {
    let [products, setProducts] = useState([]);
    const [searchTerm, setSearchTerm] = useState("");

    async function fetchproduct() {
        axios
            .get("http://127.0.0.1:8000/allproducts/")
            .then((response) => setProducts(response.data))
            .catch((error) => console.error(error));
    }

    useEffect(() => {
        fetchproduct();
    }, []);

    const show_search = async () => {
        if (searchTerm.trim() === "") return;
        const response = await fetch(
            `https://dummyjson.com/products/search?q=${searchTerm}`
        );
        const data = await response.json();
        setProducts(data.products);
    };

    const fetchelectronics = async () => {
        const response = await fetch(
            "https://dummyjson.com/products/category/laptops"
        );
        const data = await response.json();
        setProducts(data.products);
    };

    const fetchmobile = async () => {
        const response = await fetch(
            "https://dummyjson.com/products/category/smartphones"
        );
        const data = await response.json();
        setProducts(data.products);
    };

    return (
        <Base searchTerm={searchTerm} setSearchTerm={setSearchTerm} onSearch={show_search}>
            <div className="container mt-4">
                <div className="d-flex justify-content-center flex-wrap gap-2 mb-4">
                    <button onClick={fetchmobile} className="btn btn-outline-primary">
                        Mobiles
                    </button>
                    <button onClick={fetchelectronics} className="btn btn-outline-success">
                        Electronics
                    </button>
                    <button className="btn btn-outline-warning">Shoes</button>
                    <button className="btn btn-outline-info">Clothes</button>
                </div>

                <div className="row">
                    {products &&
                        products.map((p) => (
                            <div className="col-md-6 col-lg-4 col-xl-3 mb-4" key={p.id}>
                                <div className="card h-100 shadow-sm">
                                    <img
                                        src={p.photo}
                                        className="card-img-top"
                                        alt={p.name}
                                        style={{ height: "200px", objectFit: "cover" }}
                                    />
                                    <div className="card-body d-flex flex-column">
                                        <h5 className="card-title">{p.name}</h5>
                                        <p className="card-text text-muted mb-1">{p.category}</p>
                                        <p className="card-text fw-bold">₹{p.price}</p>
                                        <Link to={`/productdetails/${p.id}`} className="btn btn-primary mt-auto">
                                            View Details
                                        </Link>
                                    </div>
                                </div>
                            </div>
                        ))}
                </div>
            </div>
        </Base>
    );
}
