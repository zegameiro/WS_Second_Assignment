import { useEffect, useState } from "react";
import { Link } from "react-router";
import { useParams } from "react-router";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { FaTrashCan } from "react-icons/fa6";

import { FaCalendarAlt } from "react-icons/fa";
import { PiMagnifyingGlassPlusBold } from "react-icons/pi";
import { FaFlagCheckered } from "react-icons/fa";

import { racesService } from "../../services";

const RacesYears = () => {
  const [raceName, setRaceName] = useState("");
  const queryClient = useQueryClient();
  let { name } = useParams();

  const { data } = useQuery({
    queryKey: ["racesByName-", name],
    queryFn: () => racesService.getRacesName(name),
  });

  const deleteRaceMutation = useMutation({
    mutationKey: ["delete-race"],
    mutationFn: (data) => {
      racesService.deleteRace(data.raceId).then(() => {
        queryClient.refetchQueries({
          queryKey: ["racesByName-", name],
          type: "active",
        });
      });
    },
  });

  useEffect(() => {
    let n = name.replace(/_/g, " ");
    setRaceName(n);
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold flex items-center gap-2 pb-6">
        <FaFlagCheckered /> {raceName}
      </h1>
      <div className="flex w-full justify-center">
        {data?.data?.races.length > 0 ? (
          <div className="grid xl:grid-cols-4 lg:grid-cols-3 gap-10">
            {data?.data?.races.map((race, index) => (
              <div
                className="card w-78 bg-black border-1 border-error card-xl shadow-sm"
                key={index}
              >
                <div className="card-body">
                  <h2 className="card-title">
                    <FaCalendarAlt /> {race.raceYear}
                  </h2>
                  <div className="justify-end card-actions">
                    <Link
                      to={race.raceId.split(".org/race/")[1]}
                      className="space-x-2"
                    >
                      <button className="btn btn-error">
                        See More <PiMagnifyingGlassPlusBold />
                      </button>
                    </Link>
                    <button 
                        onClick={() => {
                          deleteRaceMutation.mutate({
                            raceId: race.raceId
                          });
                        }}
                        className="btn btn-error">
                        <FaTrashCan />
                      </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div>No races found</div>
        )}
      </div>
    </div>
  );
};

export default RacesYears;
