import React, { useState } from "react";
import { LoginApi } from "../API/LoginApi";
import { useNavigate } from 'react-router-dom';

const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const nav = useNavigate();

    const handleSubmit = async () => {
        const res = await LoginApi(username, password)
        if (res !== null) {
            alert('welcome');
            nav('/profile')
        } else {
            console.log("user was not found.");
        }
    }


    return (
        <div className="login-container">
            <div className="username">
                <label htmlFor="username">username</label><input id="username" name="username" type="text" value={username} onChange={(e) => {setUsername(e.target.value)}} />
            </div>
            <div className="password">
                <label htmlFor="password">password</label><input id="password" name="password" type="password" value={password} onChange={(e) => {setPassword(e.target.value)}}/>
            </div>
            <button onClick={handleSubmit}>Login</button>
        </div>
    )
}

export default Login;