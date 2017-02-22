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
#target_finder.join()

while not queue.empty():
    item = queue.get_nowait()
    queue.task_done()

task_done_mark.wait()
