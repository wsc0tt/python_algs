class Solution(object):
    def lemonadeChange(self, bills):
        change = []
        for bill in bills:
            if bill == 5:
                change.append(bill)
            elif bill == 10:
                if 5 in change:
                    change.append(bill)
                    change.remove(5)
                else:
                    return False
            elif bill == 20:
                if 5 in change and 10 in change:
                    change.append(20)
                    change.remove(5)
                    change.remove(10)
                elif change.count(5) >= 3:
                    change.append(20)
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
                else:
                    return False
            else:
                return False
        return True
      
    def lemonadeChangeBetter(self, bills):
        if bills[0] != 5:
            return False
        
        five_dollers = 0
        ten_dollers = 0

        for x in bills:
            if x == 5:
                five_dollers += 1
            elif x == 10:
                if five_dollers > 0:
                    five_dollers -= 1
                else:
                    return False
                ten_dollers += 1
            else:
                if five_dollers > 0 and ten_dollers > 0:
                    five_dollers -= 1
                    ten_dollers -= 1
                elif five_dollers > 2 :
                    five_dollers -= 3
                else:
                    return False
            print(five_dollers, ten_dollers)
        return True
