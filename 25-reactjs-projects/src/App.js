/* import React from 'react'; */
import './App.css';
import Accordian from './components/Accordian';
import RandomColor from './components/random-color';

function App() {
  return (
    <div className="App">
      <header>
        <h1>25 React Projects for #100daysofMiva</h1>
      </header>
      <Accordian />
      <RandomColor />
    </div>
  );
}

export default App;