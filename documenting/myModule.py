# -*- coding: utf-8 -*-
"""
<b>summary:</b> An example of a module to cover documentation generators for an in-class example for a python programming course.

Created on Mon Mar  6 18:29:50 2023

<b>author:</b> <i>C. S. Francis</i>

sdev 220 spring 2023
"""



class Person():
    def __init__(self, name, age, town):
        """
        A dataclass to handle some example data

        Parameters
        ----------
        name : str
            the person's name.
        age : int
            the <b>person's</b> age.
        town : <i>str</i>
            where the person lives.

        Returns
        -------
        None.

        """
        self.name = name
        self.age = age
        self.town = town
        
    def hasMoved(self):
        """
        A method to print an alternate string if the town data is no longer accurate

        Returns
        -------
        str
            a generic statement.

        """
        return f"{self.name} used to live in {self.town}"
        
        


def SayHi():
    """
    A method to call the standard configuration check

    Returns
    -------
    None.

    """
    print("hello world")
    



def double(x):
    """
    A function that finds twice as much as any value passed in.

    Parameters
    ----------
    x : numeric
        The number we want to find twice as much as.

    Returns
    -------
    numbeic
        twice as much as the number that was passed in.

    """
    return x + x


def adding(x, y):
    """
    A function to add a couple numbers together.

    Parameters
    ----------
    x : numeric
        teh first number to be added.
    y : numeric
        the second number to include in the sum.

    Returns
    -------
    numeric
        the summation of the two numbers passed in.

    """
    return x + y


























