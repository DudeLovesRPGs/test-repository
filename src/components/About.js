import Hero from "./Hero";
const About = () => {
  return (
    <>
      <Hero text="About us, but from hero component" />
      <div className="container">
        <div className="row">
          <div className="col-lg-8 offset-lg-2 my-5">
            <p className="lead">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem nisi optio nihil voluptates quas eius facere labore accusamus quae possimus laborum porro, magnam velit blanditiis.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
