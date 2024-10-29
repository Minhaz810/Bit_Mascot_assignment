import BASE_URL from "./init";

export const deleteMedicine = async (id) => {
    const url = `${BASE_URL}/api/v1/admin/medicine_list?id=${id}`;
    const token = JSON.parse(localStorage.getItem('userToken')).access;

    const response = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
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
            "message": "Medicine deleted successfully",
        };
    }
    return result;
};
