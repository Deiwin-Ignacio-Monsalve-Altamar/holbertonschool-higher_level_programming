

"7-rectangle.py print rectangle"


class Rectangle:
    """Class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

    def area(self):
        return self.__heigth * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__heigth == 0:
            return 0
        return (2 * self.__width) + (2 * self.__heigth)

    def __str__(self):
        new_string = ''
        if self.__width == 0 or self.__heigth == 0:
            return new_string
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        for width in range(self.__heigth):
            new_string += (self.print_symbol * self.__width) + '\n'
        return new_string

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__heigth)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
