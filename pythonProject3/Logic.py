class logic:
    def __init__(self):
        self.AllPlace = []
    def initPlace(self):
        alltags = []

        from PlaceData import create_m
        self.AllPlace = create_m()

        for i in self.AllPlace:
            for j in i.tag:
                if not (j in alltags):
                    alltags.append(j)
        return alltags

    def findplace(self, m):
        veight = {}
        maxx = 0
        id_m = -1

        for i in self.AllPlace:
            scope = 0
            for j in m:
                if j in i.tag:
                    scope+=1
            veight[i.id] = scope

        for i in veight.keys():
            if veight[i]>maxx:
                maxx = veight[i]
                id_m = i
        return (f"pic/{self.AllPlace[id_m].name}.png", self.AllPlace[id_m].placename, self.AllPlace[id_m].des)
