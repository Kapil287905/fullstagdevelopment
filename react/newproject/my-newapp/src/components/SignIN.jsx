import { useState } from "react"
import Base from "./Base"

export default function SignIN(){
    const[formData,setFormData]=useState({
        uemail:"",
        upass:""
    });
    const[errors,setErrors]=useState({});
    const [submitted,setSubmitted]=useState(false);

    const handleChange=(e)=>{
        const {name,value}=e.target;
        setFormData((prev)=>({
            ...prev,
            [name]:value
        }));
    };

    const validate=()=>{
        let newErrors={}
        let storedemail=localStorage.getItem('uemail')
        let storedupass=localStorage.getItem('upass')
        if(!formData.uemail) newErrors.uemail="Email is required";
        if(!formData.upass) newErrors.upass="Password is required";
        if(formData.uemail!==storedemail) newErrors.uemail="Incorrect Email"
        if(formData.upass!==storedupass) newErrors.upass="Incorrect Password"
        return newErrors
    };

    const handleSubmit=(e)=>{
        e.preventDefault()
        const validateErrors=validate()
        setErrors(validateErrors)
        if(Object.keys(validateErrors).length===0){
            console.log(formData.uemail,formData.upass)
            setSubmitted(true)
            window.location.href='/'
        }
        else{
            setSubmitted(false)
        }
    }



    return(
        <>
        <Base/>
        <div className="container mt-3 mb-5">
            <div className="row">
                <div className="col-md-12" style={{textAlign:"center"}}>
                    <h1>Sign UP</h1>
                    {submitted && <p style={{color:"green"}}>Form submited successfully</p>}
                </div>
                <div className="col-md-6" style={{margin:"0px auto"}}>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                            <input type="email" name="uemail" value={formData.uemail} onChange={handleChange} className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
                            <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
                            {errors.uemail && <p style={{color:"red"}}>{errors.uemail}</p>}
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                            <input type="password" name="upass" value={formData.upass} onChange={handleChange}  className="form-control" id="exampleInputPassword1"/>
                            {errors.upass && <p style={{color:"red"}}>{errors.upass}</p>}
                        </div>                        
                        <div className="mb-3 form-check">
                            <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
                            <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                </div>
            </div>
        </div>
        
        </>
    )
}