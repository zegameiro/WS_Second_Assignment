import logo from "../../../public/f1_logo.png";
import { Link } from "react-router";

function NavBar({ children }) {
  return (
    <div className="navbar bg-[#e10600] shadow-sm">
      <div className="flex-1">
        <Link to="/">
          <img src={logo} alt="logo" className="h-10" />
        </Link>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-2">
          {children}
        </ul>
      </div>
    </div>
  );
}

export default NavBar;
