#!/usr/bin/node

const args = process.argv;

function bubbleSort (list) {
  for (let i = 0; i < list.length - 1; i++) {
    for (let j = 0; j < list.length - 1; j++) {
      if (list[j] < list[j + 1]) {
        const temp = list[j];
        list[j] = list[j + 1];
        list[j + 1] = temp;
      }
    }
  }
}

if (args.length <= 3) {
  console.log(0);
} else {
  /* copy array and convert to number */
  const newArr = [];

  for (let i = 2, j = 0; j < args.length - 2; i++, j++) {
    newArr[j] = parseInt(args[i]);
  }

  bubbleSort(newArr);
  console.log(newArr[1]);
}
