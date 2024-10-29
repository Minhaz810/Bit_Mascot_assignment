import BASE_URL from "./init";

export const updateMedicine = async (payLoad) => {
    const url = `${BASE_URL}/api/v1/admin/medicine_list`;
    const token = JSON.parse(localStorage.getItem('userToken')).access;

    const response = await fetch(url, {
        method: 'PUT',
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
};
