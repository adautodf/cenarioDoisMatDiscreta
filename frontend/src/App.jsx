import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState, useEffect } from 'react';

function App() {
  const [ reflexiva, setReflexiva ] = useState('');
  const [ simetrica, setSimetrica ] = useState('');
  const [ antissimetrica, setAntissimetrica ] = useState('');
  const [ assimetrica, setAssimetrica ] = useState('');
  const [ transitiva, setTransitiva ] = useState('');

  useEffect( () => {
    axios
      .get("http://localhost:7777/get_data")
      .then((response) => {
        const data = response.data
        setReflexiva(data['reflexiva'])
        setSimetrica(data['simetrica'])
        setAntissimetrica(data['antissimetrica'])
        setAssimetrica(data['assimetrica'])
        setTransitiva(data['transitiva'])
      })
      .catch( (e) => {
        //placeholder
      })
  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a>
          Trabalho de Natureza Discreta
        </a>
        <a>
          Equipe: Adauto, Alternandes, Victor e Luiz.
        </a>
        <p>
          Reflexividade: {reflexiva}
        </p>
        <a>
          Simetria: {simetrica}
        </a>
        <p>
          Assimetria: {assimetrica}
        </p>
        <a>
          Antissimetria: {antissimetrica}
        </a>
        <p>
          Transitividade: {transitiva}
        </p>

        <a
          className="App-link"
          href="https://github.com/adautodf/cenarioDoisMatDiscreta"
          target="_blank"
          rel="noopener noreferrer"
        >
          GitHub
        </a>
      </header>
    </div>
  );
}

export default App;
