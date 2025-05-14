import { GiF1Car } from "react-icons/gi";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";

import { constructorService } from "../../services";
import { Table } from "../../components";
import { TablesTypes } from "../../components/Table";

const Constructors = () => {

	const [page, setPage] = useState(1);

  const queryClient = useQueryClient();
	const { data: constructorsData } = useQuery({
		queryKey: ["constructors"],
		queryFn: () => constructorService.get_contructors(page),
	});

  useEffect(() => {
    queryClient.refetchQueries({ queryKey: ["constructors"], type: "active" });
  }, [page]);

  useEffect(()=>{
    if(constructorsData?.data.data.length === 0 && page > 1){
      setPage(page - 1);
    }
  },[constructorsData])

  return (
    <div className="p-6">
      <span className="flex items-center justify-between text-3xl">
        <span className="flex items-center gap-2">
          <GiF1Car className="text-6xl" />
          <h1 className="font-bold">Constructors</h1>
        </span>
      </span>
			<Table data={constructorsData?.data} page={page} setPage={setPage} type={TablesTypes.CONSTRUCTORS} />
    </div>
  );
};

export default Constructors;
