import { Link, useParams } from "react-router";
import { useQuery } from "@tanstack/react-query";
import { GiFullMotorcycleHelmet } from "react-icons/gi";
import { PiSmileySadFill } from "react-icons/pi";
import { HiTrophy } from "react-icons/hi2";

import { driversService } from "../../services";
import { flagCountries } from "./utils";

const DriverProfile = () => {
  const { id } = useParams();
  const { data: driverData } = useQuery({
    queryKey: ["driver-", id],
    queryFn: () => driversService.getDriverById(id),
  });

  return (
    <div className="p-6">
      {driverData?.data ? (
        <div className="flex flex-col justify-center items-center gap-10">
          <h1 className="flex gap-2 items-center text-2xl font-semibold">
            {" "}
            <GiFullMotorcycleHelmet className="text-4xl" /> Driver Details
          </h1>
          <div className="flex flex-col gap-4">
            <div className="flex flex-col gap-10 border-2 border-error shadow-xl p-6 rounded-2xl">
              <h1 className="text-2xl font-bold">Personal Details</h1>
              <div className="divider divider-error my-[-20px]"></div>
              <div className="flex justify-around items-center w-full">
                <div className="flex flex-col text-xl space-y-3">
                  <p className="flex gap-4">
                    <span className="font-semibold">First Name</span>{" "}
                    {driverData.data.data?.forename}
                  </p>
                  <p className="flex gap-4">
                    <span className="font-semibold">Last Name</span>{" "}
                    {driverData.data.data?.surname}
                  </p>
                  <p className="flex gap-4">
                    <span className="font-semibold">Date of Birth</span>{" "}
                    {driverData.data.data?.dob}
                  </p>
                  {driverData.data.data?.code && (
                    <span className="flex gap-4">
                      <h1 className="font-semibold">Code</h1>{" "}
                      {driverData.data.data?.code}
                    </span>
                  )}
                  {driverData.data.data?.number && (
                    <span className="flex gap-4">
                      <h1 className="font-semibold">Number</h1>{" "}
                      {driverData.data.data?.number}
                    </span>
                  )}
                  <a
                    className="badge badge-soft badge-primary text-lg"
                    target="_blank"
                    href={driverData.data.data?.url}
                  >
                    {driverData.data.data?.url}
                  </a>
                </div>
                <div className="divider divider-horizontal"></div>
                <div className="card bg-base-100 border-2 h-max border-white shadow-sm w-max p-1">
                  <figure>
                    <img
                      src={`${
                        flagCountries[driverData.data.data?.nationality]
                      }`}
                      alt="Country Flag"
                      className="h-20 w-20"
                    />
                  </figure>
                  <div className="card-body">
                    <h2 className="text-xl text-center justify-center">
                      {driverData.data.data?.nationality}
                    </h2>
                  </div>
                </div>
              </div>
            </div>
            <div className="card gap-10 items-center border-2 border-error shadow-xl p-2 rounded-2xl">
              <div className="card-body">
                <h1 className="card-title text-2xl">Races Won</h1>
                <div className="divider divider-error"></div>
                {driverData?.data?.wins?.length > 0 ? (
                  <div className="grid grid-cols-3 gap-y-6 gap-x-6 overflow-y-auto w-full max-h-[30rem]">
                    {driverData.data.wins?.map((win) => (
                      <Link
                        className="duration-200 transition hover:scale-90"
                        to={`/races/${win.raceName.replace(/\s/g, "_")}/${
                          win.raceId.split(".org/race/")[1]
                        }`}
                      >
                        <div
                          key={win.raceId}
                          className="flex flex-col items-center text-warning text-xl border-2 border-warning p-2 space-y-2 rounded-lg"
                        >
                          <span className="badge badge-warning text-xl">
                            {win.raceName} {win.raceYear}
                          </span>
                          <span className="flex items-center gap-1">
                            <HiTrophy /> Points {win.points}
                          </span>
                        </div>
                      </Link>
                    ))}
                  </div>
                ) : (
                  <div className="flex gap-1 items-center text-xl text-warning">
                    <PiSmileySadFill /> This driver doesn't have any wins yet
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      ) : (
        <h1 className="text-4xl">No data found</h1>
      )}
    </div>
  );
};

export default DriverProfile;
