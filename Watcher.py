import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Watcher() :

  def __init__(self,pattern,callback):
    patterns = [pattern]
    self.callback=callback
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    self.eventHandler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    self.eventHandler.on_created = self.on_created
    self.eventHandler.on_deleted = self.on_deleted
    self.eventHandler.on_modified = self.on_modified
    self.eventHandler.on_moved = self.on_moved
    path = "."
    go_recursively = True
    self.observer = Observer()
    self.observer.schedule(self.eventHandler, path, recursive=go_recursively)
    self.observer.start()

  def rdv(self):
    self.observer.join()

  def on_created(self,event):
    print(f"hey, {event.src_path} has been created!")
    self.observer.stop()
    self.callback(event.src_path)
    #self.rdv()

  def on_deleted(self,event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

  def on_modified(self,event):
    print(f"hey buddy, {event.src_path} has been modified")

  def on_moved(self,event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
  w=Watcher("*")
  w.rdv()
