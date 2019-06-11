""" Example pylib functions"""


import pandas as pd
import cityiq


def row_generator(resource, doc, env, *args, **kwargs):
    """ 

    """
    

    config = cityiq.Config()
    return cityiq.PedestrianIterator(config ).dataframe()

   