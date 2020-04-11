import React from 'react';

class Articles extends React.Component {

  constructor(props) {
    super(props);
    this.state = { articles: undefined };
  }

  fetchArticlesBy = (author) => {
    fetch(`https://jsonmock.hackerrank.com/api/articles?author=${author}&page=1`)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // console.log(data);
        if(data.data !== undefined) {
          this.setState({articles: data.data})
        }
      });
  }

  handleClick = () => {
    const author = document.getElementById("text-input").value
    this.fetchArticlesBy(author)
  }

  render() {
    const {articles} = this.state;

    return (
      <React.Fragment>
        <div className="controls">
          <div className="input-container">
            <span>author:</span>
            <input id="text-input" type="text" className="text-input" data-testid="text-input" />
            <button className="fetch-button" data-testid="fetch-button" onClick={this.handleClick}>Fetch</button>
          </div>
        </div>
        <Results articles={articles} />
      </React.Fragment>
    );
  }
}

function Results(props){
  const { articles } = props;

  if(articles === undefined) {
    return null;
  }

  if(articles.length === 0) {
    return <div data-testid="no-results">No results</div>
  }

  return (
    <div className="results">
      {articles.filter(article => article.title != null).slice(0, 3).map(article => {
        return <li key={article.title} data-testid="result-row">{article.title}</li>
      })}
    </div>
  )
}


export default Articles;
