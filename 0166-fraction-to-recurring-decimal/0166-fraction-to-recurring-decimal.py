class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return str(0)
        neg = False
        if numerator*denominator < 0:
            neg = True
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        output = ""
        if neg:
            output += "-" + str(numerator//denominator) + "."
        else:
            output += str(numerator//denominator) + "."
        num_q = []

        while True:
            rem = numerator % denominator
            if rem == 0:
                for element in num_q:
                    output += str(element[-1])
                break
            numerator = rem * 10
            q = numerator // denominator
            # print(rem, numerator, q)
            

            if [numerator, q] not in num_q:
                num_q.append([numerator, q])

            elif [numerator, q] in num_q:
                ind = num_q.index([numerator, q])
                for element in num_q[:ind]:
                    output += str(element[-1])
                
                output += "("
                for element in num_q[ind:]:
                    output += str(element[-1])
                output += ")"
                break
            # print(num_q)

        
        return output
        