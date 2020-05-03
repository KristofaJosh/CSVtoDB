import React, {useEffect, useState} from 'react';
import './App.css';
import axios from 'axios';

function App() {
    const [fileUpload, setUpload] = useState({file: ''});
    const [messageStatus, setStatus] = useState({loading: false, message: ''});
    const [buttonStates, setButtonStates] = useState({loading: false, status: 'detach'});
    const [data, setData] = useState([]);

    useEffect(() => {
        setStatus({loading: true, message: 'Retrieving Data ...'});
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/all/',
        }).then((response) => {
            setData(response.data);
            if (response.data.length > 0) {
                setStatus({loading: false, message: 'Data Updated'});
            } else {
                setStatus({loading: false, message: 'No Data'});
            }
        }).catch((err) => {
            setStatus({loading: false, message: 'Error Occurred, Try again'});
        });

    }, [buttonStates]);

    const handleChange = (e) => {
        e.preventDefault();
        setUpload({file: e.target.files[0]})
    };

    const clearDB = (e) => {
        e.preventDefault();
        if (data.length > 0) {
            setData([]);
            setButtonStates({loading: false, status: 'detach'});

            axios({
                method: 'DELETE',
                url: 'http://127.0.0.1:8000/api/all/remove_data/',
            }).then((response) => {
                setStatus({loading: false, message: response.data.message});
            }).catch((err) => {
                setStatus({loading: false, message: 'Error Occurred, Try again'});
            });
        }
    };

    const submitForm = (e) => {
        e.preventDefault();
        if (fileUpload.file !== '') {
            setButtonStates({loading: true, status: 'detaching...'});
            setStatus({loading: true, message: 'uploading ...'});

            const formData = new FormData();
            formData.append('file', fileUpload.file);

            axios({
                method: 'PATCH',
                url: 'http://127.0.0.1:8000/api/all/translate_data/',
                data: formData,
            }).then((response) => {
                setButtonStates({loading: false, status: 'detached'});
                setStatus({loading: false, message: response.data.message});

            }).catch((err) => {
                setButtonStates({loading: false, status: 'detach'});
                setStatus({loading: false, message: err.response.data.message});
            });
        }
    };


    return (
        <div className={'App'}>
            <div className={'content'}>
                <div className="logo">
                    <img src="/assets/images/Zeno.jpg" alt=""/>
                    <p style={{fontWeight: 'bolder'}}>CSV TO DB SKILL ASSESSMENT</p>
                    <p>{messageStatus.message}</p>

                </div>
                <div className={'form'}>
                    <h3>Upload CSV</h3>

                    <span>
                        <input type="file" accept={'.csv'} onChange={handleChange}/>
                        <div>
                            <button type={'submit'} onClick={submitForm} disabled={buttonStates.loading}>
                                {buttonStates.loading ? buttonStates.status : buttonStates.status}
                            </button>
                            {data.length > 0 ? <button onClick={clearDB}>Clear DB</button> : null}
                        </div>
                    </span>
                </div>
                <div className={'csv'}>
                    <div className={'header'}><h2>CSV Data</h2></div>
                    <span className={'csv-head'}>
                        <div className={'card-info'}>
                            <span>ID</span>
                            <span>Temperature</span>
                            <span>Duration</span>
                            <span>TimeStamp</span>
                        </div>
                    </span>


                    {data.length === 0 ?
                        <div className="csvbody">
                            <p>{buttonStates.loading ? 'Loading ...' : 'No Data Found'}</p>
                        </div>

                        :
                        data && data.map((el, index) => (
                            <div key={index} className={'card'}>
                                <div key={index} className={'card-info'}>
                                    <span key={el.csv_id}>{el.csv_id}</span>
                                    <span key={el.csv_temperature}>{el.csv_temperature}</span>
                                    <span key={el.csv_duration}>{el.csv_duration}</span>
                                    <span key={el.csv_timestamp}>{el.csv_timestamp}</span>
                                </div>
                                {/*<button type={'submit'} onClick={submitForm}>edit</button>*/}
                            </div>
                        ))

                    }


                </div>
            </div>
        </div>
    );
}

export default App;
