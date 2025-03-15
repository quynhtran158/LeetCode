class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Base case: 1st row is always 1
        if rowIndex == 0:
            return [1]
        
        # Get the previous row using recursion
        prev_row = self.getRow(rowIndex - 1)
        
        row = [1]  #1st element is always 1
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])  # Sum of two numbers above
        row.append(1)  # Last element is always 1
        
        return row