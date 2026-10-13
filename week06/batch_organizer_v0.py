# W6 Day4: 批量整理 v0（故意不加异常处理的裸奔版）
import os       # 用于操作文件路径、遍历目录
import shutil   # 用于移动文件

SRC_DIR = "week06/data/sandbox"

# 分类映射表：扩展名 -> 目标文件夹名
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

def organize_files(src_dir):
    # 1. 遍历目录里的每个名字
    for name in os.listdir(src_dir):
        # 2. 拼出完整路径（目录 + 文件名）
        src_path = os.path.join(src_dir, name)

        # 3. 如果这是个目录，跳过（我们不处理子目录）
        if os.path.isdir(src_path):
            continue

        # 4. 取文件扩展名（os.path.splitext 把 "image.jpg" 拆成 ("image", ".jpg")）
        # [1] 是取第二个元素，即 ".jpg"
        # .lower() 保证大小写不敏感，.JPG 和 .jpg 一样处理
        ext = os.path.splitext(name)[1].lower()

        # 5. 查表决定分类，查不到就归到 others
        category = CATEGORY_MAP.get(ext, "others")

        # 6. 拼出目标目录路径（比如 week06/data/sandbox/images）
        target_dir = os.path.join(src_dir, category)

        # 7. 创建目标目录（如果已存在，exist_ok=True 不报错）
        os.makedirs(target_dir, exist_ok=True)

        # 8. 拼出目标文件的完整路径
        target_path = os.path.join(target_dir, name)

        # 9. 把文件从 src_path 移动到 target_path
        shutil.move(src_path, target_path)
        print(f"移动: {src_path} -> {target_path}")

if __name__ == "__main__":
    organize_files(SRC_DIR)