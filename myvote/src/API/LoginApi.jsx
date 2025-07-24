import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/';
const LOGIN_URL =   BASE_URL + 'api/token/';
const REFRESH_URL = BASE_URL + 'api/token/refresh/'

export const LoginApi = async (username, password) => {
    const response = await axios.post(LOGIN_URL, {
        username: username,
        password: password
    },
        { withCredentials: true }
    ).catch((error) => console.error(error));
    if (response.data.success) {
        return response;
    } else {
        return null;
    }
}

export const refresh = async() => {
    try {
        const response = await axios.post(REFRESH_URL, {}, {
            withCredentials: true
        });
        console.log(response);
        return true;
    } catch(error) {
        return false;
    }
}