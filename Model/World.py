class World:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.creature_list = []
        
    def addCreature(self,creature):
        self.creature_list.append(creature)