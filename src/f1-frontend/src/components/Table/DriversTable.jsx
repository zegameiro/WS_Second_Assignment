import { FaRegQuestionCircle } from "react-icons/fa";
import { PiMagnifyingGlassPlusBold } from "react-icons/pi";
import { Link } from "react-router";
import { flagCountries } from "../../pages/DriverProfile/utils";

function DriversTable({ drivers, indexDriver }) {
  return (
    <table className="table table-zebra">
      <thead>
        <tr>
          <th></th>
          <th>Name</th>
          <th>Nationality</th>
          <th>Code</th>
          <th>Number</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {drivers?.data.map((driver, index) => (
          <tr key={index} className="text-lg">
            <th>{indexDriver + index + 1}</th>
            <td>{`${driver.forename} ${driver.surname}`}</td>
            <td>
              <img
                src={`${flagCountries[driver.nationality]}`}
                alt="Country Flag"
                className="h-10 w-10"
              />
            </td>
            <td>
              {driver.code ? (
                <span className="badge badge-outline badge-error">
                  {driver.code}
                </span>
              ) : (
                <FaRegQuestionCircle className="text-warning text-xl" />
              )}
            </td>
            <td>
              {driver.number ? (
                driver.number
              ) : (
                <FaRegQuestionCircle className="text-warning text-xl" />
              )}
            </td>
            <td>
              <Link to={`${driver.driverId.split(".org/driver/")[1]}`}>
                <button className="btn btn-soft btn-info btn-circle">
                  <PiMagnifyingGlassPlusBold className="text-xl" />
                </button>
              </Link>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DriversTable;
