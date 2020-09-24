#!/usr/bin/node
/* updates the text of the HTML tag HEADER to “New Header!!!” */

$('DIV#update_header').click(function () {
  $('header').text('New Header');
});
