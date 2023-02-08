from abc import ABCMeta, abstractclassmethod


class BaseMain(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractclassmethod
    def navigate_workspace(self):
        pass
