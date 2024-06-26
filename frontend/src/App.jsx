import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login as TeacherLogin } from './pages/teacher/Login';
import { Logout as TeacherLogout } from './pages/teacher/Logout';
import { Login } from './pages/Login';
import { Root } from "./pages/Root";
import { Home } from "./pages/teacher/Home";
import { Class } from "./pages/teacher/Class";
import { CreateClass } from "./pages/teacher/CreateClass";
import { CreateChild } from "./pages/teacher/CreateChild";

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
  {
    path: "/teacher/class/:id",
    element: <Class />
  },
  {
    path: "/teacher/create-class",
    element: <CreateClass />
  },
  {
    path: "/teacher/class/:id/create",
    element: <CreateChild />
  }
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
