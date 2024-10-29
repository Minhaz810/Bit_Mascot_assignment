import React from "react"
import {createBrowserRouter} from 'react-router-dom'
import HomePage from "./pages/HomePage"
import LoginPage from "./pages/Login"
import AdminPage from "./pages/Admin"
import PrivateRoute from "./components/PrivateRoute"

const router = createBrowserRouter([
    {
        path : "/",
        element : <HomePage/>
    },
    {
        path : "/login",
        element : <LoginPage/>
    },
    {
        path : "/admin",
        element : (
        <PrivateRoute>
            <AdminPage/>
        </PrivateRoute>
        )
    },
])

export default router