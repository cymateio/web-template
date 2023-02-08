from abc import ABCMeta, abstractclassmethod


class BaseWorkspaces(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractclassmethod
    def click_collection(self):
        pass

    @abstractclassmethod
    def click_api(self):
        pass

    @abstractclassmethod
    def click_send(self):
        pass
