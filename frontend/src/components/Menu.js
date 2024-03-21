import { useEffect, useState } from "react";
import Repas from "./Repas";

function Menu() {
    const api_url = "http://127.0.0.1:8000/api/rest/repasListe/";
    const [repasList, setRepasList] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch(api_url);
                if (!res.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await res.json();
                if (Array.isArray(data)) {
                    setRepasList(data);
                } else {
                    throw new Error('Data is not an Array!');
                }
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <>
            <h2 className="text-center p-3">Menu</h2>
            <div className="container">
                <div className="row">
                    {repasList.map((repas) => (
                        <div className="col-3" key={repas.id}>
                            <Repas repas={repas} />
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
}

export default Menu;
