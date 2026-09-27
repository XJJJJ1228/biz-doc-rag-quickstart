# biz-doc-rag-quickstart
面向业务人员的企业私有文档RAG知识库快速搭建工具箱
> 项目定位：聚焦中文企业文档预处理、语义切片、提示词工程、RAG问答效果评估。
> 优势：利用汉语言文本能力优化中文文档清洗与语义切分，解决传统RAG中文语义断裂、幻觉高、溯源困难问题。
> 适用文档类型：Word、PDF导出文本（制度文档、项目方案、内部规范）

## ✨ 项目亮点
1. 中文专属文档清洗规则：处理页眉页脚、分页断句、全角半角、表格碎行
2. 混合式语义切片策略：基于标题层级+中文标点切分，避免一句话被拦腰截断
3. 溯源式RAG提示词：强制引用原文片段，抑制大模型幻觉
4. RAG问答评估体系：人工评估表 + 脚本辅助检测幻觉，量化检索质量
5. 轻量化实现：无复杂后端，Python脚本开箱即用，业务人员可快速搭建知识库

## 📁 仓库目录
```text
biz-doc-rag-quickstart/
├── README.md                    # 项目说明
├── requirements.txt             # Python依赖
├── docs/
│   ├── 中文文档预处理规范.md
│   ├── 语义切片策略.md
│   └── RAG效果评估指标.md
├── prompts/
│   ├── base_rag_prompt.md
│   ├── cite_source_prompt.md
│   └── summarize_doc_prompt.md
├── test_cases/
│   ├── case1_company_rule.txt
│   ├── case2_project_plan.txt
│   └── RAG问答效果评估表.md
└── scripts/
    ├── text_clean.py
    ├── semantic_splitter.py
    └── rag_evaluator.py
```

## 🚀 快速开始

1. 安装依赖

```
pip install -r requirements.txt
```

2. 文档清洗：把原始文本清洗成干净文本

```
python scripts/text_clean.py test_cases/case1_company_rule.txt
```

3. 语义切片：对清洗后的文本做语义分块，输出 chunk 列表

```
python scripts/semantic_splitter.py
```

4. RAG 评估：输入问答对，检测回答是否存在幻觉

```
python scripts/rag_evaluator.py
```

## 📌 核心设计思路

很多企业 RAG 项目失败不是向量库 / 大模型问题，而是上游文档治理薄弱。
通用字符切片直接按固定长度截断文本，中文容易切断完整句子，丢失章节标题上下文，检索片段语义残缺，引发幻觉。
本项目从中文篇章、标点、段落结构出发，设计语义优先的切片方案，每一块附带章节元数据，支持回答溯源。

## 📊 评估维度

- 召回率：是否检索到答案对应的原文片段
- 幻觉率：回答是否编造原文不存在信息
- 引用准确性：引用片段与原文是否一致
- 信息完整性：是否遗漏关键信息

## 📖 测试案例说明

test_cases 存放脱敏企业文档，包含企业人事制度、项目实施方案，用于多组 RAG 问答测试。

```

## 使用方法
1. 点铅笔图标进入README编辑页
2. **全选页面里所有旧文字，全部删除**
3. 粘贴上面整段全部内容
4. 提交信息填写：`统一README代码块格式`，提交修改

粘贴完成后，所有代码块样式统一，目录和命令都有高亮显示。
提交完成，仓库就全部完工啦，之后我们就可以写简历项目描述+面试问答。
```
