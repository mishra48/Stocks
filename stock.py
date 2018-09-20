from iex import Stock
import telegram_send




if int(Stock("FIT").price())> 0:
    telegram_send.send(messages=['FIT: '+str(Stock("FIT").price())])

if int(Stock("TSLA").price()) > 0:
    telegram_send.send(messages=['TSLA: ' + str(Stock("TSLA").price())])


