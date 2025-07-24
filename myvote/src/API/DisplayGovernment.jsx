import axios from "axios";
import { refresh } from "./LoginApi";

const BASE_URL = 'http://127.0.0.1:8000/';
const GOVERNMENT_URL = BASE_URL + 'api/goverment/';

export const GetGovernment = async () => {
    try {
        const response = await axios.get(GOVERNMENT_URL, { withCredentials: true });
        return response;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            const refreshed = await refresh();
            if (refreshed) {
                try {
                    const retryResponse = await axios.get(GOVERNMENT_URL, { withCredentials: true });
                    return retryResponse;
                } catch (retryError) {
                    console.error("Retry failed:", retryError);
                    return null;
                }
            } else {
                console.warn("Token refresh failed");
                return null;
            }
        } else {
            console.error("Request failed:", error);
            return null;
        }
    }
};
