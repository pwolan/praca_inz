import {useEffect, useState} from "react";
import axios from "axios";
import { Navigation } from "../../components/Navigation";

export const Home = () => {
     const [message, setMessage] = useState('');
     const classes = ['a', 'b', 'c', 'd']
     useEffect(() => {
        // if(localStorage.getItem('access_token') === null){                   
        //     window.location.href = '/login'
        // }
        // else{
         (async () => {
           try {
             const {data} = await axios.get(   
                            'http://localhost:8000/teacher', {
                             headers: {
                                'Content-Type': 'application/json'
                             }}
                           );
             console.log(data);
             setMessage(data.data);
          } catch (e) {
            console.log('not auth')
          }
         }
        )()
      // };
     }, []);
     return (
      <div>
        <Navigation />
        <div className="form-signin mt-5 text-center">

          <h3>Witaj: {message}</h3>
          <p>Your classes:</p>
          <ul>
          {classes.map((el) => (
            <li>{el}: <button><a href=""></a></button></li>
          ))}
          </ul>
        </div>
      </div>
     )
}