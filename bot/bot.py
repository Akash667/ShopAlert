from telegram.ext import Updater, Filters, MessageHandler, PicklePersistence
import telegram
import logging
import datetime
import requests


logging.basicConfig(format='%(asctime)s %(message)s\n',
                    level=logging.INFO,filename='log.json')

logger = logging.getLogger(__name__)


def  check_logic(context):
        
    print("starting job")

    URL = ""
    products = context.bot_data[]
   

    for i in products:

         response = requests.get(URL,params=params)
    



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update caused error "%s"', context.error)


def main():

    my_persistence = PicklePersistence(filename="users")
    
    updater = Updater("",persistence=my_persistence,use_context=True)

    dp = updater.dispatcher
    jobs = updater.job_queue
   
    # jobs.run_repeating( check_logic,interval=36000,first=0)

    jobs.run_repeating( check_logic,interval=3600,first=0)

    # jobs.run_once( check_logic,when=datetime.datetime.now(datetime.timezone.utc))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,kick_member))
    
    dp.add_error_handler(error)

    updater.start_polling()
    
    updater.idle()



if __name__=="__main__":
    main()