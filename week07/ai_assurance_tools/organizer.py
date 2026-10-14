# W7 Day5: FileOrganizer 类
import os
import shutil
import traceback

from ai_assurance_tools.logging_utils import write_error_log


class FileOrganizer:
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

    def __init__(self, src_dir, error_log):
        self.src_dir = src_dir
        self.error_log = error_log
        self.success = 0
        self.failed = 0
        self.skipped = 0

    def get_category(self, filename):
        """根据扩展名决定分类"""
        ext = os.path.splitext(filename)[1].lower()
        return self.CATEGORY_MAP.get(ext, "others")

    def get_unique_target_path(self, target_dir, name):
        """目标文件同名时自动加 _copy 后缀"""
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

    def organize(self):
        """主流程：遍历目录、分类、移动、记录异常"""
        if not os.path.exists(self.src_dir):
            write_error_log(self.error_log, self.src_dir, "FileNotFoundError", "源目录不存在")
            print(f"源目录不存在: {self.src_dir}")
            return self.success, self.failed, self.skipped

        for name in os.listdir(self.src_dir):
            src_path = os.path.join(self.src_dir, name)

            if os.path.isdir(src_path):
                self.skipped += 1
                continue

            try:
                category = self.get_category(name)
                target_dir = os.path.join(self.src_dir, category)
                os.makedirs(target_dir, exist_ok=True)

                target_path = self.get_unique_target_path(target_dir, name)
                shutil.move(src_path, target_path)
                self.success += 1
                print(f"成功: {src_path} -> {target_path}")

            except Exception as e:
                self.failed += 1
                write_error_log(
                    self.error_log,
                    src_path,
                    type(e).__name__,
                    str(e),
                    traceback.format_exc(),
                )
                print(f"失败: {src_path} | {type(e).__name__}: {e}")
                continue

        return self.success, self.failed, self.skipped

    def __str__(self):
        return f"FileOrganizer(src_dir={self.src_dir}, success={self.success}, failed={self.failed}, skipped={self.skipped})"