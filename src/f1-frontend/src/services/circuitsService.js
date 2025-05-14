import client from "./client"

const circuitsService = {
    async getCircuits(page){
        return await client.get(`/circuits`);
    }
}

export default circuitsService;