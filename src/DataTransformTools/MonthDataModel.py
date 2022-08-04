from collections import deque
from collections import defaultdict

class MonthDataDictionary:
    def __init__(self):
        self.daytimeobj = defaultdict(lambda: deque())
        for day in range(1, 32):
            self.daytimeobj[str(day)]
            
    def AddData(self, day, config):
        self.daytimeobj[day].append(config)
        
    def GetMonthDataDict(self):
        return self.daytimeobj