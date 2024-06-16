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
    <div className="min-h-screen bg-gray-100">
      <Navigation />
      <div className="flex flex-col items-center justify-center mt-10">
        {classData && (
          <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-3xl">
            <h1 className="text-3xl font-bold mb-4">ID klasy: {classData.id}</h1>
            <h2 className="text-2xl font-semibold mb-4">Nazwa klasy: {classData.class_name}</h2>
            <div>
              <h3 className="text-xl font-semibold mb-2">Lista dzieci:</h3>
              <ul className="list-disc list-inside space-y-2">
                {Object.entries(children).map(([id, child]) => (
                  <li key={id} className="flex justify-between items-center">
                    <span>{id}. {child.name} {child.surname}</span>
                    <Link to={`${FRONTEND_ADDRESS}/child/edit/${child.id}`} className="ml-4 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
                      Edytuj
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
            <div className="mt-6 space-y-4">
              <button onClick={handleAddChild} className="w-full bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
                Dodaj dziecko
              </button>
              <button onClick={handleImportClass} className="w-full bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">
                Importuj listę dzieci
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}