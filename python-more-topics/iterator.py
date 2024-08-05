# let's create a class that is iterable

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


my_list = MyNumbers(10, 25)  # it will give numbers starting from 10 and continuing up to 25

for x in my_list:
    print(x)

