import React, { useState } from "react";
import Upload from "./Upload";
import Chat from "./Chat";

function App() {
    const [ready, setReady] = useState(false);

    return (
        <div>
            <h1>RAG Q&A App</h1>
            {!ready ? (
                <Upload onUploadSuccess={() => setReady(true)} />
            ) : (
                <Chat />
            )}
        </div>
    );
}

export default App;