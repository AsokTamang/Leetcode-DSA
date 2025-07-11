

class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    let storage=new Set();
    for (let num of nums){
        if(storage.has(num)) return true;
        storage.add(num);
    }
    return false;
      

    }
}

const ans=new Solution();
console.log(ans.hasDuplicate([1,2,3,4]));
console.log(ans.hasDuplicate([1,2,3,2]));
