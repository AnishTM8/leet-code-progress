# Last updated: 6/25/2025, 9:21:56 AM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif  i % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))

        return res