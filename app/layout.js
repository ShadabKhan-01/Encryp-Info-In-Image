import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Navbar from "./component/Navbar";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata = {
  title: "ImageCrypt - Encrypts text seamlessly into images.",
  description: "ImageCrypt is a secure application that encrypts text into an image, allowing users to send hidden messages safely. The recipient can easily decrypt the message by uploading both the original and encrypted images to the application, revealing the hidden text. Perfect for ensuring privacy and secure communication",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <div className="fixed inset-0 -z-10 h-full w-full items-center px-5 py-24 [background:radial-gradient(125%_125%_at_50%_10%,#000_40%,#63e_100%)]"></div>
        <Navbar/>
        {children}
      </body>
    </html>
  );
}
