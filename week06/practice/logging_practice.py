# W6 Day3: 日志意识练习
import traceback
from datetime import datetime

# 日志文件路径（固定，用追加模式写入）
LOG_PATH = "week06/evidence/error_log_w6.log"

def write_error_log(file_path, error_type, error_message, traceback_text=""):
    """把一条错误信息追加写入日志文件"""
    # 1. 生成时间戳
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. 拼接主日志行（时间戳 | 文件 | 错误类型 | 错误信息）
    line = f"[{timestamp}] ERROR | file={file_path} | type={error_type} | message={error_message}\n"

    # 3. 如果有 traceback，追加到后面
    if traceback_text:
        line += f"TRACEBACK:\n{traceback_text}\n"

    # 4. 加一条分隔线，方便阅读多次错误记录
    line += "-" * 80 + "\n"

    # 5. 用 a 追加模式写入，绝不覆盖
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)

# 测试：故意触发一个 FileNotFoundError
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        f.read()
except Exception as e:
    # type(e).__name__ 拿到错误类型名，比如 FileNotFoundError
    # str(e) 拿到错误信息文本
    # traceback.format_exc() 拿到完整的调用栈
    write_error_log(
        "不存在的文件.txt",
        type(e).__name__,
        str(e),
        traceback.format_exc(),
    )
    print("错误已写入日志：", LOG_PATH)