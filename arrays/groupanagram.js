//Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

//An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
//Input: strs = ["act","pots","tops","cat","stop","hat"]
//Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


class Solution {
    groupAnagrams(strs){
        const store=new Map();
        for (let word of strs){
            const key=word.split('').sort().join();   //here we are spliting each word and sorting them and joining them as the anagrams words have same sorted word which we will use as a key in our mapstore
            if(!store.has(key)){
                store.set(key,[]);     //if our map store doesnot has a sorted word of the current indexed word as a key then we set it as a key with an empty array as a value.
            }
          
            // then for each word we get that key and push the word in the value form.
            store.get(key).push(word); 
        }
        return Array.from(store.values());   //then we return the array form of all the values of our map store.

    }
}
console.log(new Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]));