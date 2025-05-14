import {createBrowserRouter} from "react-router";
import { Home, Root, Drivers, Races, DriverProfile, Seasons, Constructors, Season, RacesYears, RaceProfile, SeasonsAdd } from "./pages";

const routes = createBrowserRouter([
    {
      path: "/",
      element: <Root/>,
      children: [
        { index: true, Component: Home },

        { path: "driver", Component: Drivers },
        { path: "driver/:id", Component: DriverProfile },

        { path: "races", Component: Races },
        { path: "races/:name", Component: RacesYears },
        { path: "races/:name/:id", Component: RaceProfile },
        
        { path: "seasons", Component: Seasons},
        { path: "seasons/add", Component: SeasonsAdd},
        { path: "seasons/:year", Component: Season},

        { path: "constructors", Component: Constructors},
      ]
    },
  ]);

export default routes;