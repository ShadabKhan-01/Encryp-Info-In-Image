"use client";
import { useState } from "react";

export default function getdata() {
  const [image1, setimage1] = useState("")
  const [image2, setimage2] = useState(null)
  const [output, setOutput] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image1", image1); // Append image1
    formData.append("image2", image2);  // Append image2

    try {
      const response = await fetch("http://localhost:5000/get", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setOutput();
    } catch {
      setOutput("Error while decripting");
    }
  };

  const handleFileChange1 = (e) => {
    const file = e.target.files[0];
    if (file) {
      setimage1(URL.createObjectURL(file)); // Generate preview URL
    }
  }
  const handleFileChange2 = (e) => {
    const file = e.target.files[0];
    if (file) {
      setimage2(URL.createObjectURL(file)); // Generate preview URL
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">Insert Images</h1>
      <form onSubmit={handleSubmit}>
        <section>
          <div className="w-80 mb-2">
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
            <input className="p-1 h-8 block w-full text-sm text-gray-900 border border-gray-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file" accept="image/*" onChange={handleFileChange1} required></input>
          </div>
          {image1 && (
            <div>
              <h3>Uploaded Image:</h3>
              <img src={image1} alt="Uploaded" style={{ maxWidth: "300px" }} />
            </div>
          )}
        </section>
        <section>
          <div className="w-80 mb-2">
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
            <input className="p-1 h-8 block w-full text-sm text-gray-900 border border-gray-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file" accept="image/*" onChange={handleFileChange2} required></input>
          </div>
          {image2 && (
            <div>
              <h3>Uploaded Image:</h3>
              <img src={image2} alt="Uploaded" style={{ maxWidth: "300px" }} />
            </div>
          )}
        </section>
        <button type="submit" className="px-6 py-2 bg-green-500 rounded-lg hover:bg-green-600">Decrypt & Retrieve</button>
      </form>
      <p className="mt-4 text-yellow-400">{output}</p>
    </div>
  );
}