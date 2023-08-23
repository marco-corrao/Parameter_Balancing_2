import pandas as pd
import numpy as np
import cobra
import logging 

class Preprocesser():
    '''
    Handles preprocessing of the metabolic model and the provided data
    '''
    def __init__(self,sbml_model,parameters):
        # Read SBML model
        try:
            self.raw_model=cobra.io.read_sbml_model(sbml_model)
            logging.info('Preprocesser: Successfully loaded raw SBML model')
        except:
            raise ValueError('Unable to read SBML Model from file. Make sure the provided path is correct and that the model can be loaded in COBRA')

