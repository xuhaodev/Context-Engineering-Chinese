# 分子：将提示与示例相结合

> “整体大于其部分之和。”

## 从原子到分子

在上一节中，我们探讨了 **原子提示** — 构成 LLM 交互基本单元的单个指令。现在，我们将这些原子组合成 **分子**：结构化的上下文，其中包括模型要遵循的示例和模式。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

这种分子方法利用了 LLM 的强大功能： **小样本学习**。

## Few-Shot Learning：实例教学

小样本学习是指我们提供所需输入-输出模式的示例，允许模型识别并继续该模式。

```
┌───────────────────────────────────────────────────────────────────────┐
│ Input: "Paris"                                                         │
│ Output: "Paris is the capital of France."                              │
│                                                                        │
│ Input: "Tokyo"                                                         │
│ Output: "Tokyo is the capital of Japan."                               │
│                                                                        │
│ Input: "Ottawa"                                                        │
│ Output: ?                                                              │
└───────────────────────────────────────────────────────────────────────┘
```

该模型识别了模式并完成了它：“渥太华是加拿大的首都。

## 分子优势：可衡量的改进

让我们比较一下原子方法和分子方法来完成同一任务：

```
┌───────────────────────────────────────┬─────────────────────────────────────┐
│ ATOMIC APPROACH                       │ MOLECULAR APPROACH                   │
├───────────────────────────────────────┼─────────────────────────────────────┤
│ "Classify this review as positive     │ "Classify the sentiment of reviews.  │
│  or negative:                         │                                      │
│                                       │ Review: 'The food was amazing!'      │
│  'The service was terrible and        │ Sentiment: Positive                  │
│   the food was cold.'"                │                                      │
│                                       │ Review: 'Waited 30 minutes and       │
│                                       │  the food was cold.'                 │
│                                       │ Sentiment: Negative                  │
│                                       │                                      │
│                                       │ Review: 'The service was terrible    │
│                                       │  and the food was cold.'"            │
│                                       │ Sentiment:                           │
└───────────────────────────────────────┴─────────────────────────────────────┘
```

分子方法通常可实现：
- 更高的准确率（许多任务提高 10-30%）
- 更高的一致性（输出的差异更小）
- 更好的格式依从性
- 更清晰地处理边缘情况

## 设计有效的分子模板

分子环境的结构非常重要。以下是常见模式：

```
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ PREFIX-SUFFIX     │  │ INPUT-OUTPUT PAIRS │  │ CHAIN-OF-THOUGHT  │
├───────────────────┤  ├───────────────────┤  ├───────────────────┤
│ <instruction>     │  │ <instruction>     │  │ <instruction>     │
│                   │  │                   │  │                   │
│ Input: <example1> │  │ Input: <example1> │  │ Input: <example1> │
│ Output: <result1> │  │ Output: <result1> │  │ Thinking: <step1> │
│                   │  │                   │  │         <step2>   │
│ Input: <example2> │  │ Input: <example2> │  │ Output: <result1> │
│ Output: <result2> │  │ Output: <result2> │  │                   │
│                   │  │                   │  │ Input: <example2> │
│ Input: <new_input>│  │ Input: <new_input>│  │ Thinking: <step1> │
│ Output:           │  │ Output:           │  │         <step2>   │
└───────────────────┘  └───────────────────┘  │ Output: <result2> │
                                              │                   │
                                              │ Input: <new_input>│
                                              │ Thinking:         │
                                              └───────────────────┘
```

每个模板都有适合不同任务的优势：
- **前缀-后缀**：最简单，适用于简单的任务
- **输入-输出对**：清晰的分界，适用于结构化数据
- **Chain-of-Thought**：揭示推理步骤，最适合复杂任务

## 示例选择的科学

并非所有示例都是平等的。为您的分子环境选择示例时：

```
┌──────────────────────────────────────────────────────────────┐
│ EXAMPLE SELECTION STRATEGIES                                 │
├──────────────────────────────────────────────────────────────┤
│ ✓ Cover diverse cases to show range                          │
│ ✓ Include edge cases that clarify boundaries                 │
│ ✓ Order from simple to complex when possible                 │
│ ✓ Use recent or common examples (recency and frequency bias) │
│ ✓ Include near-misses to establish precise boundaries        │
└──────────────────────────────────────────────────────────────┘
```

## 测量分子效率

随着上下文大小的增加，令牌计数也会增加。让我们凭经验来衡量权衡：

