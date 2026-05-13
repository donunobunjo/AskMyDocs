import React, { useState } from "react";
import { uploadFile } from "./api";

function Upload({ onUploadSuccess }) {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        await uploadFile(file);
        onUploadSuccess();
    };

    return (
        <div>
            <h2>Upload Document</h2>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default Upload;