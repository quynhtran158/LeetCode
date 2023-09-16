var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return "";
    }
    
    // Find the string with the minimum length (the limiting factor for the prefix)
    let minLen = Math.min(...strs.map(str => str.length));

    // ... Math.min function is typically used to find the minimum value among a list of numbers. The spread operator ... allows you to pass an array of numbers as if they were individual arguments to the function.

    /**
    strs.map(str => str.length): This part of the code uses the map function, which is an array method in JavaScript. The purpose of map is to transform each element of an array and create a new array based on the transformation.

(str => str.length): This is an arrow function that defines the transformation. It takes each element (in this case, a string str) from the strs array and returns its length using str.length. Essentially, it calculates the length of each string in the array.

So, strs.map(str => str.length) creates a new array containing the lengths of all the strings in the strs array. For example, if strs is ["apple", "banana", "cherry"], this part would produce [5, 6, 6]. */
    
    // Initialize the result
    let result = "";
    
    // Iterate through characters at each position
    for (let i = 0; i < minLen; i++) {
        const currentChar = strs[0][i]; // Get the current character
        
        // Check if the current character is the same in all strings
        if (strs.every(str => str[i] === currentChar)) {
            result += currentChar; // Append the character to the result
        } else {
            break; // Stop if characters are not the same in all strings
        }
    }
    
    return result;
};
