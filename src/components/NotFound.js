import Hero from "./Hero";
import {Link} from "react-router-dom";

const NotFound = () => {
  return (
    <>
      <Hero text="Oops, we couldn't find what you were looking for" />
    <p className = "mx-5 my-2">Click <Link to = "/">here</Link> to return to the homepage. </p>
    </>
  );
};

export default NotFound;
