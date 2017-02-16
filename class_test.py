class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

def class_activator(a_lon, b_lon):
    if len(a_lon) != len(b_lon):
        raise Exception('Please give two lists with same length')
    if not isinstance(a_lon, list) or not isinstance(b_lon, list):
        raise TypeError('Hello this dont work son')

    for i in range(len(a_lon)):
        class_instance = Test(a_lon[i], b_lon[i])
        print(class_instance.addition())

class_activator([2, 4, 6, 8], [2, 4, 6, 9])
