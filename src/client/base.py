from abc import ABC, abstractmethod


class BaseClient(ABC):

    @abstractmethod
    def __call__(
        self, 
        *args, 
        **kwargs
    ):
        pass
