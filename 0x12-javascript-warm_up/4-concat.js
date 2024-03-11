#!/usr/bin/node

const { argv } = process;

if (argv.length < 1) {
  console.log('undefined');
} else {
  console.log(`${argv[2]} is ${argv[3]}`);
}
