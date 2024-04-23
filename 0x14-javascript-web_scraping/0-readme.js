#!/usr/bin/node
const fs = require('fs');
const util = require('util');

function readAndPrintFile(filePath) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error occurred while reading the file: ${err}');
        } else {
            console.log(data);
        }
    });
}

if (process.argv.length !== 3) {
    console.log('Usage: node script_name.js file_path');
} else {
    const filePath = process.argv[2];
    readAndPrintFile(filePath);
}

