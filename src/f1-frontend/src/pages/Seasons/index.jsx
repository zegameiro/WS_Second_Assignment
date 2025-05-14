import { FaCalendarDays } from "react-icons/fa6";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";
import { FaCirclePlus } from "react-icons/fa6";

import { seasonsService } from "../../services";
import { Table } from "../../components";
import { TablesTypes } from "../../components/Table";
import { Link } from "react-router";

function Seasons() {
	const [page, setPage] = useState(1);

	const queryClient = useQueryClient();
	const { data: seasonsData } = useQuery({
		queryKey: ["seasons"],
		queryFn: () => seasonsService.getSeasons(page),
	});

	useEffect(() => {
		queryClient.refetchQueries({ queryKey: ["seasons"], type: "active" });
	}, [page]);

	useEffect(()=>{
    if(seasonsData?.data.data.length === 0){
      setPage(page - 1);
    }
  },[seasonsData])

	return (
	<div className="p-6">
		<span className="flex items-center text-3xl justify-between">
			<div className="flex items-center gap-2">
				<FaCalendarDays/>
				<h1 className="font-bold">Seasons</h1>
			</div>
			<Link to={"/seasons/add"}><button className="btn bg-[#e10600] items-center flex"><FaCirclePlus className="text-lg"/> Add Season</button></Link>
		</span>
			<Table data={seasonsData?.data} page={page} setPage={setPage} type={TablesTypes.SEASONS} />
	</div>
	);
}

export default Seasons;