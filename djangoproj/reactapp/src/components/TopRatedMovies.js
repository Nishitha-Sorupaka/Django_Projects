import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const TopRatedMovies = ({ year }) => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        axios.get(`/top-rated-movies/${year}/`)
            .then(response => {
                setMovies(response.data.movies);
            })
            .catch(error => {
                console.error('Error fetching top rated movies:', error);
            });
    }, [year]);

    // Prepare data for Chart.js
    const chartData = {
        labels: movies.map(movie => movie.title),
        datasets: [
            {
                label: 'Rating',
                backgroundColor: 'rgba(255,99,132,0.2)',
                borderColor: 'rgba(255,99,132,1)',
                borderWidth: 1,
                data: movies.map(movie => movie.rating)
            }
        ]
    };

    return (
        <div>
            <h2>Top Rated Movies of {year}</h2>
            <Bar
                data={chartData}
                options={{
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 10 // Assuming ratings are on a scale of 0-10
                        }
                    }
                }}
            />
        </div>
    );
};

export default TopRatedMovies;
