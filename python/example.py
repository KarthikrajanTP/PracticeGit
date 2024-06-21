import os
from datetime import datetime

ctime = os.stat('report.csv')
epoch = ctime.st_mtime
humanReadable = datetime.fromtimestamp(epoch)
print(humanReadable)