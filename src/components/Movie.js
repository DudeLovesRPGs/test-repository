import Hero from "./Hero";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
const Movie = () => {
  const { id } = useParams();
  const [movieDetails, setMovieDetails] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    console.log(`Make an api request to id ${id}`);
    fetch(
      `https://api.themoviedb.org/3/movie/${id}?api_key=63aac700c9d4670d0769bd58d6fec0ae`
    )
      .then((response) => response.json())
      .then((data) => {
        setMovieDetails(data);
        setIsLoading(false);
      });
  }, [id]);

  function renderMovieDetails() {
    if (isLoading) {
      return <Hero text="Loading..." />;
    }

    if (movieDetails) {
      //What happens if there's a missing image?
      if (movieDetails.poster_path == null) {
        const posterPath =
          "https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg";
        const backdropUrl =
          "https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg";

        return (
          <>
            <Hero text={movieDetails.original_title} backdrop={backdropUrl} />;
            <div className="container my-5">
              <div className="row">
                <div className="col-md-3">
                  <img
                    src={posterPath}
                    alt="..."
                    className="img-fluid shadow rounded"
                  />
                </div>

                <div className="col-md-9">
                  <h2>{movieDetails.original_title}</h2>
                  <p className="leqad">{movieDetails.overview}</p>
                </div>
              </div>
            </div>
          </>
        );
      } else {
        const posterPath = `https://image.tmdb.org/t/p/w500/${movieDetails.poster_path}`;
        const backdropUrl = `https://image.tmdb.org/t/p/original${movieDetails.backdrop_path}`;
        return (
          <>
            <Hero text={movieDetails.original_title} backdrop={backdropUrl} />;
            <div className="container my-5">
              <div className="row">
                <div className="col-md-3">
                  <img
                    src={posterPath}
                    alt="..."
                    className="img-fluid shadow rounded"
                  />
                </div>

                <div className="col-md-9">
                  <h2>{movieDetails.original_title}</h2>
                  <p className="leqad">{movieDetails.overview}</p>
                </div>
              </div>
            </div>
          </>
        );
      }
    }
  }
  return renderMovieDetails();
};

export default Movie;
