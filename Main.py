from TargetFinder import TargetFinder
from Queue import Queue

queue = Queue()
target_finder = TargetFinder(queue)
target_finder.start()
target_finder.join()