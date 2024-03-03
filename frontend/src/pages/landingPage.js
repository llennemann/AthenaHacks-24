import {Link } from "react-router-dom";

export default function LandingPage () {
    return (
        <>
            <h1>this is your</h1>
            <h1>finance buddy</h1>
            <Link to="/try-me">
                <button>try me!</button>
            </Link>
            <Link to="/financial-basics">
                <button>Finance Basics</button>
            </Link>
            <Link to="/about-me">
                <button>About Me</button>
            </Link>

        </>
    );
};