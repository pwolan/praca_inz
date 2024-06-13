import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { Navigation } from "../../components/Navigation";
import { useParams } from 'react-router-dom';

export const Class = () => {
  let {id} = useParams();
  const [classData, setClassData] = useState('');

  useEffect(() => {
    const fetchData = async () => {
        try {
          const response = await axios.get(`http://localhost:8000/teacher/class/${id}`, {
            headers: {
               'Content-Type': 'application/json'
            }});
            console.log(response)
          setClassData(response.data);
        } catch (error) {
          console.error('Error:', error);
        }
      };
  
      fetchData();
  }, [id]);

  return (
    <div>
    <div>
    <div> <Navigation /></div>
      {
        <div>
          <h1>ID klasy: {classData.id}</h1>
          {/* Renderuj więcej danych o klasie tutaj */}
        </div>
      }
    </div>
    </div>
  );
}
