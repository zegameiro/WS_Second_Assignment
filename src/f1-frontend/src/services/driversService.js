import client from "./client"

const driversService = {
    async getDrivers(page) {
        return await client.get(`/drivers?page=${page}`);
    },

    async getDriverById(driverId) {
        return await client.get(`/drivers/${driverId}`);
    },
    async getDriversSearch(page,query){
        return await client.get(`/drivers/search?query=${query}&page=${page}`)
    }
}

export default driversService;