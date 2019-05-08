#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class GRASP_Input(metaclass=ABCMeta):

    @abstractmethod
    def setup():
        pass

    @abstractmethod
    def receive_callback():
        pass

    @abstractmethod
    def send():
        pass
