import React from 'react';
import logo from './logo.svg';
import './App.css';
import TopGrossMovies from './components/TopGrossMovies';
import TopVotedMovies from './components/TopVotedMovies';
import TopRatedMovies from './components/TopRatedMovies';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <main>
        <div className="chart-container">
          <TopGrossMovies year={2021} />
        </div>
        <div className="chart-container">
          <TopVotedMovies />
        </div>
        <div className="chart-container">
          <TopRatedMovies year={2021} />
        </div>
      </main>
    </div>
  );
}

export default App;
