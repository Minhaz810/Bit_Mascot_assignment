import React from "react"
import {createBrowserRouter} from 'react-router-dom'
import HomePage from "./pages/HomePage"
import LoginPage from "./pages/Login"
import AdminPage from "./pages/Admin"
import PrivateRoute from "./components/PrivateRoute"
import PrivateRoute2 from "./components/PrivateRoute2"

const router = createBrowserRouter([
    {
        path : "/",
        element : (
        <PrivateRoute2>
        <HomePage/>
        </PrivateRoute2>
        )
    },
    {
        path : "/login",
        element : (
            <PrivateRoute2>
                <LoginPage/>
            </PrivateRoute2>
            )
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