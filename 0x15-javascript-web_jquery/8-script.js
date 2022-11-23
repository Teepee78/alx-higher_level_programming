const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, (response, status) => {
  if (status === 'success') {
    const results = response.results;

    for (const result of results) {
      $('UL#list_movies').append(`<li>${result.title}</li>`);
    }
  }
});
