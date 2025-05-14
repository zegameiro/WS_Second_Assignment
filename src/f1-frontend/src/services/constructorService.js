import client from "./client"

const constructorService = {
    async get_contructors(page){
        return await client.get(`/constructors?page=${page}`);
    }
}

export default constructorService;