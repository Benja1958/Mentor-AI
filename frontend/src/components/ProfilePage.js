import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProfilePage = () => {
    const [profile, setProfile] = useState({});
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/profiles/')
            .then(response => setProfile(response.data[0]))  // Assuming first profile in the response
            .catch(error => console.error(error));
    }, []);
    
    return (
        <div>
            <h1>{profile.name}</h1>
            <p>{profile.school}</p>
            <p>{profile.career_goals}</p>
        </div>
    );
};

export default ProfilePage;
