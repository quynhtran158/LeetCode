class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l, r = 0, len(people)-1
        sum = people[l] + people[r]
        people.sort()

        while l <= r:
            sum = people[l] + people[r]

            if sum <= limit: #If true, they can share a boat. Move the l pointer to the next lightest person.
                l += 1
            r -= 1 # Whether they can share a boat or not, move the r pointer to the next heaviest person.
            boat += 1

        return boat
