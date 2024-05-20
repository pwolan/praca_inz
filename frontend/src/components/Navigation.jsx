import React, { useState, useEffect} from 'react';
import { Link } from 'react-router-dom';

export function Navigation() {
   const [isAuth, setIsAuth] = useState(false);
   useEffect(() => {
     if (localStorage.getItem('access_token') !== null) {
        setIsAuth(true); 
      }
    }, [isAuth]);
     return ( 
      <div>
        <div >           
          <div className="me-auto"> 
            {isAuth ? <Link to="/teacher">Home</Link> : null}
          </div>
          <div>
            {isAuth ? <Link to="/teacher/logout">Logout</Link> :  
                    <Link to="/teacher/login">Login</Link>}
          </div>
        </div>
       </div>
     );
}