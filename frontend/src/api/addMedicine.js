import BASE_URL from "./init";

export const addMedicine = async (payLoad) => {
    const url = `${BASE_URL}/api/v1/admin/medicine_list`;
    const token = JSON.parse(localStorage.getItem('userToken')).access;
    try{
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(payLoad),
    });

    let result = await response.json();

    if (!response.ok) {
        result = {
            "status": response.status,
            "message": result.detail,
        };
    } else {
        result = {
            "status": "success",
            "result": result,
        };
    }
    return result;
    }catch{
        result = {
            "status": "bad request",
        };
        return result
    }

};
