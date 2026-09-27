import re
import json

def split_semantic(text: str, source_file: str):
    chunks = []
    # 匹配标题：1.  1.1 一、（一）
    title_pattern = re.compile(r"^([0-9.]+|[一二三四五六七八九十]+、\(.\))\s*.+")
    lines = text.split("\n")
    current_chapter = "无章节"
    current_text = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 判断是否标题
        if title_pattern.match(line):
            # 先把上一段保存
            if current_text:
                chunks.append({
                    "source_file": source_file,
                    "chapter": current_chapter,
                    "chunk_text": current_text,
                    "chunk_length": len(current_text)
                })
            current_chapter = line
            current_text = ""
        else:
            current_text += line

    # 保存最后一段
    if current_text:
        chunks.append({
            "source_file": source_file,
            "chapter": current_chapter,
            "chunk_text": current_text,
            "chunk_length": len(current_text)
        })
    return chunks

if __name__ == "__main__":
    input_file = "test_cases/case1_company_rule_cleaned.txt"
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    chunk_result = split_semantic(text, "case1_company_rule.txt")
    out_file = "test_cases/chunks_output.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(chunk_result, f, ensure_ascii=False, indent=2)
    print(f"语义切片完成！共 {len(chunk_result)} 个文本块，结果保存在 {out_file}")
