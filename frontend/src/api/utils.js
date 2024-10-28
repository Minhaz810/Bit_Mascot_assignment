export const extractPageNumber =(url)=> {
    if (url!==null){
        const match = url.match(/page=(\d+)/);
        if (match){
            return match ? parseInt(match[1], 10) : null;
        }else{
            return ""
        }
    }
    return null
}