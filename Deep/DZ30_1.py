# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# уровень DEBUG
d_i_h=logging.FileHandler('debug_info.log')
d_i_h.setLevel(logging.DEBUG)
d_i_h.setFormatter(formatter)
logger.addHandler(d_i_h)

# уровень WARNING и выше
w_e_h=logging.FileHandler('warnings_errors.log')
w_e_h.setLevel(logging.WARNING)
w_e_h.setFormatter(formatter)
logger.addHandler(w_e_h)

x = 4
y = 0

logger.info(f"The values of x and y are {x} and {y}.")
try:
    x/y
    logger.info(f"x/y successful with result: {x/y}.")
except Exception as err:
    logger.error("Exception",exc_info=True)
    print(err)

logger.debug('Это сообщение уровня DEBUG ')
logger.info('Это сообщение уровня INFO ')
logger.warning('Это сообщение уровня WARNING ')
logger.error('Это сообщение уровня ERROR ')
logger.critical('Это сообщение уровня CRITICAL ')