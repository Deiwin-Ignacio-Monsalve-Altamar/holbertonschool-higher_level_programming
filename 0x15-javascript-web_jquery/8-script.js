#!/usr/bin/node
/* script that fetches and lists all movies title by using this URL */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const films = data.results;
  for (let i = 0; i < films.length; ++i) {
    $('#list_movies').append(`<li>${films[i].title}</li>`);
  }
});
