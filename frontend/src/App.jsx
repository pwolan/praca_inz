import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login as TeacherLogin } from './pages/teacher/Login';
import { Logout } from './pages/Logout';
import { Login } from './pages/Login';
import { Login as ParentLogin } from "./pages/parent/Login";
import { Root } from "./pages/Root";
import { Home } from "./pages/teacher/Home";
import { Class } from "./pages/teacher/Class";
import { CreateClass } from "./pages/teacher/CreateClass";
import { Home as ParentHome } from "./pages/parent/Home";

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
    path: "/logout",
    element: <Logout />
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
    path: "/teacher/class/:id",
    element: <Class />
  },
  {
    path: "/teacher/create-class",
    element: <CreateClass />
  },
  {
    path: "/parent/login",
    element: <ParentLogin />
  },
  {
    path: "/parent",
    element: <ParentHome />
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
