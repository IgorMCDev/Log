from os import path
from logging import Formatter, FileHandler, getLogger, DEBUG

class Logger():
    def __init__(self, nome, data, path, nivel_log = ''):
        self.data = data
        self.nome = nome
        self.logger = getLogger(self.nome)
        self.nivel_log = nivel_log if nivel_log != '' else DEBUG
        self.destino=path
        self.handlers=[]
        self.logger.__inicializa_logs()

    def __del__(self):
        self.__finaliza_logs()
    
    def __inicializa_logs(self):
        format_log = Formatter(fmt='[%(levelname)s][%(acstime)s][%(filename)s:%(lineno)s/%(funcName)s()] %(message)s', 
                                       datefmt= '%d/%M/%Y %H:%M:%S')
        handle_logger = FileHandler(filename = path.join(self.destino,'{}{}{}'.format(self.data.strftime('%Y%m%d'), self.nome, 'LOG.txt')))
        handle_logger.setLevel(self.nivel_log)
        handle_logger.setFormatter(format_log)
        self.logger.setLevel(self.nivel_log)
        self.logger.addHandler(handle_logger)
        self.handlers.append(handle_logger)
        
    def __finaliza_logs(self):
        for handler in self.handlers:
            self.logger.removeHandler(handler)
        self.handlers.clear()