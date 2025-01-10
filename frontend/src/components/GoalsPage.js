import React, { useEffect, useState } from 'react';
import axios from 'axios';

const GoalsPage = () => {
    const [goals, setGoals] = useState([]);
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/goals/')
            .then(response => setGoals(response.data))
            .catch(error => console.error(error));
    }, []);
    
    return (
        <div>
            <h1>Goals</h1>
            <ul>
                {goals.map(goal => (
                    <li key={goal.id}>{goal.title}: {goal.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default GoalsPage;
