class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = []
        dire_queue = []
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        while radiant_queue and dire_queue:
            radiant_senator = radiant_queue.pop(0)
            dire_senator = dire_queue.pop(0)
            if radiant_senator < dire_senator:
                radiant_queue.append(radiant_senator + len(senate))
            else:
                dire_queue.append(dire_senator + len(senate))
        return "Radiant" if radiant_queue else "Dire"
