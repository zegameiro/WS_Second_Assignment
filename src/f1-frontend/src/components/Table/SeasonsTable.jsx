import { PiMagnifyingGlassPlusBold } from "react-icons/pi";
import { FaTrashCan } from "react-icons/fa6";
import { Link } from "react-router";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { seasonsService } from "../../services";

function SeasonsTable({ seasons, indexSeason }) {
  const queryClient = useQueryClient();
  const deleteSeasonMutation = useMutation({
    mutationKey: ["delete-season"],
    mutationFn: (data) =>
      seasonsService.deleteSeason(data.year).then(() => {
        queryClient.refetchQueries({ queryKey: ["seasons"], type: "active" });
      }),
  });

  return (
    <table className="table table-zebra">
      <thead>
        <tr>
          <th></th>
          <th>year</th>
          <th>url</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {seasons?.data.map((season, index) => (
          <tr key={index} className="text-lg">
            <th>{indexSeason + index + 1}</th>
            <td>{`${season.year}`}</td>
            <td>
              {
                <a className="badge badge-soft badge-primary" href={season.url}>
                  {season.url}
                </a>
              }
            </td>
            <td>
              <Link to={`/seasons/${season.year}`}>
                <button className="btn btn-soft btn-info btn-circle">
                  <PiMagnifyingGlassPlusBold className="text-xl" />
                </button>
              </Link>
            </td>
            <td>
              <button
                onClick={() =>
                  deleteSeasonMutation.mutate({
                    year: season.year,
                  })
                }
                className="btn btn-soft btn-error btn-circle"
              >
                <FaTrashCan />
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default SeasonsTable;
