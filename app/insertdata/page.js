"use client";
import { useState } from "react";

export default function getdata() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [binaryText, setBinaryText] = useState("");
  const [rgbPixels, setRgbPixels] = useState([]);
  const [imageUrl, setImageUrl] = useState("");
  // const [output, setOutput] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", file); // Append image
    formData.append("text", text);  // Append text

    try {
      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setBinaryText(data.binary_text);
      setRgbPixels(data.rgb_pixels);
      setImageUrl(`data:image/png;base64,${data.image_base64}`);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">Encrypt Data</h1>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <div className="w-80 mb-2">
          <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
          <input className="p-1 h-8 block w-full text-sm text-gray-900 border border-gray-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file" accept="image/*" onChange={handleFileChange} required></input>
        </div>
        <input
          type="text"
          placeholder="Enter encrypted data..."
          value={text}
          onChange={handleTextChange}
          required
          className="px-4 py-2 mb-4 w-80 rounded bg-gray-700 border border-gray-500"
        />
        <button type="submit" className="px-6 py-2 bg-green-500 rounded-lg hover:bg-green-600 block">Encrypt</button>
      </form>
      {/* <p className="mt-4 text-yellow-400">{output}</p> */}

      {binaryText && (
        <div>
          <h3>Binary Text:</h3>
          <p>{binaryText}</p>
        </div>
      )}

      {imageUrl && (
        <div>
          <h3>Uploaded Image:</h3>
          <img src={imageUrl} alt="Uploaded" style={{ maxWidth: "300px" }} />
        </div>
      )}

      {rgbPixels.length > 0 && (
        <div>
          <h3>RGB Pixel Data (First 5 Rows):</h3>
          <pre>{JSON.stringify(rgbPixels.slice(0, 5), null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
