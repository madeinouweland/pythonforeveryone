import datetime
import os
import sys

path = f"{os.getcwd()}/text.txt"
file = open(path,"w")
file.write(f"The datetime is {datetime.datetime.now()}")
file.close()

print(f"File {path} saved")
