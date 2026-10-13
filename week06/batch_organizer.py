# W6 Day5: 批量整理 v1
import os
import shutil
import traceback
from datetime import datetime

SRC_DIR = "week06/data/sandbox"
ERROR_LOG = "week06/evidence/error_log_w6.log"

CATEGORY_MAP = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".txt": "documents",
    ".pdf": "documents",
    ".docx": "documents",
    ".mp3": "audio",
    ".wav": "audio",
    ".mp4": "video",
    ".mov": "video",
}

def write_error_log(file_path, error_type, error_message, traceback_text=""):
    os.makedirs(os.path.dirname(ERROR_LOG), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] ERROR | file={file_path} | type={error_type} | message={error_message}\n"
    if traceback_text:
        line += f"TRACEBACK:\n{traceback_text}\n"
    line += "-" * 80 + "\n"
    with open(ERROR_LOG, "a", encoding="utf-8") as f:
        f.write(line)

def get_unique_target_path(target_dir, name):
    target_path = os.path.join(target_dir, name)
    if not os.path.exists(target_path):
        return target_path
    base, ext = os.path.splitext(name)
    index = 1
    while True:
        new_name = f"{base}_copy{index}{ext}"
        new_path = os.path.join(target_dir, new_name)
        if not os.path.exists(new_path):
            return new_path
        index += 1

def organize_files(src_dir):
    success = 0
    failed = 0
    skipped = 0

    if not os.path.exists(src_dir):
        write_error_log(src_dir, "FileNotFoundError", "源目录不存在")
        print(f"源目录不存在: {src_dir}")
        return success, failed, skipped

    for name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, name)

        if os.path.isdir(src_path):
            skipped += 1
            continue

        try:
            ext = os.path.splitext(name)[1].lower()
            category = CATEGORY_MAP.get(ext, "others")
            target_dir = os.path.join(src_dir, category)
            os.makedirs(target_dir, exist_ok=True)

            target_path = get_unique_target_path(target_dir, name)
            shutil.move(src_path, target_path)
            success += 1
            print(f"成功: {src_path} -> {target_path}")

        except Exception as e:
            failed += 1
            write_error_log(src_path, type(e).__name__, str(e), traceback.format_exc())
            print(f"失败: {src_path} | {type(e).__name__}: {e}")
            continue

    return success, failed, skipped

def main():
    print("=== 批量整理开始 ===")
    success, failed, skipped = organize_files(SRC_DIR)
    print(f"成功: {success}, 失败: {failed}, 跳过目录: {skipped}")
    print(f"错误日志: {ERROR_LOG}")

if __name__ == "__main__":
    main()