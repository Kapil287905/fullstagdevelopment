import { Children, StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle.js"

import { createBrowserRouter,RouterProvider } from 'react-router-dom'
import ProductDetails from './components/ProductDetails.jsx';
import Product from './components/Product.jsx';
import SignUP from './components/SignUP.jsx';
import SignIN from './components/SignIN.jsx';

let routes=createBrowserRouter([
  {
    path:'/',
    element:<App/>,
    children:[
      {path:'',element:<Product/>},
      {path:'/productdetails/:id',element:<ProductDetails/>},
      {path:'/signup',element:<SignUP/>},
      {path:'/signin',element:<SignIN/>}
    ]
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={routes}>
    <App />
    </RouterProvider>
  </StrictMode>,
)
