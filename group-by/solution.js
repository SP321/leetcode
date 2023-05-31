/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
  return this.reduce((x, item) => {
    const key = fn(item);
    if (!x[key]) 
      x[key] = [];
    x[key].push(item);
    return x;
  }, {});
};


/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */