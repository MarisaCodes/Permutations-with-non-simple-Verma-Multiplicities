const genPermFromArr = (arr) => {
  let perm = {};
  for (const key in arr) {
    Object.assign(perm, { [Number(key) + 1]: arr[key] });
  }
  return perm;
};

const smallNeighbors = (arr) => {
  const perm = genPermFromArr(arr);
  let arrSmallNbrs = [];

  for (const i in perm) {
    for (const j in perm) {
      if (Number(j) <= Number(i)) {
        continue;
      } else {
        const tau = arr.slice(Number(i), Number(j) - 1);
        if (!tau.length) {
          perm[i] > perm[j]
            ? arrSmallNbrs.push({ ...perm, [i]: perm[j], [j]: perm[i] })
            : null;
        } else {
          let conditionBool;
          for (let m = 0; m < tau.length; m++) {
            if (perm[i] < perm[j]) {
              conditionBool = false;
              break;
            } else {
              if (tau[m] > perm[i] || tau[m] < perm[j]) {
                conditionBool = true;
              } else {
                conditionBool = false;
                break;
              }
            }
          }
          if (conditionBool) {
            arrSmallNbrs.push({ ...perm, [i]: perm[j], [j]: perm[i] });
          }
        }
      }
    }
  }
  return arrSmallNbrs;
};

console.log(smallNeighbors([3, 2, 4, 1]).length);

module.exports = { smallNeighbors, genPermFromArr };
