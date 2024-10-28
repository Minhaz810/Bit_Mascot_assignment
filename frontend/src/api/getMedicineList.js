import BASE_URL from "./init";

export const getMedicineList = async () =>{
    const url = `${BASE_URL}/api/v1/admin/medicine_list`
    const response = await fetch(url,{
        headers:{
            'content-type':'application/json',
            'method':'GET'
        }
    })

    let result = await response.json()
    if (!response.ok){
        result = {
            "status" :response.status,
            "message":result['detail']
        }
    }

    return result
}