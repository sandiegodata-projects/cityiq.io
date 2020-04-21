""" Example pylib functions"""


import pandas as pd
import sys
print('\n'.join(sys.path))
import cityiq


def row_generator(resource, doc, env, *args, **kwargs):
    """ 

    """
    

    config = cityiq.Config()
    return cityiq.PedestrianIterator(config ).dataframe()

   