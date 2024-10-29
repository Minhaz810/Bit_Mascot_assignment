import { useState,useEffect } from "react";
import { getMedicineList } from "../api/getMedicineList";
import { extractPageNumber } from "../api/utils";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
    const [medicineList,setMedicineList] = useState([])
    const [loading,setLoading] = useState(false)
    const [next,setNext] = useState(null)
    const [prev,setPrev] = useState(null)
    const [query,setQuery] = useState("")
    const navigate = useNavigate()



    const fetchMedicineList = async (page,query) =>{
        setLoading(true)
        let data = await getMedicineList(page,query)
        if(data["status"] == "success"){
            setNext(extractPageNumber(data["result"]["next"]))
            setPrev(extractPageNumber(data["result"]["previous"]))
            setMedicineList(data["result"]["results"])
        }
        setLoading(false)
    }

    const handleNext = () =>{
        fetchMedicineList(next,"")
    }

    const handlePrevious = () =>{
        fetchMedicineList(prev,"")
    }

    const handleSearch =()=>{
        fetchMedicineList("",query)
    }
    
    const handleLoginClick = () =>{
        navigate("/login")
    }

    useEffect(()=>{
        fetchMedicineList()
    },[])

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
                        onClick={handleLoginClick}
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
                        placeholder="Search by name or batch no..."
                        className="w-[70%] px-4 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        onChange={(e)=>setQuery(e.target.value)}
                    />
                    <button className="px-4 py-2 bg-blue-500 text-white 
                        rounded-r-md hover:bg-blue-600 focus:outline-none 
                        focus:ring-2 focus:ring-blue-500"
                        onClick={()=>handleSearch()}
                    >
                        Search
                    </button>
                </div>
                <div className="flex flex-col items-center justify-center mt-8 gap-2">
                {
                    medicineList.map((item,index)=>(
                        <div key={index} className="p-4 bg-white rounded-md shadow-lg w-[75%]">
                            <div className="flex justify-between mb-2 text-lg font-semibold">
                                <span className="text-gray-800">{item.name}</span>
                                <span className="text-gray-600">{item.price}</span>
                            </div>
                            
                            <div className="flex flex-col text-sm text-gray-700">
                                <div>
                                    <span className="font-medium">Manufacturer:</span> {item.manufacturer.name}
                                </div>
                                <div>
                                    <span className="font-medium">Generic Name:</span> {item.generic_name}
                                </div>
                                <div>
                                    <span className="font-medium">Description:</span> {item.description}
                                </div>
                                <div>
                                    <span className="font-medium">Batch Number:</span> {item.batch_number}
                                </div>
                                <div>
                                    <span className="font-medium">Other Details:</span> {item.other_related_detailes}
                                </div>
                            </div>
                        </div>
                    
                    ))
                    }
                    <div className="flex gap-4 mt-4">
                        <button className="px-4 py-2 bg-blue-500 text-white 
                            font-semibold rounded hover:bg-blue-600 
                            focus:outline-none focus:ring-2 focus:ring-blue-300"
                            onClick={()=>handlePrevious()}
                        >
                            Previous
                        </button>
                        <button className="px-4 py-2 bg-blue-500 text-white 
                            font-semibold rounded hover:bg-blue-600 
                            focus:outline-none focus:ring-2 focus:ring-blue-300"
                            onClick={()=>handleNext()}
                        >
                            Next
                        </button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default HomePage
