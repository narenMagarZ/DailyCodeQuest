function containDuplicate(nums: number[]) {
    const store = new Map<number, number>()
    for(const num of nums) {
        if(store.get(num)) {
            return true;
        } else {
            store.set(num, 1);
        }
    }
    return false;
}