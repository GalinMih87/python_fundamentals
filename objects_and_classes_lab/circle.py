class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameret = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameret

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius * self.radius


print(f"{Circle.calculate_circumference():.2f}")
print(f"{Circle.calculate_area():.2f}")
print(f"{Circle.calculate_area_of_sector(angle):.2f}")