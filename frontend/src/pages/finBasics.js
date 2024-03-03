import "./finBasics.css";
import { Link } from 'react-router-dom';

export default function FinBasics () {
    return (
        <>
            <h1>finance is a broad field.</h1>
            <h3>Click here to learn more about the...</h3>

            <Link to="/financial-basics/stock-market">
                <button>what is the stock market?</button>
            </Link>
            <Link to="/financial-basics/securities">
                <button>difference between bonds/funds/stocks?</button>
            </Link>
            <Link to="/financial-basics/portfolio">
                <button>how to diversify your portfolio</button>
            </Link>
        </>
    );
};