import { useState, useEffect } from 'react';
import Search from './components/Search';

const App = () => {
    const [data, setData] = useState();

    const getData = async () => {
        const res = await fetch('/data/naive_recommend.json');
        const res_json = await res.json();
        setData(res_json);
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
            <Search data={data} />
            <p className="copyright">&copy; No Rights Reserved.</p>
        </div>
    );
};

export default App;
