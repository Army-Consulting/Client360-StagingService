class SheetLinkFacade:
    def __init__(self):
        self.links = []
    
    def capture(self):
        with open("src/LinkUtil/SheetAPILinks.txt") as e:
            for line in e:
                self.links += [line.replace("\n", "")]

    def getSheetLinks(self):
        return self.links

