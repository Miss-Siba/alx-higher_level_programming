#!/usr/bin/node

const { argv } = process;
const [,, arg0] = argv;

if (!arg0) {
  console.log('No argument');
} else {
  console.log(arg0);
}
