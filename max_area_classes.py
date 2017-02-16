class Rect:
    def __init__(self, height, width):
        """Create rectangle. Height and width must be positive."""
        assert(height > 0 and width > 0)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

def max_area(li):
    if len(li) == 0:
        return 0
    max = 0
    for item in li:
        if item.area() > max:
            max = item.area()
    return max

print(max_area( [ Rect(5,3), Rect(4,2), Rect(2, 13), Rect(3,3), Rect(50, 5000) ]))

