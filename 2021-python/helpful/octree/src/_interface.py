#!/bin/python


"""Object interfaces"""

from abc import ABCMeta, abstractmethod

class IPoint:
    @property
    @abstractmethod
    def x(self):
        pass