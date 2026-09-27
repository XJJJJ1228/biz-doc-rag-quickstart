"""
RAG评估脚本：简单检测回答是否包含原文不存在内容，标记疑似幻觉
"""

def check_hallucination(answer: str, source_text: str):
    # 简单判断：提取回答中所有中文词语，看是否在原文中存在
    import jieba
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

if __name__ == "__main__":
    # 示例问答，你可以修改这里
    source = "员工事假需要提前3个工作日提交申请，事假全年累计不超过15天。病假需提供医院诊断证明，病假不计入事假天数。"
    question = "员工一年事假最多多少天？"
    model_answer = "员工事假全年累计不超过15天。"

    has_hallu, words = check_hallucination(model_answer, source)
    print("==== RAG幻觉检测 ====")
    print(f"问题：{question}")
    print(f"模型回答：{model_answer}")
    print(f"原文片段：{source}")
    if has_hallu:
        print(f"⚠️ 疑似幻觉，出现原文不存在词汇：{words}")
    else:
        print("✅ 未检测到疑似幻觉")
