import React, { useState } from 'react';
import Repo from './Repo';

const Search = ({ recommend }) => {
    const [search, setSearch] = useState('');
    const [res, setRes] = useState(null);
    const [hasRes, setHasRes] = useState(false);

    const handleSearch = (e) => {
        e.preventDefault();

        if (search in recommend) {
            // search key exist in our recommend map
            setRes(recommend[search]);
            setHasRes(true);
            // assign response; array of recommend objects (with metadata)
        } else {
            setRes(null);
            setHasRes(true);
        }
        setSearch('');
    };

    const displayResults = (hasRes, res) => {
        if (hasRes) {
            if (res !== null) {
                return (
                    <div className="results">
                        {res.map((el, index) => {
                            return (
                                <Repo
                                    key={index}
                                    name={el.repo_name}
                                    created={el.creation_date}
                                    found={true}
                                />
                            );
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
                <div className="bouttons">
                    <button type="submit" onClick={(e) => handleSearch(e)}>
                        Search
                    </button>
                    <button
                        onClick={(e) => {
                            e.preventDefault();
                            setHasRes(false);
                            setRes([]);
                        }}
                    >
                        Clear
                    </button>
                </div>
            </form>
            {displayResults(hasRes, res)}
        </div>
    );
};

export default Search;
