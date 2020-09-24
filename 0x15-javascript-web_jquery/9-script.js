#!/usr/bin/node
/* script that fetches from https://fourtonfish.com/hellosalut/?lang=fr */
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(URL, function (data) {
  $('DIV#hello').text(data.hello);
});
