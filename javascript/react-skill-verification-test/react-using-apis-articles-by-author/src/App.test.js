import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { render, fireEvent, cleanup, wait } from '@testing-library/react';

import fetchMock from 'fetch-mock';

import 'jest-dom/extend-expect';

const renderApp = () => render(<App />);

const testIds = {
  textInput: "text-input",
  fetchButton: "fetch-button",
  resultRow: "result-row",
  noResults: "no-results",
};

beforeEach(() => {
});

afterEach(() => {
  // restore fetch() to its native implementation
  fetchMock.restore();
  cleanup();
});

test('Initial UI renders correctly', () => {
  const { getByTestId, queryByTestId, queryAllByTestId } = renderApp();

  const textInput = getByTestId(testIds.textInput);
  expect(textInput).toBeVisible();
  expect(textInput).toHaveValue("");

  const fetchButton = getByTestId(testIds.fetchButton);
  expect(fetchButton).toBeVisible();

  const results = queryAllByTestId(testIds.resultRow);
  expect(results).toHaveLength(0);

  expect(queryByTestId(testIds.noResults)).toBeNull();
});


test('Test with non existing author', async () => {
  const { getByTestId, queryAllByTestId } = renderApp();

  const textInput = getByTestId(testIds.textInput);
  const fetchButton = getByTestId(testIds.fetchButton);

  const author = 'foo';
  const url = `https://jsonmock.hackerrank.com/api/articles?author=${author}&page=1`;
  fetchMock.getOnce(url, JSON.stringify({ page:1,per_page:10,total:0,total_pages:0,data:[]}));
  fireEvent.change(textInput, { target: { value: author }});
  fireEvent.click(fetchButton);

  await wait(() => {
    const results = queryAllByTestId(testIds.resultRow);
    expect(results).toHaveLength(0);

    const noResults = getByTestId(testIds.noResults);
    expect(noResults).toBeVisible();
    expect(noResults).toHaveTextContent('No results');
  });
});

test('Test with existing author', async () => {
  const { getByTestId, queryByTestId, queryAllByTestId } = renderApp();

  const textInput = getByTestId(testIds.textInput);
  const fetchButton = getByTestId(testIds.fetchButton);

  const author = 'johndoe';
  const url = `https://jsonmock.hackerrank.com/api/articles?author=${author}&page=1`;
  fetchMock.getOnce(url, JSON.stringify({
    page:1,per_page:10,total:0,total_pages:0,data:[
      {title: "Title 1"},
      {title: null},
      {title: "Some Title 3"},
      {title: "Title 4"},
      {title: "title 5"},
    ]}));
  fireEvent.change(textInput, { target: { value: author }});
  fireEvent.click(fetchButton);

  await wait(() => {
    const results = queryAllByTestId(testIds.resultRow);
    const expectedTitles = ["Title 1", "Some Title 3", "Title 4"];
    expect(results.map(result => result.textContent)).toEqual(expectedTitles);

    expect(queryByTestId(testIds.noResults)).toBeNull();
  });
});
