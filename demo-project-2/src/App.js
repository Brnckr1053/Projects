import logo from './logo.svg';
import './App.css';

function App() {

  const changeText = (text) => {
    document.getElementById('old').getElementsByTagName('div')[0].innerHTML = text;
    document.getElementById('new-label').innerText = text;
  }

  return (
    <div className="App">
      <header className="App-header">
      <h3 id="new-label"></h3>
      <button onClick={() => changeText("next text")}>Send text to old!</button>
      </header>
    </div>
  );
}

export default App;
