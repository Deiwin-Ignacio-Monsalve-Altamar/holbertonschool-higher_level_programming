#!/usr/bin/node
/*  */
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let contents = body;
    let fs = require('fs');
    fs.writeFile(process.argv[2], contents, 'utf-8', (err) =>{
        if(err){
            console.log(err)
        }
    })    
}
});