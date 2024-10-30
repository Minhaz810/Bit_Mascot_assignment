import React, { useState } from 'react';
import SignIn from '../api/auth';
import { useNavigate } from 'react-router-dom';
import Loader from '../components/Loader';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading,setLoading] = useState(false)
  const navigate = useNavigate()

  const handleLogin = async () => {
    setLoading(true)
    const result = await SignIn(username,password)
    if (result["status"] === "success"){
        localStorage.setItem("userToken",JSON.stringify(result.data))
        navigate("/admin")
        setLoading(false)
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white shadow-md rounded">
        <h2 className="mb-6 text-2xl font-bold text-center text-gray-700">Login as Admin</h2>
        <div className="mb-4">
          <label className="block text-gray-600 mb-2" htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
        </div>
        <div className="mb-6">
          <label className="block text-gray-600 mb-2" htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
        </div>
        <button
          onClick={handleLogin}
          className="w-full py-2 px-4 bg-blue-950 hover:bg-blue-800 text-white font-semibold rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
          {loading?(<div className="flex justify-center">
            <Loader/>
          </div>):
          (<span>Login</span>)}
        </button>
      </div>
    </div>
  );
}

export default LoginPage;
