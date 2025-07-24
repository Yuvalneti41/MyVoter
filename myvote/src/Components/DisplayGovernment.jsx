import { useState, useEffect } from "react";
import { GetGovernment } from "../API/DisplayGovernment";
import GovernerProfile from "./GovernerProfile";

const DisplayGovernment = () => {
    const [governmentList, setGovernmentList] = useState({});


    useEffect(() => {
        const getData = async () => {
            const res = await GetGovernment();
            console.log(res.data);
            setGovernmentList(res.data);
        }
        getData();
    }, []);

    return (
        <>
            {governmentList && (
                <GovernerProfile governerId={governmentList.party_leader} />
            )}
        </>
    )
}

export default DisplayGovernment;