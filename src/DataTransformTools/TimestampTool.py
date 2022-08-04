from datetime import date

class Timestamp:
    def __init__(self, timestamp):
        self.TS = timestamp
        
    def TimestampToFirebaseString(self):
        # Extract the month and year from the timestamp
        return {"month": self.TS.strftime("%B"), "year": self.TS.strftime("%Y")}
    
    def IsTimestampBefore(self):
        return date.today().year >= self.TS.year and date.today().month >= self.TS.month