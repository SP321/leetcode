class MinStack {
public:
    stack<int>mi;
    stack<int>a;
    MinStack() {
        mi.push(INT_MAX);
    }
    
    void push(int val) {
        if(val<=mi.top())
            mi.push(val);
        a.push(val);
    }
    
    void pop() {
        if(a.top()==mi.top())
            mi.pop();
        a.pop();
    }
    
    int top() {
        return a.top();
    }
    
    int getMin() {
        return mi.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */