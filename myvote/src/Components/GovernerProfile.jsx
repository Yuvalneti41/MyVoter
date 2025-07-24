import { useState, useEffect } from "react";
import { fetchGovernerProfile } from "../API/GovernerProfile";

const BASE_URL = 'http://127.0.0.1:8000/';

const GovernerProfile = ({ governerId }) => {
    const [governerProfile, setGovernerProfile] = useState({
        first_name: "",
        last_name: "",
        profile_picture: ""
    });
    const [error, setError] = useState(null);

    useEffect(() => {
        const getProfile = async () => {
            try {
                console.log("Fetching profile for ID:", governerId);
                const res = await fetchGovernerProfile(governerId);
                if (res && res.data) {
                    console.log("Profile data:", res.data);
                    setGovernerProfile(res.data);
                    setError(null);
                } else {
                    throw new Error("No data in response");
                }
            } catch (e) {
                console.error("Error fetching profile:", e);
                setError("Failed to load profile.");
            }
        }
        if (governerId) getProfile();
    }, [governerId]);

    if (error) return <p>{error}</p>;

    return (
        <div className="governer-profile-container">
            {governerProfile.profile_picture ? (
                <img src={BASE_URL + governerProfile.profile_picture} alt="profile" />
            ) : (
                <p>No picture</p>
            )}
            <p>{governerProfile.first_name} {governerProfile.last_name}</p>
        </div>
    );
};

export default GovernerProfile;
