import { PiMagnifyingGlassPlusBold } from "react-icons/pi";
import { Link } from "react-router";

function RacesTable({ races, indexRaces }) {

  return(
  <table className="table table-zebra">
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Last Year</th>
        <th>First Year</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      {races?.data.map((raceT, index) => (
        <tr key={index} className="text-lg">
          <th>{indexRaces + index + 1}</th>
          <td>{`${raceT.raceName}`}</td>
          <td>{<span className="badge badge-outline badge-success">{raceT.raceDetails !== undefined && raceT.raceDetails[0].year}</span>}</td>
          <td>{<span className="badge badge-outline badge-error">{raceT.raceDetails !== undefined && raceT.raceDetails[raceT.raceDetails.length-1].year}</span>}</td>
          <td>
            <Link to={`${raceT.raceName.replace(/\s/g, "_")}`}>
              <button className="btn btn-soft btn-info btn-circle"><PiMagnifyingGlassPlusBold className="text-xl" /></button>
            </Link>
          </td>
        </tr>
      ))}
    </tbody>
  </table>
  )
}

export default RacesTable;