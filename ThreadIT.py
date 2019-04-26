import threading
from threading import Thread
class ThreadIT:
	def __init__(self, TargetFunc, amount=1, Args=None, Proxies=None, zombies=None, sleeps=0.0, xi=None):
		myThreads2 = []
		for x in range(amount):
			newThread2 = Thread(target = TargetFunc, args=[x])
			if zombies != None:
				newThread2 = Thread(target = TargetFunc, args=[zombies[x]])
			else:
				pass
			if zombies != None and Args != None:
				newThread2 = Thread(target = TargetFunc, args=[zombies[x], Args])
			elif zombies != None and Proxies != None:
				newThread2 = Thread(target = TargetFunc, args=[zombies[x], Proxies])
			elif Proxies != None:
				newThread2 = Thread(target = TargetFunc, args=[x, Proxies])
			elif Args != None:
				newThread2 = Thread(target = TargetFunc, args=[x, Args])
			elif Args != None and Proxies != None:
				newThread2 = Thread(target = TargetFunc, args=[x, Proxies, Args])
			else:
				pass
			if zombies != None and Args != None and Proxies != None:
				newThread2 = Thread(target = TargetFunc, args=[zombies[x], Proxies, Args])
			elif xi and Args != None and Proxies != None:
				newThread2 = Thread(target = TargetFunc, args=[x, Proxies, Args])
			myThreads2.append(newThread2)
			newThread2.start()
			if sleeps > 0:
				from time import sleep
				sleep(sleeps)
			else:
				pass
		for y in myThreads2:
			y.join()
