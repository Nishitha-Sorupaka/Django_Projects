import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const TopGrossMovies = ({ year }) => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        axios.get(`/top-gross-movies/${year}/`)
            .then(response => {
                setMovies(response.data.movies);
            })
            .catch(error => {
                console.error('Error fetching top gross movies:', error);
            });
    }, [year]);

    // Prepare data for Chart.js
    const chartData = {
        labels: movies.map(movie => movie.MOVIES),
        datasets: [
            {
                label: 'Gross',
                backgroundColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 1,
                data: movies.map(movie => movie.Gross)
            }
        ]
    };

    return (
        <div>
            <h2>Top Gross Movies of {year}</h2>
            <Bar
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

export default TopGrossMovies;
