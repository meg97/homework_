import logging

engine_number = '1_1'

# tell_temp = int(input("tell the temperature"))
# if tell_temp > 50:

# 	logging.warning("the engine temperature is above the optimal level")
# logging.info("the engine temperature is raising")
# logging.debug(f"the {engine_number} engine temperature is raising")
# logging.error(f"Can't turn off {engine_number} engine")

# logging.basicConfig(filename = "temperatures.log", level = logging.DEBUG)
# logging.debug("This message shiould go to the log file")
# logging.info("So shiould this")
# logging.warning("And this too")
# logging.error("And non ASCII stuff too")


# logging.basicConfig(filename = "example.log", filemode = 'w', level = logging.DEBUG)
# logging.debug("This message shiould go to the log file")
# logging.info("So shiould this")
# logging.warning("And this too")
# logging.error("And non ASCII stuff too")

# logging.warning("%s before you %s", "look", "leap")

# logging.basicConfig(format = '%(levelname)s:%(message)s', level = logging.DEBUG)
# logging.warning("And this too")
# logging.error("And non ASCII stuff too")

logging.basicConfig(format = '%(asctime)s %(message)s')
logging.warning("is the temperature 100")


dict_ = {"key1":5}

try:
	a = dict_["key2"]
except KeyError:
	logging.error('key2 is not exist', exc_info = True)

print("\n that was error message")