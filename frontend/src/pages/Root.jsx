import { Link } from "react-router-dom";
import { Navigation } from "../components/Navigation";

export const Root = () => {
    return (
        <div>
            <Navigation />
            <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center">
                <div className="max-w-lg w-full bg-white p-8 shadow-md rounded-lg mt-[-100px]">
                    <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome to Root Page</h1>
                    <p className="text-gray-600 mb-4">This is the root page of your application.</p>
                    <Link to={'/login'} className="text-blue-600 hover:underline">Go to Login Page</Link>
                </div>
            </div>
        </div>
    );
}
