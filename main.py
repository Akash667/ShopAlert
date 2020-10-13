from telegram.ext import Updater, Filters, MessageHandler, PicklePersistence
import telegram
import logging


logging.basicConfig(format='%(asctime)s %(message)s\n',
                    level=logging.INFO,filename='log.json')

logger = logging.getLogger(__name__)


def main():

    # my_persistence = PicklePersistence(filename="users") #incomment if you need persistence 
    
    # updater = Updater("",persistence=my_persistence,use_context=True)
    updater = Updater("",use_context=True)

    dp = updater.dispatcher
    jobs = updater.job_queue
   

    
    dp.add_error_handler(error)

    updater.start_polling()
    
    updater.idle()



if __name__=="__main__":
    main()