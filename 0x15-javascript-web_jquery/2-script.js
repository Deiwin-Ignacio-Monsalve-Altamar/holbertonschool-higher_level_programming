#!/usr/bin/node
/*  updates the text (#FF0000) user clicks ag DIV#red_header */

$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
