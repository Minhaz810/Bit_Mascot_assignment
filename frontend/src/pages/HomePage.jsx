import { useState,useEffect } from "react";
import { getMedicineList } from "../api/getMedicineList";

const HomePage = () => {
    return (
        <>
            <div className="w-full shadow">
                <div className="flex justify-between h-16 px-20">
                    
                    <div className="flex items-center">
                        <img src="/BitMascott.png" alt="Logo"/>
                    </div>
                    
                    <div className="flex items-center">
                    <button 
                        className="bg-blue-600 text-white font-semibold px-4 py-2 rounded-lg hover:bg-blue-700 transition duration-300"
                    >
                        Login
                    </button>
                    </div>
                </div>
            </div>
            
            <div className="flex flex-col mt-4">
                <div className="flex items-center justify-center">
                    <h1 className="text-4xl font-bold text-gray-800 ">
                        Welcome to Medicine Index
                    </h1>
                </div>
                <div className="flex items-center justify-center mt-8 gap-1">
                    <input
                        type="text"
                        placeholder="Search..."
                        className="w-[70%] px-4 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <button className="px-4 py-2 bg-blue-500 text-white rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        Search
                    </button>
                </div>
                <div className="flex items-center justify-center mt-8">
                    <h1 className="text-4xl font-bold text-gray-800 ">
                        Welcome to Medicine Index
                    </h1>
                </div>
            </div>
        </>
    )
}

export default HomePage
