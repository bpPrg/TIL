#!python
# -*- coding: utf-8 -*-#
"""
Class example

@author: Bhishan Poudel

@date: Mar 12, 2018
https://www.youtube.com/watch?v=DEwgZNC-KyE

"""
# Imports


class Person():
  def __init__(self, name):
    self.name = name

  def reveal_identity(self):
    print("My name is {}.".format(self.name))


class SuperHero(Person):
  def __init__(self, name, hero_name):
    super(SuperHero, self).__init__(name)
    self.hero_name = hero_name

  def reveal_identity(self):
    super(SuperHero, self).reveal_identity()
    print("... And I am {}.".format(self.hero_name))


def main():
  """Run main function."""
  bhishan = Person('Bhishan')
  bhishan.reveal_identity()

  # wade = SuperHero('Wade Wilson', 'Deadpool')
  # wade.reveal_identity()


if __name__ == "__main__":
  main()
