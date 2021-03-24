import logging
from Locker import *
import time
import sys
import os

import random
from prometheus_client import (Summary,
                               Counter,
                               Histogram,
                               generate_latest,
                               CONTENT_TYPE_LATEST )


#==========================================================================
class ProcessorFactory() :
  @staticmethod
  def getProcessor(type) :
    if type=='jmeter' :
      logging.info("JmeterProcessor created")
      return(JmeterProcessor())
    else :
      logging.error("type " + type + " unknown")
      return

#==========================================================================
class Processor() :

  def reader(self) :
    logging.info("Processor Launched")
    while True:
      self.line = sys.stdin.readline()
      logging.info(self.line)
      Locker.lock()
      self.process()
      Locker.unlock()

  def process(self) :
    logging.error("process method must be overriden")

  def getInfos(self) :
    logging.error("getInfos method must be overriden")

#==========================================================================
class JmeterProcessor(Processor) :
  counter=Counter('my_line_counter','my counter',['myCounterLabel'])
  summary=Summary('my_line_summary','my histogram')
  histogram=Histogram('my_line_histogram','my histogram',buckets=(0.1, 0.2, 0.3, 0.4, 0.5, float("inf")))

  def process(self) :
    JmeterProcessor.counter.labels(myCounterLabel='label1').inc()
    JmeterProcessor.summary.observe(3.14)
    JmeterProcessor.histogram.observe(random.random())

  def getInfos(self) :
    #return(str(JmeterProcessor.counter))
    return(generate_latest())



