import yaml
import os,sys
from housing.exception import HousingException
import numpy as np
import pandas as pd
from housing.constants import *

def read_yaml_file(file_path:str) -> dict:
    """
    reads a YAML file and returns the contents as a dictionary.
    file_path : str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
    