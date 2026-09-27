"""
RAG评估脚本：简单检测回答是否包含原文不存在内容，标记疑似幻觉
支持命令行传入文档与问题，自动读取切片后的chunks知识库
"""
import jieba
import json
import sys

def check_hallucination(answer: str, source_text: str):
    # 简单判断：提取回答中所有中文词语，看是否在原文中存在
    words_answer = set(jieba.lcut(answer))
    words_source = set(jieba.lcut(source_text))
    new_words = words_answer - words_source
    # 过滤虚词
    stop_words = {"的", "了", "是", "在", "和", "有"}
    suspect_words = new_words - stop_words
    if len(suspect_words) > 0:
        return True, suspect_words
    else:
        return False, suspect_words

def retrieve_relevant_chunk(question: str, chunk_list):
    """简易检索：分词匹配，返回相关性最高的文本块"""
    q_words = set(jieba.lcut(question))
    best_chunk = ""
    max_score = 0
    for chunk in chunk_list:
        c_words = set(jieba.lcut(chunk["text"]))
        # 交集数量作为相关性分数
        score = len(q_words & c_words)
        if score > max_score:
            max_score = score
            best_chunk = chunk["text"]
    return best_chunk

if __name__ == "__main__":
    # 使用方式：python scripts/rag_evaluator.py "你的问题"
    if len(sys.argv) < 2:
        print("用法：python scripts/rag_evaluator.py \"测试问题\"")
        print("示例：python scripts/rag_evaluator.py \"员工事假最多多少天？\"")
        sys.exit(1)

    question = sys.argv[1]

    # 读取上一步语义切片输出的知识库 chunks
    try:
        with open("test_cases/chunks_output.json", "r", encoding="utf-8") as f:
            chunk_list = json.load(f)
    except FileNotFoundError:
        print("错误：找不到 test_cases/chunks_output.json，请先运行 semantic_splitter.py 生成切片文件！")
        sys.exit(1)

    # 召回最相关原文片段
    source_text = retrieve_relevant_chunk(question, chunk_list)
    if not source_text:
        print("⚠️ 没有检索到相关原文片段")
        sys.exit(1)

    # 模拟RAG模型回答（简易：直接从原文提取关键信息，后面可以替换成真实大模型调用）
    # =========【重点】这里目前是简易模拟，后续可对接大模型API =========
    model_answer = source_text

    has_hallu, words = check_hallucination(model_answer, source_text)
    print("==== RAG幻觉检测 ====")
    print(f"问题：{question}")
    print(f"模型回答：{model_answer}")
    print(f"原文片段：{source_text}")
    if has_hallu:
        print(f"⚠️ 疑似幻觉，出现原文不存在词汇：{words}")
    else:
        print("✅ 未检测到疑似幻觉")
