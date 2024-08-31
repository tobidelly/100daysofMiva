/* import React from 'react'; */
import './App.css';
import Accordian from './components/Accordian';
import RandomColor from './components/random-color';
import StarRating from './components/star-rating';
import ImageSlider from './components/image-slider';
import LoadMoreData from './components/load-more-data';
import TreeView from './components/simple-tree-view';

function App() {
  return (
    <div className="App">
      <header>
        <h1>25 React Projects for #100daysofMiva</h1>
      </header>
      <Accordian />
      <RandomColor />
      <StarRating />
      <ImageSlider url={'https://picsum.photos/v2/list'} limit={'10'}/>
      <LoadMoreData />
      <TreeView />
    </div>
  );
}

export default App;