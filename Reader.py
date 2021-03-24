import logging
import sys
import os

import random

#==========================================================================
class Processor() :

  def __init__(self) :
    logging.warning("Processor Launched")

  def reader(self) :
    logging.warning("reader Launched")
    while True:
      self.line = sys.stdin.readline()
      logging.warning(self.line)

logging.warning("Processor Launched")
p=Processor()
p.reader()
