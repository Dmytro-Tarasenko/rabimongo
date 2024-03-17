from src.consumer import main
import time

if __name__ == '__main__':
    while(True):
        main()
        print('Recieved data')
        time.sleep(5)