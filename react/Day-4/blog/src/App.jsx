import './App.css'
import BookImg from "./book2.png"
import Contact from './components/contact';

function App() {
  const title="10 tips for Effective Time Management";
  const author="Jhon Due";
  const description="Best Seller of Year";
  const image=BookImg

  const contacts=[
    {
        name:"Alice",
        email:"a@gmail.com",
        phone:23334,
        address:"kandivali"
    },
    {
        name:"Bob",
        email:"b@gmail.com",
        phone:676969,
        address:"malad"
    },
    {
        name:"John",
        email:"aj@gmail.com",
        phone:12239,
        address:"dadar"
    }
]

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

  const authorstyle={
    fontSize:"16px",
    fontStyle:"italic",
    color:"#777",
    marginBottom:"10px"
  }

  const descriptionstyle={
    fontSize:"14px",
    color:"#555",
    marginBottom:"10px"
  }

  return (
    <>
      <div className='bolog-container' style={containerStyle}>
        <img src={image} alt="book1" className='bolog-image' />
        <h2 style={titlestyle}>{title}</h2>
        <p style={authorstyle}>By {author}</p>
        <p style={descriptionstyle}>{description}</p>
      </div>
      <div>
        <h1>Contact List</h1>
        <div>
          {
            contacts.map((c,index)=>
              <Contact 
              key={index}
              name={c.name}
              email={c.email}
              phone={c.phone}
              address={c.address}
              
              />
            
            )
          }
        </div>
      </div>
    </>
  )
}

export default App
