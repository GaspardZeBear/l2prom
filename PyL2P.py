import requests
import sys
import logging
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from Launcher import *
from Listener import *
import threading
import time
import os

#----------------------------------------------------------------------------
def fLaunch(args) :
    Launcher(args)

#----------------------------------------------------------------------------
def fListen(args) :
    Listener(args)

#----------------------------------------------------------------------------
def run():
    loglevel = [logging.WARNING, logging.INFO, logging.DEBUG, 1]
    logging.basicConfig(
        format="%(asctime)s %(module)s %(name)s  %(funcName)s %(lineno)s %(levelname)s %(message)s",
        level=loglevel[1],
    )
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help')

    parserLaunch=subparsers.add_parser('launch', help='a help')
    parserLaunch.set_defaults(func=fLaunch)
    parserLaunch.add_argument("--port","-p",help="listening port",default="8080")
    parserLaunch.add_argument("--file","-f",help="file to listen")
    parserLaunch.add_argument("--type","-t",help="type",default="jmeter")

    parserListen=subparsers.add_parser('listen', help='a help')
    parserListen.set_defaults(func=fListen)
    parserListen.add_argument("--port","-p",help="listening port",default="8080")
    parserListen.add_argument("--type","-t",help="type",default="jmeter")

    args=parser.parse_args()
    args.func(args)

#----------------------------------------------------------------------------
if __name__ == "__main__":
    run()

