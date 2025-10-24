//Top K Frequent Elements
//Given an integer array nums and an integer k, return the k most frequent elements within the array.

//The test cases are generated such that the answer is always unique.

//You may return the output in any order.

//Example 1:

//Input: nums = [1,2,2,3,3,3], k = 2

//Output: [2,3]
//Example 2:

//Input: nums = [7,7], k = 1

//utput: [7]

class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  topKFrequent(nums, k) {
    const store = new Map(); //we are creating a map to store the key value pair of the number and its number of appearance as a value.
    const keys = []; //this is an array which stores the number whose count matches with the k.
    for (let num of nums) {
      store.set(num,(store.get(num)||0)+1)   //here we are directly setting the num's freq using set method if store.get(num) is undefined then we set it to 0 and add 1.
    } //then this loop is done whose role is for counting the numebr of appearance of a numeber and storing as a key-value pair in a map.

    

    return keys;
  }
}


console.log(new Solution().topKFrequent([1,2,2,3,3,3,4,5],2));
