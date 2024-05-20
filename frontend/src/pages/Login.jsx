import React from "react";
import { Link } from "react-router-dom";
import { Navigation } from "../components/Navigation";

export const Login = () => {

    return (
        <div>
            <Navigation />
            <div>
                <Link className="p-4" to={'/teacher/login'}>Teacher Login Page</Link>
                <Link className="p-4" to={'/parent/login'}>Parent Login Page</Link>
            </div>
        </div>
    );
}