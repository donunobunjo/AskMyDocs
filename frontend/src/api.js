const API_URL = "http://localhost:8000";

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${API_URL}/upload/`, {
        method: "POST",
        body: formData
    });

    return res.json();
};

export const sendMessage = async (message) => {
    const res = await fetch(`${API_URL}/chat/?query=${message}`, {
        method: "POST"
    });

    return res.json();
};
