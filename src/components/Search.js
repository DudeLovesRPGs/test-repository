import Hero from "./Hero";
import {Link} from "react-router-dom";

const MovieCard = ({ movie }) => {
  const posterURL = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
  const detailUrl = `/movies/${movie.id}`
  return (
    <div className="col-lg-3 col-md-3 col-2 my-4">
      <div className="card">
        <img
          src={posterURL}
          className="card-img-top"
          alt={movie.original_title}
        />
        <div className="card-body">
          <h5 className="card-title">{movie.original_title}</h5>
          <Link to ={detailUrl} className="btn btn-primary">Show details</Link>
        </div>
      </div>
    </div>
  );
};

//TMDB API Key: 63aac700c9d4670d0769bd58d6fec0ae

const Search = ({ keyword, searchResults }) => {
  const title = `You are searching for ${keyword}`;
  const resultsHTML = searchResults.map((obj, i) => {
    return <MovieCard movie={obj} key={i} />;
  });
  
  if(resultsHTML.length ==0){
    return(
      <>
    <Hero text = "There are no search results..."/>
    </>)
  }
  else{
  return (
    <>
      <Hero text={title} />
      {resultsHTML && (
        <div className="container">
          <div className="row">{resultsHTML}</div>
        </div>
      )}
    </>
  );
  
}
};

export default Search;
