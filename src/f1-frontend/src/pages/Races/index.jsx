import { FaFlagCheckered } from "react-icons/fa";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";
import { FaCirclePlus } from "react-icons/fa6";

import { racesService } from "../../services";
import { Table } from "../../components";
import { TablesTypes } from "../../components/Table";
import { Modal } from "../../components";

function Races() {
  const [page, setPage] = useState(1);

  const queryClient = useQueryClient();
  const { data: racesData, isSuccess } = useQuery({
    queryKey: ["races"],
    queryFn: () => racesService.getRaces(page),
  });

  useEffect(() => {
    queryClient.refetchQueries({ queryKey: ["races"], type: "active" });
  }, [page]);

  useEffect(() => {
    if (racesData?.data.data.length === 0) {
      setPage(page - 1);
    }
  }, [racesData]);
  if (isSuccess) {
    return (
      <div className="p-6">
        <div className="flex justify-between items-center mb-4">
          <span className="flex items-center text-3xl gap-2">
            <FaFlagCheckered />
            <h1 className="font-bold">Races</h1>
          </span>
          <button
            className="btn bg-[#e10600]"
            onClick={() => document.getElementById("my_modal_5").showModal()}
          >
            <FaCirclePlus /> Add a new Race
          </button>
        </div>
        <Modal />
        <Table
          data={racesData?.data}
          page={page}
          setPage={setPage}
          type={TablesTypes.RACES}
        />
      </div>
    );
  } else {
    return <div>Loading...</div>;
  }
}

export default Races;
