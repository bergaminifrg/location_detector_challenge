import os
from abc import ABC, abstractmethod

class OutputStream(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    def open(self):
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()

    @abstractmethod
    def write_output(self, message):
        pass