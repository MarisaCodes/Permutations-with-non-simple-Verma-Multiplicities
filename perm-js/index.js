const getPermutations = (arr) => {
  const output = [];

  const swapInPlace = (arrToSwap, indexA, indexB) => {
    const temp1 = arrToSwap[indexA];
    arrToSwap[indexA] = arrToSwap[indexB];
    arrToSwap[indexB] = temp1;
  };

  const generate = (n, heapArr) => {
    if (n === 1) {
      output.push(heapArr.slice());
      return;
    }

    generate(n - 1, heapArr);

    for (let i = 0; i < n - 1; i++) {
      if (n % 2 === 0) {
        swapInPlace(heapArr, i, n - 1);
      } else {
        swapInPlace(heapArr, 0, n - 1);
      }

      generate(n - 1, heapArr);
    }
  };

  generate(arr.length, arr.slice());

  return output;
};

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

const genSymGroup = (groupArr) => {
  let symArr = [];
  groupArr.forEach((arr) => {
    symArr.push(genPermFromArr(arr));
  });
  return symArr;
};
const calcInversions = (arr) => {
  const perm = genPermFromArr(arr);
  let inversions = 0;
  for (const i in perm) {
    for (const j in perm) {
      if (Number(j) >= Number(i)) {
        break;
      } else {
        perm[j] > perm[i] ? (inversions += 1) : null;
      }
    }
  }
  return inversions;
};
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
const arrs = getFalsepermArrs(b_order, 5);
function createEls(arr, i) {
  const div = document.createElement("div");
  div.innerHTML = `<div id=div_${i} class="value">
  (${arr.slice(0, arr.length - 1)}) &rightarrow; ${arr[arr.length - 1]}
  </div>

  <div id=remove_${i}>
    <textarea cols="50" rows="10"></textarea>
    <button id=btn_${i}>submit</button>
  </div>
  `;
  document.body.appendChild(div);
}
let i = 0;
arrs.forEach((arr) => {
  i += 1;
  createEls(arr, i);
});

document.addEventListener("click", (event) => {
  event.preventDefault();
  if (event.target.tagName === "BUTTON") {
    const id = event.target.id.slice(4);
    const input = document
      .getElementById(`remove_${id}`)
      .querySelector("textarea")
      .value.trim();
    document
      .getElementById(`div_${id}`)
      .insertAdjacentHTML("beforeend", `&rightarrow; ${input}`);
    document.getElementById(`remove_${id}`).remove();
  }
});
