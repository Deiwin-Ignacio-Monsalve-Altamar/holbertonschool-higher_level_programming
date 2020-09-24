#!/usr/bin/node
/* adds a LI element to a list when the user clicks */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
