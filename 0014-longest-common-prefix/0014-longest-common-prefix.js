var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return "";
    }
    
    // Find the string with the minimum length (the limiting factor for the prefix)
    let minLen = Math.min(...strs.map(str => str.length));
    
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
