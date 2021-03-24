import logging
from Watcher import *
import time
import os

#==========================================================================
class Launcher():

  #----------------------------------------------------------------------------
  def __init__(self,args) :
    self.file=args.file
    self.port=args.port
    if args.file.startswith("!") :
      os.system("cat " + args.file[1:]  + "| python PyL2P.py listen --port " + self.port)
    else :
      w=Watcher(args.file,self.watcherCallBack)
      w.rdv()

  #----------------------------------------------------------------------------
  def watcherCallBack(self,fileName) :
    os.system("tail -f " + fileName + "| python PyL2P.py listen --port " + self.port)
    print("Launched ! " + fileName)

#----------------------------------------------------------------------------
if __name__ == "__main__":
    run()

