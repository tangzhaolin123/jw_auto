# encoding=utf-8
# import threading
# import time
#
# threadLock = threading.Lock()
# num = 0
#
#
# class timer(threading.Thread):
#     def __init__(self, count, interval):
#         threading.Thread.__init__(self)
#         self.interval = interval
#         self.count = count
#
#     def run(self):
#         global num
#         while True:
#             # get lock
#             threadLock.acquire()
#             if num >= self.count:
#                 threadLock.release()
#                 break
#             num += 1
#             print ('Thread name:%s, %d' % (self.getName(), num))
#             threadLock.release()
#
#             time.sleep(self.interval)
#
#
# if __name__ == '__main__':
#     thread1 = timer(1000, 1)
#     thread2 = timer(1000, 1)
#     thread1.start()
#     thread2.start()
#     thread2.join()
#     thread2.join()

class Foo(object):

  def __init__(self):
    self.myattr = 0

  def bar(self):
    self.myattr += 1
    #return None
    return self

f = Foo()
print(f.myattr)
