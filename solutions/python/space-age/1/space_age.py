class SpaceAge:
    def __init__(self, seconds):
        self.age_in_seconds = seconds
        self.age_on_earth = (seconds/31557600)
        self.age_on_mercury = self.age_on_earth/0.2408467
        self.age_on_venus = self.age_on_earth/0.61519726
        self.age_on_mars = self.age_on_earth/1.8808158
        self.age_on_jupiter = self.age_on_earth/11.862615
        self.age_on_saturn = self.age_on_earth/29.447498
        self.age_on_uranus = self.age_on_earth/84.016846
        self.age_on_neptune = self.age_on_earth/164.79132
    def on_earth(self):
        return round(self.age_on_earth,2)
    def on_mercury(self):
        return round(self.age_on_mercury,2)
    def on_venus(self):
        return round(self.age_on_venus,2)
    def on_mars(self):
        return round(self.age_on_mars,2)
    def on_jupiter(self):
        return round(self.age_on_jupiter,2)
    def on_saturn(self):
        return round(self.age_on_saturn,2)
    def on_uranus(self):
        return round(self.age_on_uranus,2)
    def on_neptune(self):
        return round(self.age_on_neptune,2)
        
