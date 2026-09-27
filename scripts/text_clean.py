import re

def clean_text(raw_text: str) -> str:
    # 1. 删除页码、页眉页脚类噪声
    raw_text = re.sub(r"第\s*\d+\s*页\s*共\s*\d+\s*页", "", raw_text)
    # 2. 删除连续空行
    raw_text = re.sub(r"\n\s*\n", "\n", raw_text)
    # 3. 删除多余空格
    raw_text = re.sub(r"\s+", " ", raw_text)
    # 4. 修复换行：行末尾不是标点，合并换行
    lines = raw_text.split("\n")
    new_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 判断行尾是否为句子结束符号
        if new_lines and not re.search(r"[。；！？：]$", new_lines[-1]):
            new_lines[-1] = new_lines[-1] + line
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法：python scripts/text_clean.py test_cases/case1_company_rule.txt")
    else:
        file_path = sys.argv[1]
        with open(file_path, "r", encoding="utf-8") as f:
            raw = f.read()
        res = clean_text(raw)
        out_path = file_path.replace(".txt", "_cleaned.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(res)
        print(f"清洗完成，输出文件：{out_path}")
