import { GiFullMotorcycleHelmet } from "react-icons/gi";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";

import { driversService } from "../../services";
import { Table } from "../../components";
import { TablesTypes } from "../../components/Table";

const Drivers = () => {

	const [page, setPage] = useState(1);
  const [query, setQuery] = useState("");

  const queryClient = useQueryClient();
	const { data: driversData } = useQuery({
		queryKey: ["drivers"],
		queryFn: () => query === "" ? driversService.getDrivers(page): driversService.getDriversSearch(page,query),
	});

  useEffect(() => {
    queryClient.refetchQueries({ queryKey: ["drivers"], type: "active" });
  }, [page,query]);

  useEffect(()=>{
    if(driversData?.data.data.length === 0 && page > 1){
      setPage(page - 1);
    }
  },[driversData])

  return (
    <div className="p-6">
      <span className="flex items-center justify-between text-3xl">
        <span className="flex items-center gap-2">
          <GiFullMotorcycleHelmet />
          <h1 className="font-bold">Drivers</h1>
        </span>
        <label className="input">
          <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g strokeLinejoin="round" strokeLinecap="round" strokeWidth="2.5" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path></g></svg>
          <input type="search" className="grow" placeholder="Search" value={query} onChange={(e)=> setQuery(e.target.value)} />
        </label>
      </span>
			<Table data={driversData?.data} page={page} setPage={setPage} type={TablesTypes.DRIVERS} />
    </div>
  );
};

export default Drivers;
