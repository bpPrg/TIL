#!python
# -*- coding: utf-8 -*-#
"""
Config parser example

@author: Bhishan Poudel

@date: 

@email: bhishanpdl@gmail.com

"""
# Imports

from configparser import ConfigParser

def eg():    
    Config = ConfigParser()    
    c = Config.read('data3.txt')
    print('c = ', c) 

    cs = Config.sections()
    print(cs)


def ConfigSectionMap(section):
    Config = ConfigParser()
    Config.read('data3.txt')
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def eg2():
    Config = ConfigParser() 
    Config.read('data3.txt')
    Name = ConfigSectionMap("SectionOne")['name']
    Age = ConfigSectionMap("SectionOne")['age']
    single = Config.getboolean("SectionOne", "single")
    print ("Hello %s. You are %s years old." % (Name, Age))
    print("single = {}".format(single))
    
    
    
def main():
    """Run main function."""
    eg2()

if __name__ == "__main__":
    main()
