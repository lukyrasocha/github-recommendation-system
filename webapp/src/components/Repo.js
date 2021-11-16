import React from 'react';
import { unstable_concurrentAct } from 'react-dom/test-utils';

const Repo = ({ name, created, languages, found }) => {
    return (
        <div>
            {found ? (
                <a
                    href={'https://www.github.com/'.concat(name)}
                    target="_blank"
                >
                    <div className="Repo">
                        <h3 className="repo_name">{name}</h3>
                        <p className="created">{created}</p>
                        <p className="languages">{languages}</p>
                    </div>
                </a>
            ) : (
                <div className="Repo">
                    <h3 className="repo_name">Could not find.</h3>
                </div>
            )}
        </div>
    );
};

export default Repo;
