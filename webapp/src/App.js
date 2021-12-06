import { useState, useEffect } from 'react';
import Search from './components/Search';
import ToggleButton from 'react-toggle-button'
import Loader from 'react-loader-spinner';

const App = () => {
    const [data, setData] = useState();
    const [algorithm, setAlgorithm] = useState(false);
    const [type, setType] = useState(false);
    const [fetched, setFetched] = useState(false);
    const [files, setFiles] = useState([null, null, null, null]);
    
    const recommendation_algorithms = ['naive_recommend', 'search_depth'];
    const recommendation_type = ['mainstream', 'niche'];

    let urls = ['data/naive_recommend_mainstream.json', 
                'data/naive_recommend_niche.json', 
                'data/search_depth_mainstream.json',
                'data/search_depth_niche.json'];

    const getAllData = async () => {
        const res = await Promise.all(urls.map(async url => {
          const resp = await fetch(url);
          return resp.json();
        }));
        console.log(res);
        setFiles(res);
        setFetched(true);
    }

    useEffect(() => {
        console.log('loading all data');
        getAllData();
    }, [])

    useEffect(() => {
        console.log('has fetched');
        setData(files[0]);
    }, [fetched])

    useEffect(() => {
        // console.log('algorithm: ', algorithm, 'type: ', type);
        const id = (algorithm ? 2 : 0) + (type ? 1 : 0)
        //console.log(id);
        setData(files[id])
    }, [algorithm, type])

    const displayAll = (fetched) => {
        if (fetched) {
            return (
                    <div className="main-container">
                        <div className="header">
                            <img src="/github-icon.png" alt="github-icon" />
                            <h1>REPOmmend</h1>
                        </div>
                    <div className='toggles'>
                        <div className="toggle algorithm">
                            <p style={{fontWeight: algorithm ? null : 'bold'}} className='left'>Naive Recommend</p>
                            <ToggleButton
                              inactiveLabel={''}
                              activeLabel={''}
                              value={algorithm}
                            colors={{
                                activeThumb: {
                                  base: 'rgb(250,250,250)',
                                },
                                inactiveThumb: {
                                  base: 'rgb(250,250,250)',
                                },
                                active: {
                                  base: 'rgb(65,66,68)',
                                },
                                inactive: {
                                  base: 'rgb(65,66,68)',
                                }
                              }}
                              onToggle={() => {
                                  setAlgorithm(!algorithm);
                              }} />
                              <p style={{fontWeight: algorithm ? 'bold' : null}} className='right'>Search Depth</p>
                        </div>
                        <div className="toggle type">
                            <p style={{fontWeight: type ? null : 'bold'}} className='left'>Mainstream</p>
                            <ToggleButton
                              inactiveLabel={''}
                              activeLabel={''}
                              value={type}
                            colors={{
                                activeThumb: {
                                  base: 'rgb(250,250,250)',
                                },
                                inactiveThumb: {
                                  base: 'rgb(250,250,250)',
                                },
                                active: {
                                  base: 'rgb(65,66,68)',
                                },
                                inactive: {
                                  base: 'rgb(65,66,68)',
                                }
                              }}
                              onToggle={() => {
                                  setType(!type);
                              }} />
                            <p style={{fontWeight: type ? 'bold': null}}className='right'>Niche</p>
                        </div>
                    </div>
                    <Search data={data} />
                    <p className="copyright">&copy; No Rights Reserved.</p>
                    </div>
                );
        } else {
            return (
                <div>
                    <Loader
                        type="ThreeDots"
                        color="#FF00FF"
                    />
                </div>);
        }
    }

return (
    displayAll(fetched));
};

export default App;
