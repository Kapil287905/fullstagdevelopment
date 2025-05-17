import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Car from './Car';
//import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Car />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();

// import React from "react";
// import ReactDom from "react-dom/client"

// const root2 = ReactDom.createRoot(document.getElementById('root2'))
// const render=()=>{
//   document.getElementById('root1').innerHTML=`<div><h1>Root2</h1><input><pre>${new Date().toLocaleTimeString()}</pre></div>`
//   root2.render(<div><h1>Root2</h1><input></input><pre>{new Date().toLocaleTimeString()}</pre></div>)
// }
// setInterval(render,1000)
