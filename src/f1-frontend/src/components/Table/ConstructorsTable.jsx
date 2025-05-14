import { PiMagnifyingGlassPlusBold } from "react-icons/pi";
import { flagCountries } from "../../pages/DriverProfile/utils";

function ConstructorsTable({ constructors, indexConstructors }) {
  
  return(
  <table className="table table-zebra">
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>nationality</th>
        <th>wikipedia</th>
      </tr>
    </thead>
    <tbody>
      {constructors?.data.map((constructor, index) => (
        <tr key={index} className="text-lg">
          <th>{indexConstructors + index + 1}</th>
          <td>{`${constructor.name}`}</td>
          <td>
              <img
                src={`${flagCountries[constructor.nationality]}`}
                alt="Country Flag"
                className="h-10 w-10"
              />
            </td>
          <td>{<span className="badge badge-outline badge-error">{constructor.url}</span>}</td>
        </tr>
      ))}
    </tbody>
  </table>
  )
}

export default ConstructorsTable;