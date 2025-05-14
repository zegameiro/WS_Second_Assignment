import { useState } from "react";
import { FaCirclePlus } from "react-icons/fa6";
import { useMutation } from "@tanstack/react-query";
import { seasonsService } from "../../services";
import { useNavigate } from "react-router";

function SeasonsAdd(){
    const [year,setYear] = useState("");
    const [url,setUrl] = useState("");
    const navigate = useNavigate();

    const sendMutation = useMutation({
        mutationKey: ["addSeason"],
        mutationFn: (data) =>
          seasonsService.addSeason(year,url).then(() => {
            navigate("/seasons")
          }),
      });

    return(
        <div className="w-[60%] mx-auto h-[100vh] flex flex-col items-center justify-center">
            <div className=" border-2 border-error rounded-lg flex flex-col items-center w-[30%] gap-3 p-3">
                <span className="text-xl">Adding a Season</span>
                <input type="number" placeholder="Year" className="input" onChange={(e)=> setYear(e.currentTarget.value)} />
                <input type="text" placeholder="Url" className="input" onChange={(e)=> setUrl(e.currentTarget.value)}/>
                <button className="flex items-center btn bg-red-500" onClick={()=>sendMutation.mutate({
                    year:year,
                    url:url,
                })}><FaCirclePlus/>Add</button>
            </div>
        </div>
    )
}

export default SeasonsAdd;