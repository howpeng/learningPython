import gwy_files as gwy
import time


while True:
    print(gwy.files.find().count())
    time.sleep(2)