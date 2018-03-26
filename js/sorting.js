let MAX_NUM = 20;
let rand = () => Math.floor(Math.random() * MAX_NUM) + 1;
let genIntArray = (n) => Array.from({length: n}, () => rand());
let sortIntArray = (arr) => { return arr.sort((a, b) => a-b); };

// define sorting functions
var bubbleSort = (arr) => { return arr; };
var insertionSort = (arr) => { return arr; };


// bubble sort
bubbleSort = (arr) => {
  for(let i=0; i<arr.length; i++) {
    for (let j=i+1; j<arr.length; j++) {
      if (arr[i] > arr[j]) {
        let tmp = arr[j];
        arr[j] = arr[i];
        arr[i] = tmp;
      }
    }
  }
  return arr;
};

// insertion sort
insertionSort = (arr) => {

}


// test cases
let assert = require('assert');
describe('#sorting algorithms', () => {
  let arr = [];
  let expect = [];

  beforeEach(() => {
    arr = genIntArray(10);
    expect = sortIntArray(arr.slice());
  });

  it('bubble sort', () => {
    console.log('array:', arr);
    console.log('expect:', expect);
    console.time('bubble');
    let result = bubbleSort(arr);
    console.timeEnd('bubble')
    console.log('bubble: ', result);
    assert.deepEqual(arr, expect);
  });

  it('insertion sort', () => {
    console.log('array:', arr);
    console.log('expect:', expect);
    console.time('insertion');
    let result = insertionSort(arr);
    console.timeEnd('insertion')
    console.log('insertion: ', result);
    assert.deepEqual(arr, expect);
  });
});

