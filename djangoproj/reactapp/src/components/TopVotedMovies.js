import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const TopVotedMovies = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        axios.get('/top-voted-movies/')
            .then(response => {
                setMovies(response.data.movies);
            })
            .catch(error => {
                console.error('Error fetching top voted movies:', error);
            });
    }, []);

    // Prepare data for Chart.js
    const chartData = {
        labels: movies.map(movie => movie.title),
        datasets: [
            {
                label: 'Votes',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                borderWidth: 1,
                data: movies.map(movie => movie.votes)
            }
        ]
    };

    return (
        <div>
            <h2>Top Voted Movies</h2>
            <Line
                data={chartData}
                options={{
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }}
            />
        </div>
    );
};

export default TopVotedMovies;
