const containerStyle={
    border:"1px solid #ddd",
    padding:"20px",
    borderRadus:"8px",
    maxWidth:"500px",
    margin:"20px auto",
    backgroundColor:"#a39f9f",
    bocShadow:"0 4px 8px rgba(0,0,0,0.1)"
}

const titlestyle={
    fontSize:"20px",
    fontWeight:"bold",
    color:"#777",
    marginBottom:"10px"
}



const Contact=({name,email,phone,address})=>{
    return(
        <div style={containerStyle}>
            <h2 style={titlestyle}>{name}</h2>
            <p><strong>EMail: </strong>{email}</p>
            <p><strong>Phone: </strong>{phone}</p>
            <p><strong>Address: </strong>{address}</p>
        </div>
    )
}

export default Contact