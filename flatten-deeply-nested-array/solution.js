/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = (arr, n) =>
    n ?
        arr.reduce(
            (temp, next) => (
                Array.isArray(next) ?
                    temp.push(...flat(next, n - 1)) :
                    temp.push(next),
                temp
            ),
            []
        ) :
        arr;