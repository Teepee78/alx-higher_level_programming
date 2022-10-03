#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  /* copy array and convert to number */
  const newArr = [];

  for (let i = 2, j = 0; j < args.length - 2; i++, j++) {
    newArr[j] = parseInt(args[i]);
  }

  newArr.sort().reverse();
  console.log(newArr[1]);
}
