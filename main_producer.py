from src.producer import main
import time

if __name__ == '__main__':
    while(True):
        main()
        print('Sent data')
        time.sleep(5)
        