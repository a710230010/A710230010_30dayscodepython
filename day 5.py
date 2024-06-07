import sys
import time

while True:
    jam = time.strftime("%H:%M:%S", time.localtime())
    
    sys.stdout.write("\r" + "Sekarang Jam: " + jam)
    sys.stdout.flush()
    
    time.sleep(1)
