import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/landingPage.js';
import AboutMe from './pages/aboutMe.js';
import TryMe from './pages/tryMe.js';
// about me, finance basics (buttons for pop ups maybe), try me (with quiz and then game (shows stock and then click yes or no
// and then click how much))

export default function Square() {
  return (
    <div>
      <Router>
          <Routes>
            <Route exact path="/" element={<LandingPage/>} />
            <Route path="/about-me" element={<AboutMe/>} />
            <Route path="/try-me" element={<TryMe/>} />
          </Routes>
      </Router>
    </div>
  );
}