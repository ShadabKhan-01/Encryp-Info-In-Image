"use client";
import { useState } from "react";
import Card from "../component/Card";
import Loader from "../component/Loader";

export default function getdata() {
  const [image1, setimage1] = useState()
  const [image2, setimage2] = useState()
  const [imagePreview1, setimagePreview1] = useState()
  const [imagePreview2, setimagePreview2] = useState()
  const [output, setOutput] = useState(null);
  const [Loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("submit start")
    const formData = new FormData();
    formData.append("image1", image1); // Append image1
    formData.append("image2", image2);  // Append image2

    try {
      setLoading(true)
      const response = await fetch("http://localhost:5001/get", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setLoading(false)
      setOutput(data.Final_text);
    } catch (error) {
      setOutput(`Error: ${error.message}`);
      console.error("Error:", error);
    }
  };

  const handleFileChange1 = (e) => {
    const file = e.target.files[0];
    if (file) {
      setimage1(file); // Generate preview URL
      setimagePreview1(URL.createObjectURL(file)); // set image
    }
  }
  const handleFileChange2 = (e) => {
    const file = e.target.files[0];
    if (file) {
      setimage2(file); // Generate preview URL
      setimagePreview2(URL.createObjectURL(file)); // set image
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">Insert Images</h1>
      <form onSubmit={handleSubmit}>
        <div className="md:flex gap-5">
          <section>
            <div className="w-80 mb-2">
              <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
              <input className="p-1 h-8 block w-full text-sm text-gray-900 border border-gray-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input1" type="file" accept="image/*" onChange={handleFileChange1} required></input>
            </div>
            {imagePreview1 && (
              <div>
                <h3>Uploaded Image:</h3>
                <img src={imagePreview1} alt="Uploaded" style={{ maxWidth: "300px" }} />
              </div>
            )}
          </section>
          <section>
            <div className="w-80 mb-2">
              <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
              <input className="p-1 h-8 block w-full text-sm text-gray-900 border border-gray-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input2" type="file" accept="image/*" onChange={handleFileChange2} required></input>
            </div>
            {imagePreview1 && (
              <div>
                <h3>Uploaded Image:</h3>
                <img src={imagePreview2} alt="Uploaded" style={{ maxWidth: "300px" }} />
              </div>
            )}
          </section>
        </div>
        <button type="submit" className="mx-auto px-6 py-2 bg-green-500 rounded-lg hover:bg-green-600">Decrypt & Retrieve</button>
      </form>
      {(Loading) && (
        <Loader />
      )}
      {output && (
        <Card Text={output} />
      )}
    </div>
  );
}