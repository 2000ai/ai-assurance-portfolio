# W7 Day5: 入口脚本，测试 FileOrganizer 类
from ai_assurance_tools import FileOrganizer

SRC_DIR = "week07/data/sandbox"
ERROR_LOG = "week07/evidence/error_log_w7.log"


def main():
    print("=== W7 可安装小包 批量整理 ===")
    organizer = FileOrganizer(SRC_DIR, ERROR_LOG)
    success, failed, skipped = organizer.organize()
    print(f"成功: {success}, 失败: {failed}, 跳过目录: {skipped}")
    print(f"错误日志: {ERROR_LOG}")
    print(organizer)   # 触发 __str__


if __name__ == "__main__":
    main()