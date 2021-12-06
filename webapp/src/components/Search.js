import React, { useState, useEffect } from 'react';
import Repo from './Repo';

const Search = ({ data }) => {
    const [search, setSearch] = useState('');
    const [res, setRes] = useState(null);
    const [hasRes, setHasRes] = useState(false);

    const randomRepo = (e) => {
        e.preventDefault();

        var keys = Object.keys(data);
        const random_repo = keys[(keys.length * Math.random()) << 0];

        setSearch(random_repo);
    };

    const handleSearch = () => {
        // e.preventDefault();
        if (search !== '') {
            if (search in data) {
                setRes(data[search]);
                setHasRes(true);
            } else {
                setRes(null);
                setHasRes(true);
            }
        }
    };

    const clearAll = () => {
        setHasRes(false);
        setRes(null);
        setSearch('');
    };

    const displayResults = (hasRes, res) => {
        if (hasRes) {
            if (res !== null) {
                return (
                    <div className="results">
                        {res.map((name, index) => {
                            if (index === res.length-1) {
                                return <Repo key={name} name={name} found={true} last={true}/>
                            } else {
                                return <Repo key={name} name={name} found={true} last={false}/>
                            }
                        })}
                    </div>
                );
            } else {
                return (
                    <div className="results">
                        <Repo found={false} />
                    </div>
                );
            }
        }
    };

    useEffect(() => {
        console.log('changed data');
        handleSearch();
        displayResults(hasRes, res);
    }, [data])


    return (
        <div className="Search">
            <form>
                <input
                    type="text"
                    placeholder="Enter a GitHub repository you like"
                    name="s"
                    autoComplete="off"
                    autoFocus
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                />
                <div className="buttons">
                    <button type="submit" onClick={(e) => {
                        e.preventDefault();
                        handleSearch()}}>
                        Search
                    </button>
                    <button
                        onClick={(e) => {
                            e.preventDefault();
                            clearAll();
                        }}
                    >
                        Clear
                    </button>
                    <button onClick={(e) => randomRepo(e)}>Random Repo</button>
                </div>
            </form>
            <div className="search-container">
                {displayResults(hasRes, res)}
            </div>
        </div>
    );
};

export default Search;
