import { useParams, Link } from "react-router";
import { FaCheckCircle } from "react-icons/fa";
import { useQuery } from "@tanstack/react-query";
import { racesService, seasonsService } from "../../services";
import TimelineInfoCard from "./card";
import { motion } from "motion/react";
import { GiFullMotorcycleHelmet, GiF1Car } from "react-icons/gi";
import { FaFireAlt } from "react-icons/fa";

function Season() {
  const { year } = useParams();

  const { data: races, isSuccess } = useQuery({
    queryKey: ["races"],
    queryFn: () => racesService.getRacesYear(year),
  });
  const { data: drivers, isSuccess: isSuccess2 } = useQuery({
    queryKey: ["driversPodium"],
    queryFn: () => seasonsService.getPodiumDrivers(year),
  });
  const { data: constructors, isSuccess: isSuccess3 } = useQuery({
    queryKey: ["constructorPodium"],
    queryFn: () => seasonsService.getPodiumConstructors(year),
  });

  if (isSuccess && isSuccess2 && isSuccess3) {
    return (
      <div className="p-6">
        <h1 className="text-6xl">Season of {year}</h1>
        <div className="divider divider-error"></div>
        <div className="flex w-full">
          <div className="w-1/2 flex flex-col items-center">
            <div className="text-4xl font-bold">Races Timeline</div>
            <div>
              <ul className="timeline timeline-vertical timeline-start">
                {races?.data.data.map((race, index) => (
                  <li key={index} className="place-items-start">
                    {index !== 0 && <hr />}
                    <div className="timeline-start">
                      {race.date !== undefined && race.date}
                    </div>
                    <div className="timeline-middle">
                      <FaCheckCircle />
                    </div>
                    <div className="timeline-end timeline-box w-full">
                      {race.winner !== undefined &&
                        race.raceName !== undefined &&
                        race.fastestLap !== undefined && (
                          <TimelineInfoCard
                            winner={race.winner}
                            racename={race.raceName}
                            fastLap={race.fastestLap}
                          />
                        )}
                    </div>
                    {index !== races?.data.data.length - 1 && <hr />}
                  </li>
                ))}
              </ul>
            </div>
          </div>
          <div className="w-1/2 pt-20 flex flex-col gap-20">
            <div>
              <div className="flex justify-around h-[200px]">
                <motion.div
                  className="bg-amber-700 w-1/5 text-black font-bold text-center h-30 mt-auto rounded-t-xl p-2 pt-5"
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
                          drivers?.data?.data[2].driverId.split(
                            ".org/driver/"
                          )[1]
                        }`}
                      >
                        <span className="flex gap-2 items-center">
                          <GiFullMotorcycleHelmet />
                          {drivers.data.data[2].driverName}
                        </span>
                      </Link>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {drivers.data.data[2].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
                <motion.div
                  className="bg-amber-400 w-1/5 text-black font-bold text-center h-50 mt-auto rounded-t-xl p-2 pt-5"
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
                          drivers?.data?.data[0].driverId.split(
                            ".org/driver/"
                          )[1]
                        }`}
                      >
                        <span className="flex gap-2 items-center">
                          <GiFullMotorcycleHelmet />
                          {drivers.data.data[0].driverName}
                        </span>
                      </Link>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {drivers.data.data[0].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
                <motion.div
                  className="bg-gray-400 w-1/5 text-black font-bold text-center h-40 mt-auto rounded-t-xl p-2 pt-5"
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
                          drivers?.data?.data[1].driverId.split(
                            ".org/driver/"
                          )[1]
                        }`}
                      >
                        <span className="flex gap-2 items-center">
                          <GiFullMotorcycleHelmet />
                          {drivers.data.data[1].driverName}
                        </span>
                      </Link>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {drivers.data.data[1].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
              </div>
              <div className="divider text-xl divider-accent">
                Drivers Podium
              </div>
            </div>
            <div>
              <div className="flex justify-around h-[200px]">
                <motion.div
                  className="bg-amber-700 w-1/5 text-black font-bold text-center h-30 mt-auto rounded-t-xl p-2 pt-5"
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
                      <span className="flex gap-1 items-center">
                        <GiF1Car className="text-2xl" />
                        {constructors.data.data[2].constructorName}
                      </span>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {constructors.data.data[2].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
                <motion.div
                  className="bg-amber-400 w-1/5 text-black font-bold text-center h-50 mt-auto rounded-t-xl p-2 pt-5"
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
                      <span className="flex gap-1 items-center">
                        <GiF1Car className="text-2xl" />
                        {constructors.data.data[0].constructorName}
                      </span>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {constructors.data.data[0].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
                <motion.div
                  className="bg-gray-400 w-1/5 text-black font-bold text-center h-40 mt-auto rounded-t-xl p-2 pt-5"
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
                      <span className="flex gap-1 items-center">
                        <GiF1Car className="text-2xl" />
                        {constructors.data.data[1].constructorName}
                      </span>
                      <span className="flex items-center gap-1">
                        <FaFireAlt /> {constructors.data.data[1].totalPoints}
                      </span>
                    </div>
                  </motion.span>
                </motion.div>
              </div>
              <div className="divider text-xl divider-accent">
                Constructor Podium
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return <div>Loading</div>;
  }
}

export default Season;
