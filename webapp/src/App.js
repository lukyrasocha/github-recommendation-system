import { useState, useEffect } from 'react';
import Search from './components/Search';

const App = () => {
    const [recommend, setRecommend] = useState();

    const getData = async () => {
        const res = await fetch('/data/test.json');
        const data = await res.json();
        setRecommend(data);
    };

    useEffect(() => {
        getData();
    }, []);

    return (
        <div className="main-container">
            <div className="header">
                <img src="/github-icon.png" alt="github-icon" />
                <h1>REPOmmend</h1>
            </div>
            <Search recommend={recommend} />
            <p className="copyright">&copy; No Rights Reserved.</p>
        </div>
    );
};

export default App;
