import React, { useState, useEffect } from 'react';
import './gui.css';

const FileUploadComponent = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [data, setData] = useState({});

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleConvert = async () => {
        // Implement file upload logic here
        if (!selectedFile) {
            console.log('No file selected.');
            return;
        }

        try {
            const formData = new FormData();
            formData.append('image', selectedFile);

            const response = await fetch("http://127.0.0.1:5000/upload", {
                method: 'POST',
                body: formData
            });

            const jsonData = await response.json();
            setData(jsonData);
        } catch (error) {
            console.log('Error', error);
        }

        console.log('Converting file:', selectedFile);
    };

    return (
        <div className="file-upload-container">
            <input type="file" onChange={handleFileChange} className="file-input" />
            <button onClick={handleConvert} className="convert-button">Convert picture</button>
        </div>
    );
};

export default FileUploadComponent;
