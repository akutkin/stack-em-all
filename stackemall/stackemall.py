#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
functions to stack VLBI maps

Created on Fri Oct 13 21:04:17 2017

@author: AK
"""
import os

import astropy.io.fits as pf
import skimage as ski
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from logger import start_logging


logger = start_logging('debug', fmt='')

def check_params(mfiles):
    """
    Check that all the files have the same params
    Input: mfiles -- iterable of filenames to stack
    """
    for mfile in mfiles:
        if not os.path.exists(mfile):
            logger.error('No such file: {}'.format(mfile))
#        par =




