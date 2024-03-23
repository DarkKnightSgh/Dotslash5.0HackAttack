import React, { useState } from 'react';
import './gui.css';

const FileUploadComponent = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [audioSrc, setAudioSrc] = useState('');
    const [caption, setCaption] = useState('');

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
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

            const jsonData = await response.json();
            console.log(jsonData);

            // Update audio source and caption with the response data
            setAudioSrc(jsonData.audio_file);
            setCaption(jsonData.caption);
        } catch (error) {
            console.log('Error', error);
        }
    };

    return (
        <div className="file-upload-container">
            <input type="file" onChange={handleFileChange} className="file-input" />
            <button onClick={handleConvert} className="convert-button">Convert picture</button>
            {audioSrc && (
                <div className="audio-container">
                    <audio controls>
                        <source src={audioSrc} type="audio/mpeg" />
                        Your browser does not support the audio element.
                    </audio>
                    <p>{caption}</p>
                </div>
            )}
        </div>
    );
};

export default FileUploadComponent;