```
                   [Accuracy]
                       ▲
                       │
                       │                  ● 4-shot
                       │
                       │              ● 3-shot
                       │
                       │          ● 2-shot
                       │
                       │      ● 1-shot
                       │
                       │  ● 0-shot
                       │
                       └────────────────────────►
                                [Tokens]
```

关键见解： **收益递减**。每个额外的示例都会消耗代币，但产生的改进比前一个少。

## 寻找分子最佳位置

对于大多数任务，有一个最佳数量的示例可以平衡质量和令牌效率：

```
┌─────────────────────────────────────────────────────────────────┐
│ EXAMPLE COUNT HEURISTICS BY TASK TYPE                           │
├───────────────────────────┬─────────────────────────────────────┤
│ Classification            │ 1-3 examples per class              │
├───────────────────────────┼─────────────────────────────────────┤
│ Generation                │ 2-5 examples                        │
├───────────────────────────┼─────────────────────────────────────┤
│ Structured Extraction     │ 2-4 examples covering all fields    │
├───────────────────────────┼─────────────────────────────────────┤
│ Reasoning                 │ 2-3 examples with thinking steps    │
├───────────────────────────┼─────────────────────────────────────┤
│ Translation               │ 3-5 examples with varying complexity│
└───────────────────────────┴─────────────────────────────────────┘
```

## 动态分子构建

高级上下文工程涉及为每个输入动态选择最相关的示例：

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   User Query                                                      │
│       │                                                           │
│       ▼                                                           │
│  ┌─────────────┐      ┌─────────────────┐                         │
│  │ Query       │      │                 │                         │
│  │ Analysis    │─────▶│ Example         │                         │
│  │             │      │ Database        │                         │
│  └─────────────┘      │                 │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │ Retrieve most                      │
│                              │ similar examples                   │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │ Dynamic         │                         │
│                       │ Molecular       │                         │
│                       │ Context         │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │                                    │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │                 │                         │
│                       │ LLM             │                         │
│                       │                 │                         │
│                       └─────────────────┘                         │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

这种方法：
1. 分析用户查询
2. 检索最相关的示例
3. 构建量身定制的分子环境
4. 将优化的上下文发送到 LLM

## 付诸实践：一个简单的实现

这是一个 Python 函数，它从示例中构建了一个分子上下文：

```python
def create_molecular_context(instruction, examples, new_input, 
                            format_type="input-output"):
    """
    Construct a molecular context from examples.
    
    Args:
        instruction (str): The task instruction
        examples (List[Dict]): List of example input/output pairs
        new_input (str): The new input to process
        format_type (str): Template type (input-output, chain-of-thought)
    
    Returns:
        str: The complete molecular context
    """
    context = f"{instruction}\n\n"
    
    # Add examples based on format type
    if format_type == "input-output":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Output: {example['output']}\n\n"
    elif format_type == "chain-of-thought":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Thinking: {example['thinking']}\n"
            context += f"Output: {example['output']}\n\n"
    
    # Add the new input
    context += f"Input: {new_input}\nOutput:"
    
    return context
```

## 关键要点

1. **分子环境** 将指令与示例相结合以提高 LLM 性能
2. **小样本学习** 允许模型识别并继续模式
3. **模板结构** 很重要;不同的格式更适合不同的任务
4. **示例选择** 是一门科学;多样性、边缘情况和排序都很重要
5. **存在收益递减**;每增加一个示例，收益就会递减
6. **动态构造** 可以优化每个特定输入的上下文

## 练习练习

1. 执行一个简单的分类任务，并使用 0、1、3 和 5 个示例来衡量性能
2. 比较同一任务的不同模板结构
3. 根据与新输入的相似性实现动态示例选择
4. 为您关心的任务找到“最小可行分子”

## 后续步骤

在下一节中，我们将探索 **cells** — 在多个交互中维护内存和状态的上下文结构。

[继续 03_cells_memory.md →](03_cells_memory.md)

---

## 深入探讨：提示工程与情境工程

Prompt Engineering 专注于制作完美的指令。上下文工程包括这些以及更多：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT ENGINEERING LAYERS                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────┐                                               │
│   │ State & Memory  │  Conversation history, persistent variables   │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Retrieved Data  │  RAG, tool outputs, external knowledge        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Examples        │  Few-shot learning, demonstrations            │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Instructions    │  Prompts, system messages, constraints        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Model Behavior  │  Training data, alignments, capabilities      │
│   └─────────────────┘                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

上下文工程让您可以控制更多这些层，从而获得更强大的应用程序。
