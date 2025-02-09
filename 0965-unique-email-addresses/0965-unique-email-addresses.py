class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
        have 2 pointer starts at beginning of 2 email in the list and check the emails at the same time
        if we see "." simply skip over the "."
        if we see the "+", jump right to the domain after @

        if see @, check the email in reversed 
        
        '''
        uniqueEmail = set()
    
        for email in emails:
            cleanLocal = []
            for currChar in email:
                if currChar == "+" or currChar == "@":
                    break
                if currChar != ".":
                    cleanLocal.append(currChar)
            
            domain = []
            for currChar in reversed(email):
                domain.append(currChar)
                if currChar == "@":
                    break
                
            
            cleanLocal = "".join(cleanLocal)
            domain = "".join(domain[::-1])
            uniqueEmail.add(cleanLocal + domain)
        return len(uniqueEmail)
                