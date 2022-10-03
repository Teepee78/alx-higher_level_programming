#!/usr/bin/node

const args = process.argv;
const num = Math.floor(Number(args[2]));

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
