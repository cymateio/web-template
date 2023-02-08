from abc import ABCMeta, abstractclassmethod


class BaseSignin(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractclassmethod
    def signin(self, username, password):
        pass

    @abstractclassmethod
    def set_username(self, username):
        pass

    @abstractclassmethod
    def set_password(self, password):
        pass

    @abstractclassmethod
    def click_signin(self):
        pass
