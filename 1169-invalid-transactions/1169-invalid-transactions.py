class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        validTransaction = defaultdict(list)
        invalid = []
        for transaction in transactions:
            user, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                invalid.append(transaction)
            elif user in validTransaction:
                # 50 - 20 = 30
                if time - validTransaction[user][0][-1] <= 60 and validTransaction[user][1][-1] != city:
                    invalid.append(transaction)
                    while (validTransaction[user][0] and time - validTransaction[user][0][-1] <= 60 and validTransaction[user][1][-1] != city):                        
                        invalid.append(validTransaction[user][2].pop())
                        validTransaction[user][0].pop()
                        validTransaction[user][1].pop()
                        
                else:
                    validTransaction[user][0].append(time)
                    validTransaction[user][1].append(city)
                    validTransaction[user][2].append(transaction)

            else:
                validTransaction[user].append([])
                validTransaction[user].append([])
                validTransaction[user].append([])
                validTransaction[user][0].append(time)
                validTransaction[user][1].append(city)
                validTransaction[user][2].append(transaction)

        return sorted(invalid, key=lambda x: int(x.split(",")[1]))
            


