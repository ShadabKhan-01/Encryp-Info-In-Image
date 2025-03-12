"use client";
import { useState } from "react";

export default function getdata() {
    const [input, setInput] = useState("");
    const [output, setOutput] = useState("");
  
    const handleRetrieve = () => {
      try {
        setOutput(`Decrypted: ${atob(input)}`);
      } catch {
        setOutput("Invalid data format!");
      }
    };
  
    return (
      <div className="min-h-screen flex flex-col items-center justify-center">
        <h1 className="text-3xl font-bold mb-4">Get Data</h1>
        <input 
          type="text" 
          placeholder="Enter encrypted data..." 
          value={input} 
          onChange={(e) => setInput(e.target.value)} 
          className="px-4 py-2 mb-4 w-80 rounded bg-gray-700 border border-gray-500"
        />
        <button onClick={handleRetrieve} className="px-6 py-2 bg-green-500 rounded-lg hover:bg-green-600">Decrypt & Retrieve</button>
        <p className="mt-4 text-yellow-400">{output}</p>
      </div>
    );
  }