import Hero from './Hero';

const Home = () => {
    return(
      <>
      <Hero text = "Welcome to React 201"/>
      <div className= "container">
        <div className = "row">
          <div className = "col-lg-8 offset-lg-2 my-5">
            <p className = "lead">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat laborum, possimus aperiam molestias, vel aut accusantium voluptates asperiores ipsa mollitia non a quas! Ipsam commodi animi, tenetur optio distinctio obcaecati?

            </p>
          </div>
        </div>
      </div>
        </>
    )
  }

  export default Home;