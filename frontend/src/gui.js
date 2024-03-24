import React, { useState, useEffect } from 'react';
import './gui.css';

const FileUploadComponent = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploadedImage, setUploadedImage] = useState('');
    const [caption, setCaption] = useState('');

    useEffect(() => {
        fetch('/caption.txt')
            .then(response => response.text())
            .then(text => setCaption(text))
            .catch(error => console.error('Error fetching caption:', error));
    }, []);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
        setUploadedImage(URL.createObjectURL(event.target.files[0]));
    };

    const handleConvert = async () => {
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

            if (response.ok) {
                const data = await response.json();
                if (data.caption) {
                    setCaption(data.caption);
                } else {
                    console.log('Caption not found in response');
                }
            } else {
                console.log('Error:', response.statusText);
            }

        } catch (error) {
            console.log('Error', error);
        }

        try {
            const captionResponse = await fetch("http://127.0.0.1:5000/caption", {
                method: 'GET'
            });

            if (!captionResponse.ok) {
                throw new Error('Failed to fetch caption');
            }

            const captionText = await captionResponse.text();
            setCaption(captionText);
            console.log(captionText);
        } catch (error) {
            console.error('Error fetching caption:', error);
        }
    };

    return (
        <div className="container">
            <div className="file-upload-container">
                <input type="file" onChange={handleFileChange} className="file-input" />
                <button onClick={handleConvert} className="convert-button">Convert picture</button>
            </div>
            {uploadedImage && (
                <div className="file-upload-container">
                    <img src={uploadedImage} alt="Uploaded" className="uploaded-image" />
                </div>
            )}
            {caption && (
                <div className="file-upload-container">
                    <h3>Caption:</h3>
                    <p>{caption}</p>
                </div>
            )}
        </div>
    );
};

export default FileUploadComponent;
