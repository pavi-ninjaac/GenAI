// import React, { useState } from "react";
import React from "react";

import PageLayout from "./PageLayout";
// import axios from "axios";

// function App() {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     if (!file) {
//       setMessage("No file selected.");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);
//     // setMessage("Error uploading file");

//     try {
//       const response = await axios.post("http://localhost:8000/upload/", formData, {
//         headers: {
//           "Content-Type": "multipart/form-data",
//         },
//       });
//       setMessage(`File uploaded successfully: ${response.data.filename}`);
//     } catch (error) {
//       setMessage(error.message);
//     }
//   };

//   return (
//     <div className="App">
//       <h1>Upload PDF</h1>
//       <form onSubmit={handleSubmit}>
//         <input type="file" onChange={handleFileChange} accept="application/pdf" />
//         <button type="submit">Upload</button>
//       </form>
//       <p>{message}</p>
//     </div>
//   );
// }

function App() {
  return (
      <PageLayout />
  );
}

export default App;
