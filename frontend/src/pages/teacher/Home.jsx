import {useEffect, useState} from "react";
import axios from "axios";
import { Navigation } from "../../components/Navigation";
import {BACKEND_ADDRESS, FRONTEND_ADDRESS} from "../../constances";

export const Home = () => {
     const [name, setName] = useState('');
     const [classes, setClasses] = useState('');
     useEffect(() => {
        if(localStorage.getItem('access_token') === null){                   
            window.location.href = '/login'
        }
        else{
         (async () => {
           try {
             const {data} = await axios.get(   
                            BACKEND_ADDRESS + '/teacher',
                           );
             console.log(data);
             setName(data.name);
             setClasses(data.classes);
          } catch (e) {
            console.log('not auth')
          }
         }
        )()
      };
     }, []);

     const handleCreateClass = () => {
      // Logika do tworzenia nowej klasy
      // Można przekierować użytkownika do formularza tworzenia nowej klasy
      window.location.href = `${FRONTEND_ADDRESS}/teacher/create-class`;
    };

    return (
      <div>
        <Navigation />
        <div className="min-h-screen bg-gray-100">
          <div className="flex flex-col items-center justify-center mt-10">
            <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md">
              <h3 className="text-2xl font-semibold mb-4">Witaj, {name}!</h3>
              <p className="text-lg mb-4">Twoje klasy:</p>
              <ul className="list-disc list-inside space-y-2 mb-4">
                {Object.entries(classes).map(([id, el]) => (
                  <li key={id} className="flex justify-between items-center">
                    <span>{el}</span>
                    <button className="ml-4 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
                      <a href={FRONTEND_ADDRESS + '/teacher/class/' + id}>Modyfikuj</a>
                    </button>
                  </li>
                ))}
              </ul>
              <button onClick={handleCreateClass} className="w-full bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
                Utwórz nową klasę
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }