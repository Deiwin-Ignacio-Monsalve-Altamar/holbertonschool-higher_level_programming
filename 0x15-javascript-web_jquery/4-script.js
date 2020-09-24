#!/usr/bin/node
/* toggles the class of the HTML tag HEADER */
$('#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
