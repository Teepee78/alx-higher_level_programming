const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, (response, status) => {
  if (status === 'success') {
    $('DIV#character').text(response.name);
  }
});
