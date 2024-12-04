class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        make a hmap and store all transactions

        iterate through all transactions and find the one which is invalid

        """
        hmap = {}
        invalidTransaction = set()
        invalidOutput = []
        for i, t in enumerate(transactions):
            name, time, amt, city = t.split(',')

            if name not in hmap:
                hmap[name] = [[i, int(time), int(amt), city]]
            else:
                hmap[name].append([i, int(time), int(amt), city])
            
        for name, transaction in hmap.items():
            for transA in hmap[name]:
                i, time, amt, city = transA

                if amt > 1000:
                    invalidTransaction.add(i)
                
                for transB in hmap[name]:
                    j, timeJ, amtJ, cityJ = transB

                    if i != j and abs(time - timeJ) <= 60 and city != cityJ:
                        invalidTransaction.add(i)
                        invalidTransaction.add(j)
        for idx in invalidTransaction:
            invalidOutput.append(transactions[idx])
        
        return invalidOutput