# 认知工具：扩展上下文工程框架

> “心灵不是要填满的器皿，而是要点燃的火。”

## 从生物学到认知

我们的情境工程之旅遵循一个生物学隐喻：

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Atoms   │────►│ Molecules│────►│  Cells   │────►│  Organs  │
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Prompts │     │ Few-shot │     │  Memory  │     │Multi-agent│
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

现在，我们将通过与人类认知的相似之处来扩展这个框架。就像人类大脑使用认知工具来有效地处理信息一样，我们可以为 LLM 创建类似的结构：

```
┌──────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE TOOLS EXTENSION                       │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Heuristics        │ Mental shortcuts that simplify       │
│ COGNITION│                   │ complex problems                     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Prompt Programs   │ Structured prompt patterns that      │
│ PARALLEL │                   │ guide model reasoning                │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Schemas           │ Organized knowledge structures       │
│ COGNITION│                   │ that help categorize information     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Context Schemas   │ Standardized formats that            │
│ PARALLEL │                   │ structure information for models     │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Priming           │ Activation of certain associations   │
│ COGNITION│                   │ that influence subsequent thinking   │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Recursive         │ Self-referential prompting that      │
│ PARALLEL │ Prompting         │ shapes model behavior patterns       │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘
```


## 认知工具？ 

### **[使用认知工具在语言模型中引出推理 - IBM 苏黎世，2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

