from TargetFinder import TargetFinder
from Worker import Worker
from Queue import Queue
from threading import Event

queue = Queue()
task_done_mark = Event()

if task_done_mark.isSet():
    task_done_mark.clear()

target_finder = TargetFinder(queue, task_done_mark)
target_finder.start()

worker_list = []
for i in range(5):
    worker = Worker(queue, task_done_mark)
    worker_list.append(worker)
    worker.setDaemon(True)
    worker.start()


print queue.qsize()
