#!/usr/bin/node

const { argv } = process;
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
if (!isNaN(num1) && !isNaN(num2)) {
  add(num1, num2);
} else {
  console.log('NaN');
}
