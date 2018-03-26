#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 16, 2017 Wed
# Last update :

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print('Meow')

    def __repr__(self):
        return '<Cat object. Name: {0}>'.format(self.name)


class CatBox:
    def __init__(self, size=3):
        self.size = size
        self.cats = []

    def add_cat(self, cat):
        if isinstance(cat, Cat):
            if len(self.cats) <= self.size:
                self.cats.append(cat)
            else:
                raise MemoryError('The box is full (it has {0} cats}.'.format(self.size))
        else:
            raise TypeError('Expected a Cat instance, got {0} instead'.format(type(cat)))

    def __repr__(self):
        return repr(self.cats)

def main():
    """Run main function."""
    box = [Cat('Narancs'), Cat('Omlás'), Cat('Don Gatto'), Cat('Vörös Harry'), Cat('Félszemű Babylon')]
    # for cat in box:
    #     print(cat)

    my_box = CatBox()
    my_box.add_cat(Cat('Narancs'))
    my_box.add_cat(Cat('Omlás'))
    my_box.add_cat(Cat('Don Gatto'))
    print(my_box)
    my_box.add_cat(Cat('Vörös Harry'))
    # my_box.add_cat(Cat('Narancs')) # This gives error

if __name__ == "__main__":
    main()
