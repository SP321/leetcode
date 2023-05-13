class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans=[]
        for i in range(len(transactions)):
            name_i, time_i, amount_i, city_i = transactions[i].split(',')
            time_i = int(time_i)
            amount_i = int(amount_i)

            if amount_i > 1000:
                ans.append(transactions[i])
            else:
                for j in range(len(transactions)):
                    if i != j:
                        name_j, time_j, amount_j, city_j = transactions[j].split(',')
                        time_j = int(time_j)
                        amount_j = int(amount_j)

                        if name_i == name_j and abs(time_i - time_j) <= 60 and city_i != city_j:
                            ans.append(transactions[i])
                            break
        return ans