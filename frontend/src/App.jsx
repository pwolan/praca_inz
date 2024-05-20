import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login as TeacherLogin } from './pages/teacher/Login';
import { Login } from './pages/Login';
import { Root } from "./pages/Root";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />
  },
  {
    path: "/login",
    element: <Login/>,
  },
  {
    path: "/teacher/login",
    element: <TeacherLogin />,
  },
]);

function App() {

  // useEffect(() => {
  //   fetch('http://localhost:8000/teacher/')
  //     .then(res => res.json())
  //     .then(data => setData(data.data));
  // })

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
