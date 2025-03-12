"use client";
import { useState } from "react";
import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-4xl font-bold mb-6">Secure Data Manager</h1>
      <div className="space-x-10 text-4xl" >
        <Link href="/insertdata">
          <button className="cursor-pointer px-6 py-3 bg-blue-600 rounded-xl shadow-lg hover:bg-blue-700 w-2xs aspect-square">Insert Data</button>
        </Link>
        <Link href="/getdata">
          <button className="cursor-pointer px-6 py-3 bg-blue-600 rounded-xl shadow-lg hover:bg-blue-700 w-2xs aspect-square">Get Data</button>
        </Link>
      </div>
    </div>
  );
}