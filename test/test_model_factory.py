import pytest
import sys
import os
import StringIO
sys.path.append(os.path.abspath('../'))
from src.models.ModelFactory import ModelFactory
from src.models.RandomForest import RandomForest


def test_model_load():
    """ Test the file parsing function"""
    fileString = """[model]
                    name=RandomForest
                    [params]
                    n_estimators=10"""
    expectedModel = "RandomForest"
    expectedparams = {"n_estimators": "10"}
    
    factory = ModelFactory()
    with open("test.ini", "w") as text_file:
        text_file.write(fileString)
    model, params = factory.parsefile("test.ini")
    os.remove("test.ini")

    assert model == expectedModel
    assert params == expectedparams


def test_getmodelfromfile():
    """ Test the model loading from file function"""
    fileString = """[model]
                    name=RandomForest
                    [params]
                    n_estimators=10
                    criterion=entropy"""

    expectedModel = RandomForest(n_estimators=10, criterion='entropy')
    
    factory = ModelFactory()
    with open("test.ini", "w") as text_file:
        text_file.write(fileString)
    model = factory.getmodelfromfile("test.ini")
    os.remove("test.ini")

    assert type(model) == type(expectedModel)
    assert model.get_params() == expectedModel.get_params()
