from time import sleep
import os
class SleepD:
    def __init__(self, time=None, method='title', clear=None):
        self.clear = clear
        #Title Only is only for >1 in INT
        #log is Tenth of decimal 
        if time:
            if time < 0:
                raise IOError("Time Less Than 0 in SleepD()")
            self.time = time
            if method == 'title':        
                self.sleeptitle()
            elif method == 'log':
                self.sleeplog()
        else:
            raise IOError("Try Putting Number in SleepD()") 
    def sleeptitle(self):
        self.time = int(self.time)
        while self.time != -1:
            if self.time == 0:
                os.system('title Time Left: ' + str(int(self.time)))
                self.time -= 1
                continue
            os.system('title Time Left: ' + str(int(self.time)))
            sleep(1)
            self.time -= 1
    def sleeplog(self):
        while self.time != 0:
            if self.time < 0:
                self.time = 0
                if self.clear != None:
                    os.system('cls')
                print('Time Left: ' + str(self.time))
                continue
            print('Time Left: ' + str(self.time))
            sleep(0.0166666666666666667)
            self.time -= 0.0166666666666666667
