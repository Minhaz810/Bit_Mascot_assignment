import BASE_URL from "./init";

const SignIn = async (username,password) =>{
    const url = `${BASE_URL}/api/token/`;
    const payload = {
        "username" :username,
        "password":password,
    }
    const response = await fetch(url,{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body: JSON.stringify(payload)
    })

    let result = await response.json()

    if (!response.ok){
        result = {
            "status":"error",
            "message":result['detail']
        }
    }else{
        result = {
            "status":"success",
            "data":result
        }
    }

    return result
}

export default SignIn