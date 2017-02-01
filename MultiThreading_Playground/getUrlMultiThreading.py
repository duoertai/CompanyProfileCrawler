import Queue
import threading
import urllib2
import time
import sys

hosts = ["http://google.com", "http://yahoo.com", "http://apple.com"]

queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            host = self.queue.get()
            url = urllib2.urlopen(host)
            print url.read(100)
            self.queue.task_done()

start = time.time()

for i in range(len(hosts)):
    t = ThreadUrl(queue)
    t.setDaemon(True)
    t.start()

for host in hosts:
    queue.put(host)

queue.join()

print "Elapsed time: %s" % (time.time() - start)
sys.exit()
