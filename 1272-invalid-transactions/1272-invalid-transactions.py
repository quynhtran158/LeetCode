'''
question:
what is the type of amount, time? str or int?


we need to group the transac share the same name to check the 2nd condition
- once group:  compare the transaction
- when both transaction has same name, diff 60 time and diff city => both invalid

plan:
- group all transac by ppl name, hash table
- each transac check if violate the amount rule 
- each transac compare with other transac to check time and city 
- have a set to avoid duplicate invalid transact. a transact can be invalid in multiple ways or match with multiple other transact 

+ key: name, val: list of transaction
+ set of idx to store the invalid transact
+ split the value by comma
+ store in hash table as tuple 
+ check invalid condition
    + if amount > 1000
    + iterate thru transact w same name for t, c, j in d[name]
        + if city are diff
        + time <= 60
        + if condiation meet, mark both transact 



'''
from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #key name, val list of tuple time city idx
        transactionByName = defaultdict(list)
        invalidIndex = set()

        for index, transaction_str in enumerate(transactions):
            name, time_str, amount_str, city = transaction_str.split(",")
            time = int(time_str)
            amount = int(amount_str)
            transactionByName[name].append((time, city, index))
            if amount > 1000:
                invalidIndex.add(index)
            #iterate all transaction tuple with the key as name (mtv once, beijing second)
            for prev_time, prev_city, prev_index in transactionByName[name]:
                if prev_city != city and abs(time-prev_time) <= 60:
                    invalidIndex.add(index)
                    invalidIndex.add(prev_index)
        return [transactions[i] for i in invalidIndex]


        