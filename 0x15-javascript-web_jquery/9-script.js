const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$('document').ready(() => {
  $.get(url, (response, status) => {
    if (status === 'success') {
      $('DIV#hello').text(response.hello);
    }
  });
});
