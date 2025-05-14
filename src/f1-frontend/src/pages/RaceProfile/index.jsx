import { useParams, Link } from "react-router";
import { useQuery } from "@tanstack/react-query";
import { racesService } from "../../services";
import { GiFullMotorcycleHelmet, GiF1Car } from "react-icons/gi";
import { FaFlagCheckered } from "react-icons/fa";
import { motion } from "motion/react";
import { FaClock } from "react-icons/fa6";

const RaceProfile = () => {
  let { name, id } = useParams();

  const { data } = useQuery({
    queryKey: ["racesById-", id],
    queryFn: () => racesService.getRaceId(id),
  });

  return (
    <div className="p-6">
      <h1 className="flex items-center gap-2 text-2xl font-semibold pb-5">
        {" "}
        <FaFlagCheckered /> Race Details
      </h1>
      <div className="flex flex-col gap-4">
        <div className="flex justify-between gap-10 border-2 border-error shadow-xl p-6 rounded-2xl w-full">
          <div className="flex flex-col gap-7 w-full">
            <h1 className="text-2xl font-bold">Race Information</h1>
            <div className="divider divider-error my-[-20px]"></div>
            <div className="flex items-center w-full">
              <div className="flex flex-col text-xl space-y-3">
                {data?.data?.race?.name && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Name</span>{" "}
                    {data?.data?.race?.name}
                  </p>
                )}
                {data?.data?.race?.date && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Date</span>{" "}
                    {data?.data?.race?.date}
                  </p>
                )}
                {data?.data?.race?.round && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Round</span>{" "}
                    {data?.data?.race?.round}
                  </p>
                )}
                {data?.data?.race?.url && (
                  <a
                    className="badge badge-soft badge-primary text-lg"
                    target="_blank"
                    href={data?.data?.race?.url}
                  >
                    {data?.data?.race?.url}
                  </a>
                )}
              </div>
            </div>
          </div>
          <div className="divider divider-horizontal divider-error"></div>
          <div className="flex flex-col gap-7 w-full">
            <h1 className="text-2xl font-bold">Circuit Information</h1>
            <div className="divider divider-error my-[-20px]"></div>
            <div className="flex items-center w-full">
              <div className="flex flex-col text-xl space-y-3">
                {data?.data?.circuit?.name && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Name</span>{" "}
                    {data?.data?.circuit?.name}
                  </p>
                )}
                {data?.data?.circuit?.location && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Location</span>{" "}
                    {data?.data?.circuit?.location}
                  </p>
                )}
                {data?.data?.circuit?.lat && data?.data?.circuit?.lng && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Coordinates</span> (
                    {data?.data?.circuit?.lat}, {data?.data?.circuit?.lng})
                  </p>
                )}
                {data?.data?.circuit?.country && (
                  <p className="flex gap-4">
                    <span className="font-semibold">Country</span>{" "}
                    {data?.data?.circuit?.country}
                  </p>
                )}
                {data?.data?.circuit?.url && (
                  <a
                    className="badge badge-soft badge-primary text-lg"
                    target="_blank"
                    href={data?.data?.circuit?.url}
                  >
                    {data?.data?.circuit?.url}
                  </a>
                )}
              </div>
            </div>
          </div>
        </div>
        {data?.data?.results && data?.data?.results.length > 0 && (
          <div className="pt-10">
            <div className="flex justify-around h-[200px]">
              <motion.div
                className="bg-amber-700 w-1/5 text-black font-bold text-center h-30 mt-auto rounded-t-xl p-2 pt-3"
                initial={{ height: 0 }}
                animate={{ height: 100 }}
                transition={{ duration: 0.5 }}
              >
                <motion.span
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 1 }}
                >
                  <div className="flex flex-col text-center justify-center items-center">
                    <Link
                      className="duration-200 transition hover:scale-105"
                      to={`/driver/${
                        data?.data?.results[2].driverId.split(".org/driver/")[1]
                      }`}
                    >
                      <span className="flex gap-2 items-center">
                        <GiFullMotorcycleHelmet />
                        {data?.data?.results[2].driverName}
                      </span>
                    </Link>
                    <span className="flex gap-2 items-center">
                      <GiF1Car className="text-3xl" />
                      {data?.data?.results[2].constructorName}
                    </span>
                    <span className="flex items-center gap-2">
                      <FaClock /> {data?.data?.results[2].time}
                    </span>
                  </div>
                </motion.span>
              </motion.div>
              <motion.div
                className="bg-amber-400 w-1/5 text-black font-bold text-center h-50 mt-auto rounded-t-xl p-2 pt-3"
                initial={{ height: 0 }}
                animate={{ height: 200 }}
                transition={{ duration: 0.5 }}
              >
                <motion.span
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 1 }}
                >
                  <div className="flex flex-col text-center justify-center items-center">
                    <Link
                      className="duration-200 transition hover:scale-105"
                      to={`/driver/${
                        data?.data?.results[0].driverId.split(".org/driver/")[1]
                      }`}
                    >
                      <span className="flex gap-2 items-center">
                        <GiFullMotorcycleHelmet />
                        {data?.data?.results[0].driverName}
                      </span>
                    </Link>
                    <span className="flex gap-2 items-center">
                      <GiF1Car className="text-3xl" />
                      {data?.data?.results[0].constructorName}
                    </span>
                    <span className="flex items-center gap-2">
                      <FaClock /> {data?.data?.results[0].time}
                    </span>
                  </div>
                </motion.span>
              </motion.div>
              <motion.div
                className="bg-gray-400 w-1/5 text-black font-bold text-center h-40 mt-auto rounded-t-xl p-2 pt-3"
                initial={{ height: 0 }}
                animate={{ height: 150 }}
                transition={{ duration: 0.5 }}
              >
                <motion.span
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 1 }}
                >
                  <div className="flex flex-col text-center justify-center items-center">
                    <Link
                      className="duration-200 transition hover:scale-105"
                      to={`/driver/${
                        data?.data?.results[1].driverId.split(".org/driver/")[1]
                      }`}
                    >
                      <span className="flex gap-2 items-center">
                        <GiFullMotorcycleHelmet />
                        {data?.data?.results[1].driverName}
                      </span>
                    </Link>
                    <span className="flex gap-2 items-center">
                      <GiF1Car className="text-3xl" />
                      {data?.data?.results[1].constructorName}
                    </span>
                    <span className="flex items-center gap-2">
                      <FaClock /> {data?.data?.results[1].time}
                    </span>
                  </div>
                </motion.span>
              </motion.div>
            </div>
            <div className="divider text-xl divider-accent">Drivers Podium</div>
          </div>
        )}
      </div>
    </div>
  );
};

export default RaceProfile;
