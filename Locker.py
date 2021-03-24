import threading

#==========================================================================
class Locker() :
  _lock=threading.Lock()

  @staticmethod
  def lock() :
    Locker._lock.acquire()
  @staticmethod
  def unlock() :
    Locker._lock.release()



