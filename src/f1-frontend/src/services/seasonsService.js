import client from "./client"

const seasonsService = {
    async getSeasons(page){
        return await client.get(`/seasons?page=${page}`);
    },
    async getPodiumDrivers(year){
        return await client.get(`/seasons/podium/driver/${year}`)
    },
    async getPodiumConstructors(year){
        return await client.get(`/seasons/podium/constructor/${year}`)
    },
    async deleteSeason(year) {
        return await client.delete(`/seasons/delete`, {
            data: { year: year }
        });
    },
    async addSeason(year,url){
        return await client.post(`/seasons/insert`,{
            year: year,
            url:url
        });
    },
}

export default seasonsService;