### 提示符和提示程序作为推理工具调用
> “认知工具”将推理作封装在 LLM 本身中 — [IBM 苏黎世](https://www.arxiv.org/pdf/2506.12115)



![图像](https://github.com/user-attachments/assets/cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae)

> **这些认知工具（结构化提示模板作为工具调用）通过识别手头的主要概念、提取问题中的相关信息以及突出显示有意义的属性、定理和技术来分解问题
可能有助于解决问题。**

![图像](https://github.com/user-attachments/assets/f7ce8605-6fa3-494f-94cd-94e6b23032b6)


> **这些模板支撑着类似于认知心理捷径的推理层，通常被称为 “启发式”。**

## 提示程序：LLM 的算法思维（推理工具调用）

提示程序是一种结构化的、可重用的提示模式，旨在指导 LLM 的推理过程，类似于启发式方法指导人类思维的方式。

### 从 Ad-hoc Prompts 到 Programmatic Patterns

让我们将 ad-hoc 提示与简单的 prompt 程序（推理工具调用）进行比较：

```
┌───────────────────────────────────────────────────────────────┐
│ AD-HOC PROMPT                                                 │
├───────────────────────────────────────────────────────────────┤
│ "Summarize this article about climate change in 3 paragraphs. │
│  Make it easy to understand."                                 │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│ PROMPT PROGRAM                                                │
├───────────────────────────────────────────────────────────────┤
│ program Summarize(text, paragraphs=3, complexity="simple") {  │
│   // Define the task                                          │
│   task = `Summarize the following text in ${paragraphs}       │
│           paragraphs. Use ${complexity} language.`;           │
│                                                               │
│   // Define the process                                       │
│   process = ```                                               │
│     1. Identify the main topic and key points                 │
│     2. Organize points by importance                          │
│     3. Create a coherent summary with:                        │
│        - First paragraph: Main topic and context              │
│        - Middle paragraph(s): Key supporting details          │
│        - Final paragraph: Conclusions or implications         │
│   ```;                                                        │
│                                                               │
│   // Define the output format                                 │
│   format = "A ${paragraphs}-paragraph summary using           │
│             ${complexity} language.";                         │
│                                                               │
│   // Construct the complete prompt                            │
│   return `${task}\n\nProcess:\n${process}\n\n                │
│           Format:\n${format}\n\nText to summarize:\n${text}`; │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

提示程序方法具有以下几个优点：
1. **可重用性**：相同的模式可以应用于不同的文本
2. **参数化**：轻松自定义长度、复杂性等。
3. **透明度**：清晰的结构使提示的意图明确
4. **一致性**：在运行中产生更可预测的结果

### 简单提示程序模板

以下是创建自己的提示程序的基本模板：

```
program [Name]([parameters]) {
  // Define the task
  task = `[Clear instruction using parameters]`;
  
  // Define the process
  process = ```
    1. [First step]
    2. [Second step]
    3. [Additional steps as needed]
  ```;
  
  // Define the output format
  format = "[Expected response structure]";
  
  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\n[Input]`;
}
```

在实践中，可以通过多种方式实现此模板：
- 作为文档中的伪代码或协议 shell
- 作为生成提示的实际 JavaScript/Python 函数
- 作为具有变量替换的 YAML 模板
- 作为标准化提示构建的 JSON 模式

## 推理提示模板（工具调用）

### 1. 循序渐进的推理

将复杂推理分解为可管理步骤的基本模板。

```markdown
# Step-by-Step Reasoning Template

Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {{problem}}

Please follow this process:
1. **Understand**: Restate the problem and identify what you need to find.
2. **Plan**: Outline your approach to solving the problem.
3. **Execute**: Work through each step of your plan in detail.
   - Step 1: [Description of the first step]
   - Step 2: [Description of the second step]
   - Step 3: [Continue with additional steps as needed]
4. **Verify**: Check your solution against the original problem.
5. **Conclude**: State your final answer or conclusion clearly.

Show all your work and explain your reasoning at each step.
```

**Token Count**：~130 个代币（仅限模板）

## 什么是协议 shell？（推理工具调用）

协议 shell 是结构化的，没有代码模板，将与 AI 系统的通信组织成清晰、一致的模式。将它们视为建立以下目标的对话蓝图：

1. **意向**：您要完成的任务
2. **输入**：您提供的信息
3. **处理**：应如何处理信息
4. **输出**：您期望的结果

### 基本协议 Shell 结构

```
/protocol.name{
    intent="Clear statement of purpose",
    input={
        param1="value1",
        param2="value2"
    },
    process=[
        /step1{action="do something"},
        /step2{action="do something else"}
    ],
    output={
        result1="expected output 1",
        result2="expected output 2"
    }
}
```

此结构创建了一个清晰、令牌高效的框架，您和 AI 都可以遵循该框架。

**反思练习**：看看你最近的 AI 对话。您能否识别出您一直在使用的隐含结构（即情感背景、潜在意图、长期目标、相互矛盾的输入等）？将这些内容形式化为协议 shell 并使数据更加明确如何改善您的交互？

## 协议 shell 剖析

让我们剖析协议 shell 的每个组件，以了解其用途和强大功能：

```
┌─────────────────────────────────────────────────────────┐
│                    PROTOCOL ANATOMY                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /protocol.name{                                        │
│    │       │                                            │
│    │       └── Subtype or specific variant              │
│    │                                                    │
│    └── Core protocol type                               │
│                                                         │
│    intent="Clear statement of purpose",                 │
│    │       │                                            │
│    │       └── Guides AI understanding of goals         │
│    │                                                    │
│    └── Declares objective                               │
│                                                         │
│    input={                                              │
│        param1="value1",   ◄── Structured input data     │
│        param2="value2"                                  │
│    },                                                   │
│                                                         │
│    process=[                                            │
│        /step1{action="do something"},     ◄── Ordered   │
│        /step2{action="do something else"} ◄── steps     │
│    ],                                                   │
│                                                         │
│    output={                                             │
│        result1="expected output 1",   ◄── Output        │
│        result2="expected output 2"    ◄── specification │
│    }                                                    │
│  }                                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```


## 上下文模式：结构化信息模式


就像人类思维使用图式来组织知识一样，我们可以为 LLM 创建上下文图式，即构建信息以提高模型理解的标准化方法。

### 基本架构结构

```
┌───────────────────────────────────────────────────────────────┐
│ CONTEXT SCHEMA                                                │
├───────────────────────────────────────────────────────────────┤
│ {                                                             │
│   "$schema": "context-engineering/schemas/v1.json",           │
│   "title": "Analysis Request Schema",                         │
│   "description": "Standard format for requesting analysis",   │
│   "type": "object",                                           │
│   "properties": {                                             │
│     "task": {                                                 │
│       "type": "string",                                       │
│       "description": "The analysis task to perform"           │
│     },                                                        │
│     "context": {                                              │
│       "type": "object",                                       │
│       "properties": {                                         │
│         "background": { "type": "string" },                   │
│         "constraints": { "type": "array" },                   │
│         "examples": { "type": "array" }                       │
│       }                                                       │
│     },                                                        │
│     "data": {                                                 │
│       "type": "string",                                       │
│       "description": "The information to analyze"             │
│     },                                                        │
│     "output_format": {                                        │
│       "type": "string",                                       │
│       "enum": ["bullet_points", "paragraphs", "table"]        │
│     }                                                         │
│   },                                                          │
│   "required": ["task", "data"]                                │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```


### **[MEM1：学习协同记忆和推理以实现高效的长视野代理 - 新加坡-麻省理工学院 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

> “我们的结果表明，推理驱动的内存整合有望成为现有解决方案的可扩展替代方案，用于训练长视野交互式代理，其中效率和性能都得到了优化。” [](https://arxiv.org/pdf/2506.15841)

![图像](https://github.com/user-attachments/assets/16e3f241-5f44-4ed5-9622-f0b4acbb67b0)


### 从 Schema 到 Prompt

通过填写结构化模板，可以将 Schema 转换为实际的提示：

```
# Analysis Request

## Task
Identify the main themes and supporting evidence in the provided text.

## Context
### Background
This is a speech given at a climate conference in 2023.

### Constraints
- Focus on scientific claims
- Ignore political statements
- Maintain neutrality

### Examples
- Theme: Rising Sea Levels
  Evidence: "Measurements show a 3.4mm annual rise since 2010"

## Data
[The full text of the speech would go here]

## Output Format
bullet_points
```

这种结构化的方法有助于模型准确理解所提供的信息以及预期的回报。

## 递归提示：自引用改进

递归提示类似于认知启动，它建立了影响后续模型行为的模式。关键的见解是让模型反思并改进自己的输出。

### 基本递归模式

```
┌───────────────────────────────────────────────────────────────┐
│ RECURSIVE PROMPTING FLOW                                      │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐    │
│  │             │      │             │      │             │    │
│  │  Initial    │─────►│  Self-      │─────►│  Improved   │    │
│  │  Response   │      │  Reflection │      │  Response   │    │
│  │             │      │             │      │             │    │
│  └─────────────┘      └─────────────┘      └─────────────┘    │
│        ▲                                          │           │
│        └──────────────────────────────────────────┘           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 简单的实施

```python
def recursive_prompt(question, model, iterations=2):
    """Apply recursive prompting to improve responses."""
    
    # Initial response
    response = model.generate(f"Question: {question}\nAnswer:")
    
    for i in range(iterations):
        # Self-reflection prompt
        reflection_prompt = f"""
        Question: {question}
        
        Your previous answer: 
        {response}
        
        Please reflect on your answer:
        1. What information might be missing?
        2. Are there any assumptions that should be questioned?
        3. How could the explanation be clearer or more accurate?
        
        Now, provide an improved answer:
        """
        
        # Generate improved response
        response = model.generate(reflection_prompt)
    
    return response
```

这种简单的递归模式可以通过鼓励模型批判和完善自己的思维来显著提高响应质量。

## 将所有内容放在一起：认知体系结构

这些认知工具可以组合成一个反映人类思维过程的完整架构：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE ARCHITECTURE                               │
│                                                                           │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Input Parser   │  Understands user intent using schema recognition    │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Prompt Program │  Selects and applies appropriate reasoning pattern   │
│  │  Selector       │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Working Memory │  Maintains state and context across steps            │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Recursive      │  Applies self-improvement through reflection         │
│  │  Processor      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Output         │  Formats final response according to schema          │
│  │  Formatter      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

这个架构可以使用我们讨论过的工具和模式作为一个完整的系统来实现。

## 关键要点

1. **提示程序/协议** 结构推理，如人类启发式
2. **Context Schemas** 组织信息，如心理知识结构
3. **递归提示** 创建类似于认知反思的自我提升循环
4. **认知架构将** 这些工具组合成完整的系统

这些对上下文工程框架的认知扩展使我们能够创建更复杂但更易于理解的 LLM 方法。

## 练习练习

1. 将您常用的提示之一转换为提示程序
2. 为使用 LLM 执行的常见任务创建简单架构
3. 实施基本的递归提示以提高响应质量
4. 将这些方法组合成一个微型认知架构

## 后续步骤

在接下来的部分中，我们将探讨这些认知工具的实际实现：
- Jupyter 笔记本演示了正在运行的提示程序
- 用于创建自己的架构的模板
- 完整认知架构的示例

[继续阅读下一部分 →](06_advanced_applications.md)

---

## 深入探讨：从我们的研究到您的应用

上述认知工具是更高级研究概念的简化表示。对于那些有兴趣进一步探索的人：

- **提示程序** 是研究人员所说的“程序化提示”或“结构化提示框架”的实际实现
- **Context Schemas** 表示知识表示系统和本体论框架的简化版本
- **递归提示** 与 AI 系统中的自我反思、元认知和递归自我提升有关

这些简化的框架使高级概念易于理解，同时保留了其实际实用性。
