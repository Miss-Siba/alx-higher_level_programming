#!/usr/bin/node

const { argv } = process;
const size = parseInt(argv[2]);

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
