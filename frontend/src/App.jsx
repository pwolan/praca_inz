import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login as TeacherLogin } from './pages/teacher/Login';
import { Logout as TeacherLogout } from './pages/teacher/Logout';
import { Login } from './pages/Login';
import { Root } from "./pages/Root";
import { Home } from "./pages/teacher/Home";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/teacher",
    element: <Home />,
  },
  {
    path: "/teacher/login",
    element: <TeacherLogin />,
  },
  {
    path: "/teacher/logout",
    element: <TeacherLogout />,
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
