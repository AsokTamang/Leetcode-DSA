class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const first=[...s].sort().join('');
         const second=[...t].sort().join('');
         return first===second;

            
      

    }
}

const ans=new Solution();
console.log(ans.isAnagram('jar','raj'));
console.log(ans.isAnagram('first','raj'));
