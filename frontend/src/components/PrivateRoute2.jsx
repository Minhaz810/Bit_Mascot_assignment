import React from 'react';
import { Navigate } from 'react-router-dom';

function PrivateRoute2({ children }) {
  const token = localStorage.getItem('userToken');

  return token ? <Navigate to="/admin"/>:children;
}

export default PrivateRoute2;