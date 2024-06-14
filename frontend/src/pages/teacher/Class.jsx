import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { Navigation } from "../../components/Navigation";
import { useParams, Link } from 'react-router-dom';
import {BACKEND_ADDRESS, FRONTEND_ADDRESS} from '../../constances';

export const Class = () => {
  let {id} = useParams();
  const [classData, setClassData] = useState('');
  const [children, setChildren] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(BACKEND_ADDRESS + `/teacher/class/${id}`);
        setClassData(response.data);
        setChildren(response.data.children);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchData();
  }, [id]);

  const handleAddChild = () => {
    // Logika do dodania nowego dziecka
    // Formularz można zrobić za pomocą Formik -> Patrz Login.jsx
  };

  const handleImportClass = () => {
    // Logika do importu listy dzieci z pliku
  };

  return (
    <div>
      <Navigation />
      <div>
        {classData && (
          <div>
            <h1>ID klasy: {classData.id}</h1>
            <h2>Nazwa klasy: {classData.class_name}</h2>
            <div>
              <h3>Lista dzieci:</h3>
              <ul>
                {Object.entries(children).map(([id, child]) => (
                  <li key={id}>
                    {id} {child.name} {child.surname}
                    <Link to={`${FRONTEND_ADDRESS}/child/edit/${child.id}`}>Edytuj</Link>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <button onClick={handleAddChild}>Dodaj dziecko</button>
              <br></br>
              <button onClick={handleImportClass}>Importuj listę dzieci</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
