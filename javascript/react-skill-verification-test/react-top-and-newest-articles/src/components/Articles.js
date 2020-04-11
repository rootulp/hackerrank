import React from 'react';

function Articles (props) {
  const { articles, sortOrder } = props;
  const sortedArticles = sortArticles(sortOrder, articles)

  return (
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Upvotes</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        {sortedArticles.map((article) => {
          return <Article article={article} key={article.title} />
        })}
      </tbody>
    </table>
  );
}

function Article(props) {
  const {article} = props;

  return (<tr data-testid="article">
    <td data-testid="article-title">{article.title}</td>
    <td data-testid="article-upvotes">{article.upvotes}</td>
    <td data-testid="article-date">{article.date}</td>
  </tr>)
}

function sortArticles(sortOrder, articles) {
  if (sortOrder === "VOTES") {
    return articles.sort((a, b) => a.upvotes - b.upvotes).reverse()
  } else if (sortOrder === "DATE") {
    return articles.sort((a, b) => a.date.localeCompare(b.date)).reverse()
  }
}

export default Articles;
