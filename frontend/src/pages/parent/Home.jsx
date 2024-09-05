import {useEffect} from "react";
import axios from "axios";
import { Navigation } from "../../components/Navigation";
import {BACKEND_ADDRESS} from "../../constances";

export const Home = () => {
    //  const [message, setMessage] = useState('');
    //  const [classes, setClasses] = useState('');
     useEffect(() => {
        if(localStorage.getItem('access_token') === null){                   
            window.location.href = '/login'
        }
        else{
         (async () => {
           try {
             const {data} = await axios.get(   
                            BACKEND_ADDRESS + '/parent',
                           );
             console.log(data);
            //  setMessage(data.data);
            //  setClasses(data.classes);
          } catch (e) {
            console.log('not auth')
          }
         }
        )()
      };
     }, []);
     return (
      <div>
        <Navigation />
        <div className="form-signin mt-5 text-center">

          <h3>Witaj Rodzicu </h3>
          <p>Twoje dzieci:</p>
          <ul>

          </ul>
        </div>
      </div>
     )
}