class SpaceAge:
    def __init__(self, seconds):
        YEAR_IN_SECONDS = 31557600
        ORBITAL_PERIOD = {
            "Mercury": 0.2408467,
            "Venus": 0.61519726,
            "Earth": 1.0,
            "Mars": 1.8808158,
            "Jupiter": 11.862615,
            "Saturn": 29.447498,
            "Uranus": 84.016846,
            "Neptune": 164.79132,
        }
        self.age = seconds / YEAR_IN_SECONDS

    def on_mercury(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Mercury"]
        return round(planet_age, 2)

    def on_venus(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Venus"]
        return round(planet_age, 2)

    def on_earth(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Earth"]
        return round(planet_age, 2)

    def on_mars(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Mars"]
        return round(planet_age, 2)

    def on_jupiter(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Jupiter"]
        return round(planet_age, 2)

    def on_saturn(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Saturn"]
        return round(planet_age, 2)

    def on_uranus(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Uranus"]
        return round(planet_age, 2)

    def on_neptune(self):
        planet_age = self.age / self.ORBITAL_PERIOD["Neptune"]
        return round(planet_age, 2)
