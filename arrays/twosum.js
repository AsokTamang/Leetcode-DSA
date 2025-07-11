//Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

//You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target                                     //4   i=3   j=3
   * @return {number[]}
   */
  twoSum(nums, target) {
    const storage = new Map(); //this stores the datas in key-value pair
    for (let i = 0; i < nums.length; i++) {
      //here first of all we are looping through each nums in an array.
      const required = target - nums[i]; //then we are subtracting the target value with the num value  in each index of arrray to get the required num value
      if (storage.has(required)) {
        //if our map store has the required num value then we get its index aand ofcourse we have the index of our calculating num value from for loop
        return [storage.get(required), i]; //then we return the indices as asked by the question.
      }
      storage.set(nums[i], i); //if our map store doesnot has the required num value then we set the current calculating num value with its index for future calculation.
    }
    return [];
  }
}

const ans = new Solution();
console.log(ans.twoSum([1, 3, 4, 5], 4));
console.log(ans.twoSum([1, 3, 4, 5], 30));
