import argparse
import logging
from time import gmtime, strftime

import jeff

options = {
    "verbosity" : False ,
    "jenkins"   : False  ,
    "test" : False
}
parser = argparse.ArgumentParser()
#Argumente Hinzufügen
parser.add_argument("--verbose", help="increase output verbosity",action="store_true")
parser.add_argument("-v", help="increase output verbosity",action="store_true")
parser.add_argument("--jenkins", help="meant to be used by jenkins", action="store_true")
parser.add_argument("-j", help="meant to be used by jenkins", action="store_true")
parser.add_argument("--test", help="meant to be used by Testing Routine", action="store_true")
parser.add_argument("-t", help="meant to be used by Testing Routine", action="store_true")
#Optionen Setzen
args = parser.parse_args()
if args.verbose or args.v:
    print("Verbosity turned on.")
    options["verbosity"]=False
elif args.jenkins or args.j:
    print("Jenkins is running this.")
    options["jenkins"]=True
elif args.test or args.t:
    print("Testrun is starting.")
    options["test"]=True

# Set up logging
def Logging():
    logtime = strftime("%Y-%m-%d_%H_%M", gmtime())
    log='Log//run_'+logtime+'.log'

    logging.basicConfig(
        filename=log,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s -  %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
    logging.info('Logging was set up.')
    return

#     Run bot
if __name__ == '__main__':
#Start Logging
# Jenkins Test 3
    if(options["jenkins"]):
        Logging()
        logging.info('Running bot as jenkins.')
        jeff.run();
    elif(options["test"]):
        logging.info('Running bot in Test-mode.')
        jeff.run();
    elif(options["verbosity"]):
        logging.info('Running bot and print out logs.')
        jeff.run();