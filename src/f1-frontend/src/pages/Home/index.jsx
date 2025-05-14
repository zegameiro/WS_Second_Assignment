import { useEffect, useState } from "react";
import { motion, useScroll, useMotionValueEvent } from "motion/react";
import f1_car from "../../../public/f1_car.png"
import back from "../../../public/backGround.jpg"
import { Link } from "react-router";

import { GiFullMotorcycleHelmet, GiF1Car } from "react-icons/gi";
import { FaFlagCheckered } from "react-icons/fa";
import { FaCalendarDays } from "react-icons/fa6";

function Home() {
  const { scrollY } = useScroll();
  const [skew,setSkew] = useState(0);

  useMotionValueEvent(scrollY, "change", (latest) => {
    setSkew(Math.min((latest / 300) * 15, 15));
  })
  
  return(
    <div className="items-center flex flex-col">
      <h1 className="text-7xl font-bold p-8">Pitstop The F1 Data Checker</h1>
      <div className="divider w-[80%] mx-auto"></div>
      <div className="flex w-[60%] justify-items-center">
        <div className="w-full relative min-h-[800px]">
          <motion.img src={back} className="rounded-3xl absolute" animate={{skewX:skew/3,rotateY:skew,boxShadow:`-10px 5px 5px black`}}/>
          <motion.img src={f1_car} className="w-full absolute pointer-events-none" animate={{x:skew*20,y:skew*20}}/>
        </div>
      </div>
      <div className="flex flex-col justify-items-start w-[60%]">
        <h1 className="text-5xl pb-5">Explore</h1>
        <div className="grid grid-cols-2 w-[50%] gap-2">
          <Link to="/driver">
          <butoon className="btn bg-[#e10600] items-center flex w-full">
            <GiFullMotorcycleHelmet />
            <span className="ml-2 text-xl font-semibold">Drivers</span>
          </butoon>
          </Link>
          <Link to="/races">
          <button className="btn bg-[#e10600] items-center flex w-full">
            <FaFlagCheckered />
            <span className="ml-2 text-xl font-semibold">Races</span>
          </button>
          </Link>
          <Link to="/constructors">
          <butoon className="btn bg-[#e10600] items-center flex w-full">
            <GiF1Car className="text-3xl" />
            <span className="ml-2 text-xl font-semibold">Constructors</span>
          </butoon>
          </Link>
          <Link to="/seasons">
          <butoon className="btn bg-[#e10600] items-center flex w-full">
            <FaCalendarDays />
            <span className="ml-2 text-xl font-semibold">Seasons</span>
          </butoon>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Home;