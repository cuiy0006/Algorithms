/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
struct MaxStack {
    values: Vec<i32>,
}

impl MaxStack {

    fn new() -> Self {
        MaxStack {
            values: Vec::new(),
        }
    }
    
    fn push(&mut self, x: i32) {
        self.values.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        self.values.pop().unwrap()
    }
    
    fn top(&self) -> i32 {
        *self.values.last().unwrap()
    }
    
    fn peek_max(&self) -> i32 {
        *self.values.iter().max().unwrap()
    }
    
    fn pop_max(&mut self) -> i32 {
        let max = self.peek_max();
        for i in (0..self.values.len()).rev() {
            if self.values[i] == max {
                return self.values.remove(i)
            }
        }
        unimplemented!()
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * let obj = MaxStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.peek_max();
 * let ret_5: i32 = obj.pop_max();
 */
