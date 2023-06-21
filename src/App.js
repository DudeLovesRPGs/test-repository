import "./App.css";
import { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Search from "./components/Search";
import Movie from "./components/Movie";
import NotFound from "./components/NotFound";
import { Switch, Route } from "react-router-dom";

function App() {
  const[searchResults, setSearchResults] = useState([]);
  const[searchText, setSearchText] = useState('');

  useEffect(() =>{
    if(searchText){
      fetch(`https://api.themoviedb.org/3/search/movie?query=${searchText}&api_key=63aac700c9d4670d0769bd58d6fec0ae`)
      .then(response => response.json())
      .then(data => {
        setSearchResults(data.results)
      })
    }
  }, [searchText])

      


  return (
    <div>
      <Navbar searchText = {searchText} setSearchText ={setSearchText} />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        {/* <Route path="/search" component={Search} keyword = {searchText} searchResults = {searchResults} /> */}
        <Route path = "/search">
          <Search keyword = {searchText} searchResults = {searchResults} />
        </Route>
        <Route path="/movies/:id" component={Movie} />
        <Route path = '*' component = {NotFound}/>

      </Switch>
    </div>
  );
}

export default App;
