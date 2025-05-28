import { Outlet } from "react-router-dom"
import AllUser from "./components/AllUser"
import Product from "./components/Product"

function App() {

  return (
    <>
     {/* <Product/> */}
     <Outlet/>    
    </>
  )
}

export default App
