# This is a file mocking prediction model
from pathlib import Path

# Example of importing another module inside the same directory
from .somedep import some_var


class Model():
    def __init__(self, model_path):
        with open(model_path) as f:
            self.text = f.read()

    def summary(self):
        print(self.text)

    def predict(self, X=None):
        return 0.8742


# Load model
base_path = Path(__file__).parent
file_path = base_path / 'model_data/model.txt'

model = Model(model_path=file_path)

