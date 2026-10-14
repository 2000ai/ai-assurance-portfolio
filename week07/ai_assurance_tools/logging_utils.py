# W7 Day4: 日志工具模块
import os
import traceback
from datetime import datetime


def write_error_log(log_path, file_path, error_type, error_message, traceback_text=""):
    """把错误追加写入日志文件"""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] ERROR | file={file_path} | type={error_type} | message={error_message}\n"
    if traceback_text:
        line += f"TRACEBACK:\n{traceback_text}\n"
    line += "-" * 80 + "\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line)