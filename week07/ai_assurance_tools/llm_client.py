# W8 Day4: LLM 客户端封装
import os
import time
import traceback
from datetime import datetime

from openai import OpenAI


class LLMClient:
    def __init__(self, api_key=None, base_url=None, model=None, error_log=None):
        self.api_key = api_key or os.getenv("ZAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("缺少 ZAI_API_KEY，请在 .env 中设置或传入 api_key 参数。")

        self.base_url = base_url or os.getenv(
            "ZAI_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/"
        )
        self.model = model or os.getenv("ZAI_MODEL", "glm-4-flash")
        self.error_log = error_log or "week08/evidence/error_log_w8.log"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def chat(self, messages):
        """发送对话请求，返回结构化结果"""
        start = time.time()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=False,
            )
            elapsed = time.time() - start
            return {
                "ok": True,
                "content": response.choices[0].message.content,
                "usage": getattr(response, "usage", None),
                "elapsed": elapsed,
                "error": None,
            }
        except Exception as e:
            elapsed = time.time() - start
            self._write_error(e, elapsed)
            return {
                "ok": False,
                "content": None,
                "usage": None,
                "elapsed": elapsed,
                "error": f"{type(e).__name__}: {e}",
            }

    def _write_error(self, error, elapsed):
        """把错误写入日志文件（追加模式）"""
        os.makedirs(os.path.dirname(self.error_log), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = (
            f"[{timestamp}] ERROR | type={type(error).__name__} | "
            f"message={error} | elapsed={elapsed:.2f}s\n"
            f"TRACEBACK:\n{traceback.format_exc()}\n"
            + "-" * 80 + "\n"
        )
        with open(self.error_log, "a", encoding="utf-8") as f:
            f.write(line)