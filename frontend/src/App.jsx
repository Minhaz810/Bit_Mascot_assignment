import { useState,useEffect } from 'react'
import { getMedicineList } from './api/getMedicineList'

export default function App() {
  useEffect(()=>{
    const fetchMedicineList = async () =>{
      const result = await getMedicineList()
      console.log(result)
    }
    fetchMedicineList()
  },[])

  return (
    <h1 className="text-3xl">
      Hello world!
    </h1>
  )
}
