#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Logging

Created on Fri Oct 13 23:12:24 2017

@author: AK
"""

import logging
#logging.shutdown()
reload(logging) # reload the module to avoid multiple Spyder console output
import logging.handlers


def start_logging(log_level='info', logfile=None, fmt='short',
                  logtype='unlimited', loglim=200, logcount=5):
    """
    Use this to start logging to console.
    You might want to specify log file also (filename.log)
    And the type of logging to the file:
        unlimited - the output is just appended to the logfile
        #limited - not implemented
        rotating - rotate <logfile> <logcount> times when it <logsize> KB
    """
    if log_level is None:
        main_logger = logging.getLogger(__name__)
        return main_logger
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    hndlrs = [logging.StreamHandler()] # console handler
    if logfile is not None:
        if logtype == 'unlimited':
            hndlrs.append(logging.FileHandler('{}'.format(logfile),
                                                       encoding='utf8'))
        elif logtype == 'rotating':
            hndlrs.append(logging.handlers.RotatingFileHandler(
                            '{}'.format(logfile), encoding='utf8',
                             maxBytes=loglim*1024, backupCount=logcount))
    main_logger = logging.getLogger()
    main_logger.setLevel(LEVELS[log_level])
    if fmt == 'short':
        formatter = logging.Formatter("%(levelname)s: %(name)s: %(message)s")
    else:
        formatter = logging.Formatter(fmt='%(levelname)s:%(name)s: %(message)s '
                                      '(%(asctime)s; %(filename)s:%(lineno)d)',
                                      datefmt="%Y-%m-%d %H:%M:%S")
    #create formatter
#    formatter = logging.Formatter("%(asctime)s - %(name)s - " + \
#                                  "%(levelname)s - %(message)s")

    for h in hndlrs:
        h.setFormatter(formatter)
        h.setLevel(LEVELS[log_level])
        main_logger.addHandler(h)
    main_logger.info("\nLogging started. Level {}. Logfile {}".\
                     format(log_level, logfile))
    return main_logger

