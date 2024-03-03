import {Link } from "react-router-dom";
import "./landingPage.css"
import Girl from '../images/DALL_E_2024-03-02_16.30.png';

export default function LandingPage () {
    return (
        <>
            <div class="background-rectangle"></div>
            <div class="small-title-text">this is your</div>
            <div class="big-title-text">finance buddy</div>
            <Link to="/try-me">
                <button class="try-me-button">✨try me!✨</button>
            </Link>
            <Link to="/financial-basics">
                <button class="finance-basics-button">Finance Basics</button>
            </Link>
            <Link to="/about-me">
                <button class="about-me-button">About Me</button>
            </Link>
            <div class="blue-circle"></div>
            <img class="girl" src={Girl}/>

        </>
    );
};