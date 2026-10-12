# W5 Day5: 词频统计 v1
ARTICLE = """
Python is great. Python is easy. Learning Python is fun.
Python is powerful and Python is friendly.
"""

PUNCTUATIONS = [".", ",", "!", "?", ";", ":", "\n", "\t", "(", ")", "\"", "'"]

def clean_text(text):
    """清洗文本：转小写、去标点"""
    text = text.lower()
    for p in PUNCTUATIONS:
        text = text.replace(p, " ")
    return text

def get_words(text):
    """先清洗，再按空白切分成列表"""
    cleaned = clean_text(text)
    return cleaned.split()

def count_words(words):
    """统计每个词出现的次数，返回字典"""
    counts = {}
    for word in words:
        if word == "":
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts

def sort_counts(counts):
    """把字典转成列表，按次数降序排序"""
    items = list(counts.items())
    items.sort(key=lambda item: item[1], reverse=True)
    return items

def main():
    words = get_words(ARTICLE)
    counts = count_words(words)
    sorted_counts = sort_counts(counts)

    print(f"总词数: {len(words)}")
    print(f"唯一词数: {len(counts)}")
    print("Top 10:")

    for word, count in sorted_counts[:10]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()