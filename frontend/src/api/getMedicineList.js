import BASE_URL from "./init";

export const getMedicineList = async (page="",query="") => {
    const url = `${BASE_URL}/api/v1/public/medicine_list?query=${query}&page=${page}`;
    
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    let result = await response.json();
    
    if (!response.ok) {
        result = {
            "status": response.status,
            "message": result.detail,
        };
    }
    result = {
        "status": "success",
        "result":result
    }
    return result;
};
