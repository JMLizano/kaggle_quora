import configparser
import importlib


class ModelFactory():

    def __init__(self):
        self.config = configparser.ConfigParser()

    def parsefile(self, file):
        self.config.read(file)
        model = self.config["model"]["name"]
        params = self.config._sections["params"]
        return model, params

    def getmodelfromfile(self, file):
        """Parse 'file' and returns specified model initialized with params in file
        """
        try:
            model, params = self.parsefile(file)
            model_module = importlib.import_module('src.models.' + model)
            model_class = getattr(model_module, model)

            return model_class(**params)
        except ImportError:
            loggin.error("Model specified does not exist (or is not implemented)")

        
