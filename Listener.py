import requests
import sys
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from Locker import *
from Processor import *
import threading
import time
import os

#==========================================================================
class Listener() :

  def __init__(self,args):
    port = int(args.port)
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    logging.info("http server is running on port " + str(port))
    processor=ProcessorFactory.getProcessor(args.type)
    HTTPRequestHandler.setResponseProvider(processor)
    tReader=threading.Thread(target=processor.reader)
    tReader.daemon=True
    tReader.start()
    httpd.serve_forever()

#==========================================================================
class HTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    responseProvider=None

    def do_GET(self, body=True):
      t = self.path.split("/")
      if len(t) < 1:
        logging.warning("cannot process requests "+self.path+", returning 404")
        self.send_response(404)
        self.end_headers()
        return
      # Respond with the requested data
      self.send_response(200)
      self.end_headers()
      Locker.lock()
      self.wfile.write(self.responseProvider.getInfos())
      Locker.unlock()
      return

    # !!!!!! ugly !!!!!!!
    @staticmethod
    def setResponseProvider(processor):
      logging.info("Setting Response provider")
      HTTPRequestHandler.responseProvider=processor
