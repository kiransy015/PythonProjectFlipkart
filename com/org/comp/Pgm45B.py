class circle:
    pie = 3.142

    def __init__(self,r):
        self.radius = r

    def area_of_circle(self):
        area = circle.pie*self.radius*self.radius
        print("Area of a circle is",area)

    def circ_of_circle(self):
        circ = 2*circle.pie*self.radius
        print("Crc of circle is",circ)

    def diameter_of_circle(self):
        diameter = 2*self.radius
        print("Diameter of circle is",diameter)

    print("---------------------------")

c1 = circle(3.5)
c1.area_of_circle()
c1.circ_of_circle()
c1.diameter_of_circle()

c2 = circle(4.5)
c2.area_of_circle()
c2.circ_of_circle()
c2.diameter_of_circle()

c3 = circle(5.5)
c3.area_of_circle()
c3.circ_of_circle()
c3.diameter_of_circle()

