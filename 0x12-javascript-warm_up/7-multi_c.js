#!/usr/bin/node

const { argv } = process;
const num = parseInt(argv[2]);

if (!isNaN(num)) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
