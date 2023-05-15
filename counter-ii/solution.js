/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
class Counter {
  constructor(n) {
    this.n=n;
    this.nn=n;
  }
  decrement(){
      return --this.n;
  }
  reset(){
      return this.n=this.nn;
  }
  increment(){
      return ++this.n;
  }
}
var createCounter = function(n) {
    return new Counter(n);
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */