import time
import datetime
import os


class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = None
        self.elapsed_time = 0.0
        self.format_elapsed_time = None
        self.format_start_time = None
        self.format_end_time = None
        self.date_string = None

    def start(self):
        # Run stopwatch until user enters ctrl-c
        try:
            self.start_time = time.time()
            os.system('clear')
            print("Time started, ctrl-c to end")
            print("\n")
            print('''
                  70000007                  
                  70000007                  
                    0000                    
        707      9000000009      707        
       00008 300000000000000002 90000       
       900000000           7000000008       
         70005           0    20007         
        0000            07      0000        
       7000            00        0007       
       000            001         000       
      7000           000          0007      
      100           0000          7003      
      7009          6006          6007      
       000                        0007      
       6000                      0006       
        0000                    0000        
         00007                 0000         
          700000            00000           
             000000000000000000             
                700000000007                
                                            
                                            


                  ''')

            while True:
                pass

        except KeyboardInterrupt:
            self.end_time = time.time()

        self.elapsed_time = self.end_time - self.start_time

        self.calc_stats()

    def calc_stats(self):
        self.format_start_time = datetime.datetime.fromtimestamp(int(self.start_time)).time().strftime('%H:%M:%S')
        self.format_end_time = datetime.datetime.fromtimestamp(int(self.end_time)).time().strftime('%H:%M:%S')
        self.format_elapsed_time = str(datetime.timedelta(seconds=int(self.elapsed_time)))

        self.date_string = datetime.datetime.now().strftime("%m/%d/%Y")
