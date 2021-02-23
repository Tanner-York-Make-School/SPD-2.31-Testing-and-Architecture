"""
By Kami Bigdely
Refactored by Tanner York
Extract superclass.
"""

class Shape():
    """Class representation of a shape"""
    def __init__(self, visible=True):
        """Creates a new Shape object with the given visibility"""
        self.visible = visible

    def hide(self):
        """Makes the rectangle no longer visible"""
        self.visible = False

    def make_visible(self):
        """Make the rectangle visible"""
        self.visible = True


class Circle(Shape):
    """Class representation of a circle"""
    def __init__(self, x, y, r, visible=True):
        """
        Creates a new Circle object with the folowing info:
            center_x(int): x coord for circles center
            cener_y(int): y coord for circles center
            r(int): radius of the circle
            visible(bood): wether the circle is visible or not
        """
        super().__init__(visible)
        self.center_x = x
        self.center_y = y
        self.r = r

    def display(self):
        """Draws the circle on the canvas"""
        if self.visible:
            print('drew the circle.')

    def get_center(self):
        """Gets the circles center"""
        return self.center_x, self.center_y


class Rectangle(Shape):
    """Class representation of a rectangle"""
    def __init__(self, x, y, width, height, visible=True):
        """
        Creates a new Rectangle object with the following info:
            x(int): x coord for the rectangle left bottom corner
            y(int): y coord for rectangle left bottom corner
            width(int): width of the rectangle
            height(int): height of the rectangle
            visible(bool): wether the rectangle is visble or not
        """
        super().__init__(visible)
        # left-bottom corner.
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display(self):
        """Draws the rectangle on the canvas"""
        if self.visible:
            print('drew the rectable.')

    def get_center(self):
        """Returns the center of the rectangle"""
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.make_visible()
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())