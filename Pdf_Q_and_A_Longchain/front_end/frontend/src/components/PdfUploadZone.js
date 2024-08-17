import React, { useState } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';


const PdfUploadZone = () => {
    const [file, setFile] = useState(null);
    const [uploadMessage, setUploadMessage] = useState("");
    const [filename, setFileName] = useState("");
    const [filePresent, setFilePresent] = useState("");

    const onDrop = async (acceptedFiles) => {
      if (acceptedFiles.length === 0) {
        setUploadMessage("Please drop a valid PDF file.");
        return;
      }

      const file = acceptedFiles[0];
      setFile(file);
      setFilePresent(true);
      setFileName(file.name);
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: 'application/pdf',
        multiple: false,
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setUploadMessage("No file selected.");
        return;
        }

        const formData = new FormData();
        formData.append("file", file);
        console.log(formData);
        try {
            const response = await axios.post("http://localhost:8000/upload/", formData, {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            });
            setUploadMessage(`File uploaded successfully: ${response.data.filename}`);
          } catch (error) {
            setUploadMessage("Error uploading file. Please try again.");
          }
        setFilePresent(false);
        setFileName("");
    };

    return (
        <div>
            <div {...getRootProps({ className: 'dropzone' })}>
                <input {...getInputProps()} />
                {isDragActive ? (
                <p>Drop the PDF file here :) ...</p>
                ) : (
                <p>Drag and drop a PDF file here, or click here to select a file :) ...</p>
                )}
            </div>

            {filename &&
            <p className="file-name">File name: {filename}</p>}
            {filePresent &&
            <input
                type="submit"
                onClick={handleSubmit}
                className="submit"
            />
            }
            {uploadMessage && <p className="upload-message">{uploadMessage}</p>}
        </div>
    )
}

export default PdfUploadZone;
