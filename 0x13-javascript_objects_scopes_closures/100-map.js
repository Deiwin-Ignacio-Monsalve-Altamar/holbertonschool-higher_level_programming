#!/usr/bin/node
const mapped = require('./100-data').list;

function print (list) {
  console.log(list);

  const mapeado = list.map((val, idx) => idx * val);
  console.log(mapeado);
}

print(mapped);
