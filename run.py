import argparse
import logging
from time import gmtime, strftime

import jeff



class Run():
    def __init__(self):
        self.options = {"verbosity": False,
                       "jenkins": False,
                       "test": False
                       }
        self.logSetting = None

    def setOption(self, option, value):
        self.options[option] = value
        return 0

    def getOption(self, option):
        if self.options.get(option) is not None:
            return self.options.get(option)
        else:
            return -1

    def args(self):
        parser = argparse.ArgumentParser()
        # Argumente Hinzufügen
        parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
        parser.add_argument("-v", help="increase output verbosity", action="store_true")
        parser.add_argument("--jenkins", help="meant to be used by jenkins", action="store_true")
        parser.add_argument("-j", help="meant to be used by jenkins", action="store_true")
        parser.add_argument("--test", help="meant to be used by Testing Routine", action="store_true")
        parser.add_argument("-t", help="meant to be used by Testing Routine", action="store_true")
        # Options Setup
        args = parser.parse_args()
        if args.verbose or args.v:
            print("Verbosity turned on.")
            self.options["verbosity"] = True
            return 'VERBOSITY'
        elif args.jenkins or args.j:
            print("Jenkins is running this.")
            self.options["jenkins"] = True
            return 'JENKINS'
        elif args.test or args.t:
            print("Testrun is starting.")
            self.options["test"] = True
            return 'TEST'
        return 0

    # Set up logging
    def log(self, level):
        logtime = strftime("%Y-%m-%d_%H_%M", gmtime())
        logname = 'Log//run_' + logtime + '.log'
        if level == "DEBUG":
            logging.basicConfig(
                filename=logname,
                filemode='w',
                level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s -  %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S')
            return "DEBUG"
        elif level == "INFO":
            logging.basicConfig(
                filename=logname,
                filemode='w',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s -  %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S')
            return "INFO"
        elif level == "WARNING":
            logging.basicConfig(
                filename=logname,
                filemode='w',
                level=logging.WARNING,
                format='%(asctime)s - %(levelname)s -  %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S')
            return "WARNING"

        logging.info('log was set up.')

    def getLogSettings(self):
        if self.logSetting is None:
            return -1
        return self.logSetting

    def setLogSettings(self, value):
        print(value)
        if value is not None:
            self.logSetting = value


if __name__ == '__main__':
    # Init args
    run = Run()
    run.args()
    # Start log
    if run.options["jenkins"]:
        run.setLogSettings(run.log("WARNING"))
        logging.info('Running bot as jenkins.')
        jeff.run()
    elif run.options["test"]:
        run.setLogSettings(run.log("INFO"))
        logging.info('Running bot in Test-mode.')
        jeff.run()
    elif run.options["verbosity"]:
        run.setLogSettings(run.log("DEBUG"))
        logging.info('Running bot and print all Info in DEBUG Mode.')
        jeff.run()
