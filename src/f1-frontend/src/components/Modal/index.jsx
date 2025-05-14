import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { circuitsService } from "../../services";
import { racesService } from "../../services";

const Modal = () => {
  const { data: circuits } = useQuery({
    queryKey: ["circuits"],
    queryFn: () => circuitsService.getCircuits(),
  });
	const queryClient = useQueryClient();
  const [circuitId, setCircuitId] = useState("");
  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  const [year, setYear] = useState("");
  const [round, setRound] = useState(null);

	const addRaceMutation = useMutation({
		mutationKey: ["addRace"],
		mutationFn: (newRace) => {
			return racesService.addRace(newRace).then(() => {
				queryClient.refetchQueries({ queryKey: ["races"], type: "active" })
				document.getElementById("my_modal_5").close();
			});
		},
	});

	const handleSubmit = () => {
		if(circuitId.length === 0 || name.length === 0 || date.length === 0 || year.length === 0 || round.length === 0) {
			alert("Please fill all the fields");
			return;
		} else {
			addRaceMutation.mutate({
				circuitId: circuitId,
				name: name,
				date: date,
				year: year,
				round: round
			});
			resetForm();
		}
	}

	const resetForm = () => {
		setCircuitId("");
		setName("");
		setDate("");
		setYear("");
		setRound("");
		document.getElementById("my_modal_5").close();
	}

  return (
    <div>
      <dialog id="my_modal_5" className="modal modal-bottom sm:modal-middle">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Add a new Race</h3>
          <fieldset className="fieldset bg-base-200 border border-base-300 p-4 rounded-box">
            <legend className="fieldset-legend">Race Details</legend>

            <label className="fieldset-label">Name</label>
            <input
              type="text"
              className="input w-full"
              placeholder="Name of the Race"
							value={name}
							onChange={(e) => setName(e.target.value)}
            />

            <label className="fieldset-label">Date</label>
            <input 
							type="date" 
							defaultValue={date}
							className="input w-full" 
							onChange={(e) => setDate(e.target.value)}
						/>

            <label className="fieldset-label">Year</label>
            <input
              type="number"
							value={year}
              className="input w-full"
              placeholder="Year of the race"
              onChange={(e) => setYear(e.target.value)}
            />

            <label className="fieldset-label">Round</label>
            <input
              type="number"
              className="input w-full"
							value={round}
              placeholder="Round of the race"
              onChange={(e) => setRound(e.target.value)}
            />
            <legend className="fieldset-label">Circuit</legend>
            <select 
							defaultValue="Choose a Circuit"
							className="select w-full"
							onChange={(e) => setCircuitId(e.target.value)}
						>
							<option disabled>Choose a Circuit</option>
              {circuits?.data?.circuits?.map((circuit) => (
                <option key={circuit.circuitId} value={circuit.circuitId}>
                  {circuit.name}
                </option>
              ))}
            </select>
          </fieldset>
          <div className="modal-action">
            <form method="dialog" className="flex gap-2">
							<button className="btn btn-outline btn-success" onClick={(e) => {e.preventDefault(); handleSubmit()}}>Add Race</button>
              <button className="btn btn-soft btn-error" onClick={(e) => {e.preventDefault(); resetForm()}}>Close</button>
            </form>
          </div>
        </div>
      </dialog>
    </div>
  );
};

export default Modal;
