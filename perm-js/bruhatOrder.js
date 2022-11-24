const { getPermutations } = require("./permutations");
const { smallNeighbors } = require("./smallNeighbors");
const { calcInversions } = require("./inversions");

const genBruhatOrder = (arrSymN) => {
  const sortedSymNByLength = [];
  arrSymN.forEach((arr) => {
    const i = calcInversions(arr);
    arr.push(smallNeighbors(arr).length);
    if (sortedSymNByLength[i]) {
      sortedSymNByLength[i] = [...sortedSymNByLength[i], arr];
    } else {
      sortedSymNByLength[i] = [arr];
    }
  });
  return sortedSymNByLength;
};

const getFalsepermArrs = (sortedSymNByLength, max_nbrs) => {
  let falsePermArrs = [];
  for (const i in sortedSymNByLength) {
    for (const j in sortedSymNByLength[i]) {
      const permArr = sortedSymNByLength[i][j];
      if (permArr[permArr.length - 1] >= max_nbrs) {
        falsePermArrs.push(permArr);
      }
    }
  }
  return falsePermArrs;
};

const b_order = genBruhatOrder(getPermutations([1, 2, 3, 4, 5]));
console.log(getFalsepermArrs(b_order, 5));
