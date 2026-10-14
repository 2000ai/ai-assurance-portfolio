# W7 Day2: 封装与方法拆分

class TemperatureConverter:
    def __init__(self):
        self._history = []

    def celsius_to_fahrenheit(self, celsius):
        """摄氏度转华氏度"""
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """华氏度转摄氏度"""
        return (fahrenheit - 32) * 5 / 9

    def record_history(self, source, target, value, result):
        """把一次换算记录进历史"""
        self._history.append({
            "source": source,
            "target": target,
            "value": value,
            "result": result,
        })

    def show_history(self):
        """打印所有历史记录"""
        if not self._history:
            print("暂无换算历史。")
            return

        print("=== 换算历史 ===")
        for i, item in enumerate(self._history, start=1):
            print(f"{i}. {item['value']} {item['source']} -> {item['result']:.2f} {item['target']}")

    def __str__(self):
        return f"TemperatureConverter(已记录 {len(self._history)} 条历史)"


if __name__ == "__main__":
    converter = TemperatureConverter()

    f = converter.celsius_to_fahrenheit(100)
    print(f"100 摄氏度 = {f:.2f} 华氏度")
    converter.record_history("摄氏度", "华氏度", 100, f)

    c = converter.fahrenheit_to_celsius(212)
    print(f"212 华氏度 = {c:.2f} 摄氏度")
    converter.record_history("华氏度", "摄氏度", 212, c)

    converter.show_history()

    print(converter)