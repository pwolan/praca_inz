import { Link } from "react-router-dom";

export const Root = () => {

    return (
        <div>
        <h1>Root</h1>
        <Link to={'/login'}>Login Page</Link>
        </div>
    );
}