function checkAnagram(a: string, b: string) {
    if(a.length !== b.length) {
        return false;
    }
    const storeA = new Map<string, number>();
    for(const i of a) {
        const val = storeA.get(i);
        if(val) {
            storeA.set(i, val + 1);
        } else {
            storeA.set(i, 1);
        }
    }
    const storeB = new Map<string, number>();
    for(const i of b) {
        const val = storeB.get(i);
        if(val) {
            storeB.set(i, val + 1);
        } else {
            storeB.set(i, 1);
        }
    }

    const storeALen = storeA.size,
    storeBLen = storeB.size;
    if(storeALen !== storeBLen) {
        return false;
    }
    
    const keys = [...storeA.keys()]
    for(let i = 0; i < storeALen; i++) {
        const key = keys[i];
        if(storeA.get(key) !== storeB.get(key)) {
            return false;
        }
    }
    return true;
}