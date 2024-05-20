import React from "react";
import { Link } from "react-router-dom";

export const Login = () => {

    return (
        <div>
            <div>
                <Link className="p-4" to={'/teacher/login'}>Teacher Login Page</Link>
                <Link className="p-4" to={'/parent/login'}>Parent Login Page</Link>
            </div>
        </div>
    );
}