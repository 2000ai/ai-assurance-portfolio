import torch
import os

# 为了演示干净，先删掉可能存在的旧文件
if os.path.exists("/tmp/hacked_by_ai.txt"):
    os.remove("/tmp/hacked_by_ai.txt")

print("⏳ 受害者正在使用 torch.load 加载模型...")

# 🎯 强行关闭安全防护，模拟旧版本 PyTorch 的受害者
model = torch.load("malicious_model.pt", weights_only=False)

print("✅ 模型加载完成！")