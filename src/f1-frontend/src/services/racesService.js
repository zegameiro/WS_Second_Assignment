import client from "./client"

const race_service = {
    async getRaces(page) {
        return await client.get(`/races?page=${page}`);
    },
    async getRacesYear(year) {
        return await client.get(`/races/${year}`);
    },
    async getRacesName(name) {
        return await client.get(`/races/name/${name}`);
    },
    async getRaceId(id) {
        return await client.get(`/races/id/${id}`);
    },
    async deleteRace(raceId) {
        return await client.delete(`/races/delete`, {
            data: { raceId: raceId }
        })
    },
    async addRace(raceData) {
        return await client.post('races/insert', {
            circuitId: raceData.circuitId,
            name: raceData.name,
            date: raceData.date,
            year: raceData.year,
            round: raceData.round
        })
    }
}

export default race_service;