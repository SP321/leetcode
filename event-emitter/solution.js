class EventEmitter {
    cb = {};
    
    subscribe(event, ele) {
        if (this.cb[event])
            this.cb[event].push(ele);
        else
            this.cb[event] = [ele];

        return {
            unsubscribe: () => {
                if (this.cb[event] && this.cb[event].length > 1)
                    this.cb[event].pop();
                else
                    delete this.cb[event];
            },
        };
    }

    emit(event, args = []) {
        if (this.cb[event])
            return this.cb[event].map(ele => ele(...args));
        
        return [];
    }
}
/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */