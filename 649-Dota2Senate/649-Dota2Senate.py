# Last updated: 6/22/2025, 7:16:00 PM
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        rq = deque()
        dq= deque()

        s = list(senate)

        for index, char in enumerate(s):
            if char == 'R':
                rq.append(index)
            else:
                dq.append(index)
        
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()

            if r < d:
                rq.append(r + len(senate))
            else: 
                dq.append(d + len(senate))
        
        return "Radiant" if rq else "Dire"