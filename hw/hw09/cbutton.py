# cbutton.py
#    Modified Button widget to circular instead of rectangular.

from graphics import *

class CButton:

    """A button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    #def __init__(self, win, center, width, height, label):
    def __init__(self, win, center, radius, label):
        """ Creates a circular button, eg:
        qb = Button(myWin, Point(30,25), 10, 'Quit') """

        #w,h = width/2.0, height/2.0
        #x,y = center.getX(), center.getY()
        #self.xmax, self.xmin = x+w, x-w
        #self.ymax, self.ymin = y+h, y-h
        #p1 = Point(self.xmin, self.ymin)
        #p2 = Point(self.xmax, self.ymax)
        # uses center point and radius as parameters
        self.center_x = center.getX()
        self.center_y = center.getY()
        self.radius = radius
        #self.rect = Rectangle(p1,p2)
        self.circ = Circle(center, radius)
        #self.rect.setFill('lightgray')
        self.circ.setFill('lightgray')
        #self.rect.draw(win)
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """ RETURNS true if button active and p is inside"""
        #return self.active and \
        #       self.xmin <= p.getX() <= self.xmax and \
        #       self.ymin <= p.getY() <= self.ymax
        return self.active and ((p.getX() - self.center_x)**2 +
                                (p.getY() - self.center_y)**2 <= self.radius**2)

    def getLabel(self):
        """RETURNS the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        #self.rect.setWidth(2)
        self.circ.setWidth(2)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        #self.rect.setWidth(1)
        self.circ.setWidth(1)
        self.active = 0
