# Last updated: 6/22/2025, 7:15:59 PM
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        output = []

        for asteroid in asteroids:
            if asteroid > 0:
                output.append(asteroid)
            
            if asteroid < 0:
                while output and output[-1] > 0 and abs(asteroid) > abs(output[-1]):
                    output.pop()
                if output and output[-1] > 0 and abs(asteroid) == abs(output[-1]):
                    output.pop()
                elif not output or output[-1] < 0:
                    output.append(asteroid)
            
        return output