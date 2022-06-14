class Creature:
    
    COEFF_STRENGHT_ON_ENERGY_CONSUPTION = 3
    COEFF_MAXPOINT_ON_ENERGY_CONSUPTION = 2
    
    COEFF_STRENGHT_ON_WATER_CONSUPTION = 3
    COEFF_MAXPOINT_ON_WATER_CONSUPTION = 2
    
    def __init__(self,x,y,max_health,max_energy,max_water,speed,strenght):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.max_energy = max_energy
        self.max_water = max_water
        
        self.health = max_health
        self.energy = max_energy
        self.water = max_water
        
        self.speed = speed
        self.strenght = strenght
        self.energy_consuption = self.COEFF_MAXPOINT_ON_ENERGY_CONSUPTION * self.max_health + self.COEFF_STRENGHT_ON_ENERGY_CONSUPTION
        self.water_consuption = self.COEFF_MAXPOINT_ON_WATER_CONSUPTION * self.max_water + self.COEFF_STRENGHT_ON_ENERGY_CONSUPTION
        
    def move(self,translation_x,translation_y):
        self.x += translation_x
        self.y += translation_y
    
    def modify_health(self,modification):
        self.health = (self.health +  modification) if (self.health + modification) < self.max_health else self.max_health
    
    def modify_water(self,modification):
        self.water = (self.water + modification) if (self.water + modification) < self.max_water else self.max_water
        
    def modify_energy(self,modification):
        self.energy = (self.energy + modification) if (self.energy + modification) < self.max_energy else self.max_energy
        
    