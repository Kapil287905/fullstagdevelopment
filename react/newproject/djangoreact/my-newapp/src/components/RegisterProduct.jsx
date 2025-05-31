import axios from "axios";
import { useEffect, useState } from "react";

export default function RegisterProduct() {
    let [products, setProducts] = useState([]);
    const [newName, setName] = useState("");
    const [newCategory, setCategory] = useState("");
    const [newPrice, setPrice] = useState("");
    const [newPhoto, setPhoto] = useState("");
    const [successMsg, setSuccessMsg] = useState(false);

    async function fetchproduct() {
        axios
            .get("http://127.0.0.1:8000/allproducts/")
            .then((response) => setProducts(response.data))
            .catch((error) => console.error(error));
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        axios
            .post("http://127.0.0.1:8000/addproduct/", {
                name: newName,
                category: newCategory,
                price: newPrice,
                photo: newPhoto,
            })
            .then((response) => {
                fetchproduct();
                setName("");
                setCategory("");
                setPrice("");
                setPhoto("");
                setSuccessMsg(true);
                setTimeout(() => setSuccessMsg(false), 3000);
            });
    };

    useEffect(() => {
        fetchproduct();
    }, []);

    let storedemail = localStorage.getItem("uemail");

    return (
        <div className="container py-5">
            <div className="text-center mb-4">
                <h2 className="fw-bold">Product Dashboard</h2>
                <p className="text-muted">Welcome, <strong>{storedemail}</strong></p>
                <a href="/" className="btn btn-outline-danger btn-sm mt-2">Logout</a>
            </div>

            <div className="row justify-content-center">
                <div className="col-md-8 col-lg-6">
                    <div className="card shadow-sm border-0">
                        <div className="card-body">
                            <h4 className="card-title mb-4 text-primary">Add New Product</h4>

                            {successMsg && (
                                <div className="alert alert-success" role="alert">
                                    Product added successfully!
                                </div>
                            )}

                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label htmlFor="name" className="form-label">Name</label>
                                    <input
                                        type="text"
                                        id="name"
                                        className="form-control"
                                        placeholder="Enter product name"
                                        value={newName}
                                        onChange={(e) => setName(e.target.value)}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="category" className="form-label">Category</label>
                                    <input
                                        type="text"
                                        id="category"
                                        className="form-control"
                                        placeholder="Enter category"
                                        value={newCategory}
                                        onChange={(e) => setCategory(e.target.value)}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="price" className="form-label">Price</label>
                                    <input
                                        type="number"
                                        id="price"
                                        className="form-control"
                                        placeholder="Enter price"
                                        value={newPrice}
                                        onChange={(e) => setPrice(e.target.value)}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="photo" className="form-label">Photo URL</label>
                                    <input
                                        type="text"
                                        id="photo"
                                        className="form-control"
                                        placeholder="Enter image URL"
                                        value={newPhoto}
                                        onChange={(e) => setPhoto(e.target.value)}
                                        required
                                    />
                                </div>
                                <div className="d-grid">
                                    <button type="submit" className="btn btn-primary">
                                        Add Product
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            {products.length > 0 && (
    <>
        <h3 className="mt-5 text-center text-secondary">Product List</h3>
        <div className="table-responsive mt-3">
            <table className="table table-bordered table-hover align-middle">
                <thead className="table-primary">
                    <tr>
                        <th>#</th>
                        <th>Photo</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price ($)</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product, index) => (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>
                                <img
                                    src={product.photo}
                                    alt={product.name}
                                    style={{ width: "60px", height: "60px", objectFit: "cover", borderRadius: "6px" }}
                                />
                            </td>
                            <td>{product.name}</td>
                            <td>{product.category}</td>
                            <td>{product.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    </>
)}

           

        </div>
    );
}
