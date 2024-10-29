import { useState,useEffect } from "react";
import { getMedicineList } from "../api/getMedicineList";
import { getManufacturerList } from "../api/getManufacturerList";
import { extractPageNumber } from "../api/utils";
import { useNavigate } from "react-router-dom";
import { updateMedicine } from "../api/updateMedicine";
import { deleteMedicine } from "../api/deleteMedicine";

const AdminPage = () => {
    const [medicineList,setMedicineList] = useState([])
    const [manufacturerList,setManufacturerList] = useState([])
    const [loading,setLoading] = useState(false)
    const [next,setNext] = useState(null)
    const [prev,setPrev] = useState(null)
    const [query,setQuery] = useState("")
    const [deleteModalOpen,setDeleteModalOpen] = useState(false)
    const [editModelOpen,setEditModalOpen] = useState(false)
    const [editableData,setEditableData] = useState({})
    const [medicineName, setMedicineName] = useState(editableData?.name || "");
    const [medicinePrice, setMedicinePrice] = useState(editableData?.price || "");
    const [manufacturer, setManufacturer] = useState(editableData?.manufacturer || {});
    const [genericName, setGenericName] = useState(editableData?.generic_name || "");
    const [description, setDescription] = useState(editableData?.description || "");
    const [batchNumber, setBatchNumber] = useState(editableData?.batch_number || "");
    const [otherDetails, setOtherDetails] = useState(editableData?.other_related_details || "");
    const [selectedID,setSelectedID] = useState(null)

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

    const fetchManufacturerList = async () =>{
        setLoading(true)
        let data = await getManufacturerList()
        if(data["status"] == "success"){
            setManufacturerList(data["result"]["results"])
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
    
    const handleLogoutClick = () =>{
        localStorage.removeItem('userToken');
        navigate("/")
    }

    const handleDeleteModalPopUp = (id) => {
        setSelectedID(id)
        setDeleteModalOpen(true)
    }

    const handleEditModalPopUp = (item) => {
        setEditableData(item)
        setEditModalOpen(true)
    }

    const handleDelete = async () =>{
        const result = await deleteMedicine(selectedID)
        if (result["status"]==="success"){
            setDeleteModalOpen(false)
            fetchMedicineList()
        }
    }
    
    const handleUpdate = async () =>{
        const payLoad = {
            "id":editableData.id,
            "name": medicineName,
            "price": medicinePrice,
            "manufacturer": manufacturer,
            "generic_name": genericName,
            "description": description,
            "batch_number": batchNumber,
            "other_related_detailes": otherDetails
          };
        
        const result = await updateMedicine(payLoad)
        if (result["status"]==="success"){
            setEditModalOpen(false)
            fetchMedicineList()
        }
    }

    useEffect(()=>{
        fetchMedicineList()
        fetchManufacturerList()
    },[])

    useEffect(() => {
        if (editableData) {
          setMedicineName(editableData.name || "");
          setMedicinePrice(editableData.price || "");
          setManufacturer(editableData.manufacturer || "");
          setGenericName(editableData.generic_name || "");
          setDescription(editableData.description || "");
          setBatchNumber(editableData.batch_number || "");
          setOtherDetails(editableData.other_related_detailes || "");
        }
      }, [editableData]);
    
    
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
                        onClick={handleLogoutClick}
                    >
                        Logout
                    </button>
                    </div>
                </div>
            </div>
            
            <div className="flex flex-col mt-4">
                <div className="flex items-center justify-center">
                    <h1 className="text-4xl font-bold text-gray-800 ">
                        Admin Panel
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
                            <div className="flex justify-between">
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
                                <div className="mt-16 flex space-x-4">
                                    <button className="px-4 py-1 bg-blue-500 text-white font-semibold rounded 
                                    hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300"
                                    onClick={()=>{handleEditModalPopUp(item)}}
                                    >
                                        Edit
                                    </button>
                                    <button className="px-4 py-1 bg-red-500 text-white font-semibold rounded
                                     hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-300"
                                     onClick={()=>{handleDeleteModalPopUp(item.id)}}
                                     >
                                        Delete
                                    </button>
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
            {deleteModalOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
                    <div className="w-full max-w-sm rounded-xl bg-white px-8 py-12 shadow-lg">
                        <div className="mb-4 text-center">
                            Are you Sure You Want To Delete This Medicine
                        </div>
                        <div className="flex justify-center space-x-4">
                            <button
                                className="rounded-full bg-[rgba(0,200,0,0.8)] px-10 py-2 font-semibold text-white transition-transform duration-300 hover:scale-105"
                                onClick={()=>handleDelete()}
                            >
                                Yes
                            </button>
                            <button
                                className="rounded-full bg-[rgba(255,0,0,0.8)] px-10 py-2 font-semibold text-white transition-transform duration-300 hover:scale-105"
                                onClick={() => setDeleteModalOpen(false)}
                            >
                                No
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {editModelOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
                <div className="w-full max-w-sm rounded-xl bg-white px-8 py-12 shadow-lg">
                    <div className="mb-6 text-center font-semibold text-lg">
                    Edit Medicine Details
                    </div>
                    <div className="space-y-4">
                    <input
                        type="text"
                        placeholder="Name"
                        value={medicineName}
                        onChange={(e) => setMedicineName(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="number"
                        placeholder="Price"
                        value={medicinePrice}
                        onChange={(e) => setMedicinePrice(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <select
                        value=""
                            onChange={(e) => {
                            const selectedManufacturer = manufacturerList.find(item => item.id === parseInt(e.target.value));
                            setManufacturer(selectedManufacturer);
                        }}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="" disabled>{manufacturer?.name}</option>
                        {manufacturerList.map((item) => (
                        <option key={item.id} value={item.id}>
                            {item.name}
                        </option>
                        ))}
                    </select>
                    <input
                        type="text"
                        placeholder="Generic Name"
                        value={genericName}
                        onChange={(e) => setGenericName(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="text"
                        placeholder="Description"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="text"
                        placeholder="Batch Number"
                        value={batchNumber}
                        onChange={(e) => setBatchNumber(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="text"
                        placeholder="Other Details"
                        value={otherDetails}
                        onChange={(e) => setOtherDetails(e.target.value)}
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    </div>
                    <div className="flex justify-center space-x-4 mt-6">
                    <button
                        className="rounded-full bg-[rgba(0,200,0,0.8)] px-10 py-2 font-semibold text-white transition-transform duration-300 hover:scale-105"
                        onClick={() => handleUpdate()}
                    >
                        Save
                    </button>
                    <button
                        className="rounded-full bg-[rgba(255,0,0,0.8)] px-10 py-2 font-semibold text-white transition-transform duration-300 hover:scale-105"
                        onClick={() => setEditModalOpen(false)}
                    >
                        Cancel
                    </button>
                    </div>
                </div>
              </div>
            )}
        </>
    )
}

export default AdminPage
