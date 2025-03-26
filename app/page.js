"use client";
import Link from "next/link";
import dynamic from 'next/dynamic';

const Button = dynamic(() => import('./component/Button'), { ssr: false });

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-center text-3xl md:text-4xl font-bold mb-6">Encrypts text seamlessly into images</h1>
      <div className="flex flex-col md:flex-row items-center gap-5 text-3xl mx-auto" >
        <Link href="/insertdata">
          {/* <button className="cursor-pointer px-6 py-3 bg-blue-600 rounded-xl shadow-lg hover:bg-blue-700 w-2xs aspect-square">Insert Data</button> */}
          <Button Text = {"Encrypt Data"}/>
        </Link>
        <Link href="/getdata">
          {/* <button className="cursor-pointer px-6 py-3 bg-blue-600 rounded-xl shadow-lg hover:bg-blue-700 w-2xs aspect-square">Get Data</button> */}
          <Button Text = {"Decrypt Data"}/>
        </Link>
      </div>
    </div>
  );
}