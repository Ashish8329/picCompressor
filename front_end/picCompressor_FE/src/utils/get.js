const BASE_URL = import.meta.env.VITE_API_URL;


export const fetchProductStatus = async (req_id) => {
    const url = `${BASE_URL}/product/?req_id=${req_id}`;
    console.log(url)
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const res = await response.json();
        return res;

    } catch (error) {

        console.error("API Error:", error);
        throw error; 

    }
};
