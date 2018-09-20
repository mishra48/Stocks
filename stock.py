from iex import Stock
import telegram_send
import sched,time


def print_stocks():
    fit = int(Stock("FIT").price())
    tes = int(Stock("TSLA").price())
    if fit > 5:
        telegram_send.send(messages=['FIT: '+str(fit)])

    if  tes > 200:
        telegram_send.send(messages=['TSLA: ' + str(tes)])


if __name__ == '__main__':


    s = sched.scheduler(time.time, time.sleep)
    while 1:
        s.enter(10,1,print_stocks)
        s.run()

        print_stocks()




