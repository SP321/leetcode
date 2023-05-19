/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    async function asyncfunc() {
        if (functions.length === 0) return;
        const fn = functions.shift();
        await fn();
        await asyncfunc();
    }
    const nPromises = Array(n).fill().map(asyncfunc);
    await Promise.all(nPromises);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */