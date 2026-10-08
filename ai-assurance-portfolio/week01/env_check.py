import platform
import sys
from datetime import datetime

print("Python 版本:", sys.version)
print("平台:", platform.platform())
print("当前时间:", datetime.now())
print("解释器路径:", sys.executable)