import React from "react";
import axios from "axios";
import { Formik, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { Navigation } from "../../components/Navigation";
import { BACKEND_ADDRESS, FRONTEND_ADDRESS } from '../../constances';

const validationSchema = Yup.object().shape({
  className: Yup.string().required('Nazwa klasy jest wymagana')
});

export const CreateClass = () => {
  const submit = async (values, { setStatus }) => {
    const newClass = {
      name: values.className,
      user_id: localStorage.getItem('user_id') // Zakładamy, że user_id jest przechowywany w localStorage
    };

    try {
      // Utworzenie nowej klasy i przypisanie jej do zalogowanego nauczyciela
      const { data } = await 
        axios.post(BACKEND_ADDRESS+'/teacher/class/create',
        newClass, {
        headers:
          { 'Content-Type': 'application/json' },
        }, { withCredentials: true});

      if (!data) {
        console.log('Nie udało się stworzyć klasy');
        setStatus('Nie udało się stworzyć klasy');
        return;
      }

      // Przekierowanie do strony głównej nauczyciela
      window.location.href = FRONTEND_ADDRESS + '/teacher';
    } catch (error) {
      console.log(error);
      setStatus('Wystąpił Błąd. Spróbuj ponownie.');
      return;
    }
  }

  return (
    <div>
      <Navigation />
      <section className="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center">
        <div className="w-full max-w-md bg-white rounded-lg shadow dark:border dark:bg-gray-800 dark:border-gray-700 mt-[-100px]">
          <div className="p-6 space-y-4 sm:p-8">
            <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              Utwórz nową klasę
            </h1>
            <Formik
              initialValues={{
                className: ''
              }}
              validationSchema={validationSchema}
              onSubmit={submit}
            >
              {({ values, status, handleChange, handleBlur, handleSubmit, setStatus }) => (
                <form className="space-y-4 md:space-y-6" onSubmit={(e) => {
                  e.preventDefault();
                  handleSubmit();
                }}>
                  <div>
                    <label htmlFor="className" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nazwa klasy</label>
                    <input value={values.className} onChange={handleChange} onBlur={handleBlur} type="text" name="className" id="className" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                    <ErrorMessage name="className" component="div" className="text-red-600 text-sm" />
                  </div>
                  {!!status && <div className="text-red-600">{status}</div>}
                  <button type="submit" className="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Utwórz klasę</button>
                </form>
              )}
            </Formik>
          </div>
        </div>
      </section>
    </div>
  );
}
