import { Link } from "react-router-dom";
import { Navigation } from "../components/Navigation";

export const Root = () => {

    return (
        <div>
            <Navigation />
            <h1>Root</h1>
            <Link to={'/login'}>Login Page</Link>
        </div>
    );
}