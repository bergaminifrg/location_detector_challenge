import os
from abc import ABC, abstractmethod

class InputStream(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    def open(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Input file '{self.file_path}' does not exist.")

    @abstractmethod
    def read_input(self):
        pass