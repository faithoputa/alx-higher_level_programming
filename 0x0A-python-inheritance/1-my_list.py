#!/usr/bin/python3
class MyList(list):

    def print_sorted(self):
        self.sort()
        for elem in self:
            print(elem)

