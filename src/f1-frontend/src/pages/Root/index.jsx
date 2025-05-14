import { Outlet } from "react-router";
import { NavBar, NavBarLink } from "../../components";

import { GiFullMotorcycleHelmet, GiF1Car } from "react-icons/gi";
import { FaFlagCheckered } from "react-icons/fa";
import { FaCalendarDays } from "react-icons/fa6";

function Root({}) {

  return (
    <div>
      <NavBar>
        <NavBarLink to="/driver">
          <GiFullMotorcycleHelmet />
          <span className="ml-2 text-xl font-semibold">Drivers</span>
        </NavBarLink>
        <NavBarLink to="/races">
          <FaFlagCheckered />
          <span className="ml-2 text-xl font-semibold">Races</span>
        </NavBarLink>
        <NavBarLink to="/constructors">
          <GiF1Car className="text-3xl" />
          <span className="ml-2 text-xl font-semibold">Constructors</span>
        </NavBarLink>
        <NavBarLink to="/seasons">
          <FaCalendarDays />
          <span className="ml-2 text-xl font-semibold">Seasons</span>
        </NavBarLink>
      </NavBar>
      <Outlet />
    </div>
  );
}

export default Root;