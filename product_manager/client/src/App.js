import React from 'react';
import './App.css'
import { BrowserRouter, Switch, Route, Link } from "react-router-dom";
import Main from './views/Main';
import Detail from './views/Detail';
import Update from './views/Update';
import ProductForm from './components/ProductForm';


function App() {
  return (
    
    <BrowserRouter>
      <div className="App">
        <h1>Welcome to Product Manager</h1>
        <p>
          <Link to="/products">Add a Product</Link>
        </p>
        <Switch>
          <Route exact path="/products/">
            <Main />
          </Route>
        </Switch>
        <Switch>
          <Route exact path="/products/:id">
            <Detail />
          </Route>
        </Switch>
        <Switch>
          <Route exact path="/products/:id/:edit">
            <Update />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
      
    
  );
}
export default App;

