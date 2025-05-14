import { FaClock,FaFlagCheckered,FaTrophy } from "react-icons/fa";
import { GiF1Car,GiFullMotorcycleHelmet } from "react-icons/gi";


function TimelineInfoCard({racename,winner,fastLap}){
  return(
    <div className="w-full min-w-50">
      <h1 className="text-red-400 font-bold text-2xl flex items-center gap-1"><FaFlagCheckered />{racename}</h1>
      <div className="divider my-[-3px]"></div>
        <div className="flex justify-around">
          <div className="w-1/2 text-lg">
            <div className="font-bold flex items-center gap-1 text-green-400"><FaClock/>Fastest Lap</div>
            <div className="flex items-center gap-1"><GiFullMotorcycleHelmet />{fastLap.driverName}</div>
            <div className="flex items-center gap-1"><GiF1Car className="text-xl" />{fastLap.constructorName}</div>
            <div className="flex items-center gap-1"><FaClock/>{fastLap.time}</div>
          </div>
          <div className="w-1/2 text-lg">
            <div className="font-bold flex items-center gap-1 text-yellow-300"><FaTrophy/>Race Winner</div>
            <div className="flex items-center gap-1"><GiFullMotorcycleHelmet />{winner.driverName}</div>
            <div className="flex items-center gap-1"><GiF1Car className="text-xl" />{winner.constructorName}</div>
            <div className="flex items-center gap-1"><FaClock/>{winner.fastestLap}</div>
          </div>
      </div>
    </div>
  )
}

export default TimelineInfoCard;