import {useEffect} from "react"
import axios from "axios";
export const Logout = () => {
    useEffect(() => {
       (async () => {
         try {
          console.log('logout')
           await axios.post('http://localhost:8000/logout',{
                 refresh_token:localStorage.getItem('refresh_token')
                 } ,{headers: {'Content-Type': 'application/json'}},  
                 {withCredentials: true});
            console.log('logout success')
           localStorage.clear();
           axios.defaults.headers.common['Authorization'] = null;
           window.location.href = '/login'
           } catch (e) {
             console.log('logout not working', e)
           }
         })();
    }, []);
    return (
       <div>Logging out...</div>
     )
}