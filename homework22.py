import random
import logging
ansers = 0
while ansers <50:
	
	logging.basicConfig(format = '%(asctime)s %(message)s',  filename = "for_homework22", level = logging.DEBUG)
	random_answer = random.randint(0,50)
	if 0 <= random_answer <=9:
		logging.debug("debug")
	if 10 <= random_answer <= 19:
		logging.info("info")
	if 20 <= random_answer <= 29:
		logging.warning("warning")
	if 30 <= random_answer <= 39:
		logging.error("error")
	if 40 <= random_answer <= 50:
		logging.critical("critical")

	ansers += 1