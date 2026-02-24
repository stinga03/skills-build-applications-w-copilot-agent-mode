import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
// ...existing code...

function App() {
  return (
    <Router>
      <div>
        <header>
          <img src="/octofitapp-small.svg" alt="Octofit Tracker Logo" className="app-logo" />
          <h1 style={{margin: 0}}>Octofit Tracker</h1>
          <nav>
            <Link to="/activities">Activities</Link>
            <Link to="/leaderboard">Leaderboard</Link>
            <Link to="/teams">Teams</Link>
            <Link to="/users">Users</Link>
            <Link to="/workouts">Workouts</Link>
          </nav>
        </header>
        <div className="container mt-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={<h2>Welcome to Octofit Tracker!</h2>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
