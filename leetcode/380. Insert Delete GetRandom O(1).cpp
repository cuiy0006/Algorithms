class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(m.find(val) != m.end()){
            return false;
        }
        v.push_back(val);
        m[val] = v.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(m.find(val) == m.end()){
            return false;
        }
        int idx = m[val];
        int num = v[v.size() - 1];
        
        m[num] = idx;
        m.erase(val);

        v[idx] = num;
        v.pop_back();
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int idx = rand() % v.size();
        return v[idx];
    }
    
private:
    unordered_map<int, int> m;
    vector<int> v;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
