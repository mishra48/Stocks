from iex import Stock
import telegram_send
import sched,time

flag1 = 0
flag2 = 0
def print_stocks():
    fit = float(Stock("FIT").price())
    tes = float(Stock("TSLA").price())
    if fit > 5:
        telegram_send.send(messages=['FIT: '+str(fit)])
        flag1 = 1

    if  tes > 200:
        telegram_send.send(messages=['TSLA: ' + str(tes)])
        flag2 = 1
    if flag1 == 1:
        time.sleep(300)
        flag1 = 0
        flag2 = 0

if __name__ == '__main__':



    while 1:


        print_stocks()





