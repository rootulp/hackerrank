import React, { Component } from 'react';
import './App.css';

import Articles from './components/Articles';

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {sortOrder: "VOTES"}
  }

  handleTopClick = () => {
    this.setState({sortOrder: "VOTES"})
  }

  handleNewestClick = () => {
    this.setState({sortOrder: "DATE"})
  }

  render() {
    const { articles } = this.props;
    const { sortOrder } = this.state;

    return (
      <div className="App">
        <div className="navigation">
          <button data-testid="top-link" onClick={this.handleTopClick}>Top</button>
          <button data-testid="newest-link" onClick={this.handleNewestClick}>Newest</button>
        </div>
        <Articles articles={articles} sortOrder={sortOrder} />
      </div>
    );
  }
}

export default App;
