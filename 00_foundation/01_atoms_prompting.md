# 原子：提示的基本单位

> “如果你想从头开始制作苹果派，你必须首先发明宇宙。”

## 原子：单一指令

在我们的上下文工程之旅中，我们从最基本的单元开始： **原子** — LLM 的单个独立指令。

```
┌───────────────────────────────────────────────┐
│                                               │
│  "Write a poem about the ocean in 4 lines."   │
│                                               │
└───────────────────────────────────────────────┘
```

这是最纯粹的提示工程形式：一个人，一条指令，一个模型响应。简单、直接、原子。

## 原子提示剖析

让我们分解一下什么是有效的原子提示：

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ATOMIC PROMPT = [TASK] + [CONSTRAINTS] + [OUTPUT FORMAT]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

例如：

```
┌─────────────────────┬────────────────────────┬────────────────────┐
│        TASK         │      CONSTRAINTS       │   OUTPUT FORMAT    │
├─────────────────────┼────────────────────────┼────────────────────┤
│ "Write a poem       │ "about the ocean       │ "in 4 lines."      │
│  about space."      │  using only words      │                    │
│                     │  with 5 letters        │                    │
│                     │  or less."             │                    │
└─────────────────────┴────────────────────────┴────────────────────┘
```

## 原子的局限性

虽然原子提示是 LLM 交互的构建块，但它们很快就会揭示出基本的局限性：

```
┌──────────────────────────────────────┐
│ LIMITATIONS OF ATOMIC PROMPTS        │
├──────────────────────────────────────┤
│ ✗ No memory across interactions      │
│ ✗ Limited demonstration capability   │
│ ✗ No complex reasoning scaffolds     │
│ ✗ Prone to ambiguity                 │
│ ✗ High variance in outputs           │
└──────────────────────────────────────┘
```

让我们通过一个简单的实验来实证地衡量这一点：

```python
# A basic atomic prompt
atomic_prompt = "List 5 symptoms of diabetes."

# Send to LLM multiple times
responses = [llm.generate(atomic_prompt) for _ in range(5)]

# Measure variability
unique_symptoms = set()
for response in responses:
    symptoms = extract_symptoms(response)
    unique_symptoms.update(symptoms)

print(f"Found {len(unique_symptoms)} unique symptoms across 5 identical prompts")
# Typically outputs far more than just 5 unique symptoms
```

问题是什么？即使使用相同的原子提示，我们每次都会得到不同的响应。当给定最少的上下文时，模型难以保持一致性。

## 单原子基线：有用但有限

尽管存在局限性，但原子提示会建立我们的基线。他们帮助我们：

1. 衡量代币效率（最小开销）
2. 基准响应质量
3. 建立实验对照

```
                     [Response Quality]
                            ▲
                            │
                            │               ⭐ Context
                            │                 Engineering
                            │               
                            │           
                            │       ⭐ Advanced
                            │         Prompting
                            │
                            │   ⭐ Basic Prompting
                            │
                            │
                            └────────────────────────►
                                  [Complexity]
```

## 不言而喻的背景：模型已经“知道”什么

即使使用原子提示符，LLM 也会从他们的训练中利用大量的隐式上下文：

```
┌───────────────────────────────────────────────────────────────┐
│ IMPLICIT CONTEXT IN MODELS                                    │
├───────────────────────────────────────────────────────────────┤
│ ✓ Language rules and grammar                                  │
│ ✓ Common knowledge facts                                      │
│ ✓ Format conventions (lists, paragraphs, etc.)                │
│ ✓ Domain-specific knowledge (varies by model)                 │
│ ✓ Learned interaction patterns                                │
└───────────────────────────────────────────────────────────────┘
```

这种隐含知识为我们提供了基础，但它并不可靠，并且因模型和版本而异。

## 幂律：代币质量曲线

对于许多任务，我们观察到上下文标记和输出质量之间的幂律关系：

```
    Quality
      ▲
      │
      │    •
      │        •
      │            •
      │                •
      │                    •
      │                        •         •         •
      │                             
      └───────────────────────────────────────────► Tokens
                                      
          [Maximum ROI Zone]       [Diminishing Returns]
```

关键见解：有一个“最大 ROI 区域”，只需添加几个代币即可显著提高质量。

## 从原子到分子：需要更多背景

原子的局限性自然而然地引导我们进行下一步： **分子**，或将说明与示例、附加上下文和结构化格式相结合的多部分提示。

以下是基本转换：

```
┌──────────────────────────┐         ┌──────────────────────────┐
│                          │         │ "Here's an example:      │
│ "Write a limerick about  │    →    │  There once was a...     │
│  a programmer."          │         │                          │
│                          │         │  Now write a limerick    │
└──────────────────────────┘         │  about a programmer."    │
                                     └──────────────────────────┘
    [Atomic Prompt]                       [Molecular Prompt]
```

通过添加示例和结构，我们开始有意识地塑造上下文窗口 - 这是上下文工程的第一步。

## 测量原子效率：您的首要任务

在继续之前，请尝试以下简单练习：

1. 完成你给 LLM 的基本任务
2. 创建三个不同的原子提示符版本
3. 衡量使用的标记和主观质量
4. 绘制效率边界

```
┌─────────────────────────────────────────────────────────────┐
│ Task: Summarize a news article                              │
├─────────┬───────────────────────────────┬────────┬──────────┤
│ Version │ Prompt                        │ Tokens │ Quality  │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ A       │ "Summarize this article."     │ 4      │ 2/10     │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ B       │ "Provide a concise summary    │ 14     │ 6/10     │
│         │  of this article in 3         │        │          │
│         │  sentences."                  │        │          │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ C       │ "Write a summary of the key   │ 27     │ 8/10     │
│         │  points in this article,      │        │          │
│         │  highlighting the main        │        │          │
│         │  people and events."          │        │          │
└─────────┴───────────────────────────────┴────────┴──────────┘
```

## 关键要点

1. **原子提示符** 是 LLM 交互的基本单元
2. 它们遵循一个基本结构：任务 + 约束 + 输出格式
3. 它们有固有的局限性：没有记忆、示例或推理支架
4. 即使是简单的原子提示也利用了模型的隐式知识
5. 上下文标记和质量之间存在幂律关系
6. 超越原子是迈向上下文工程的第一步

## 后续步骤

在下一节中，我们将探讨如何将原子组合成 **分子** — 小样本学习模式可显著提高可靠性和控制。

[继续访问 02_molecules_context.md →](02_molecules_context.md)

---

## 深入探讨：提示模板

对于那些想要更多地尝试原子提示的人，这里有一些模板可以尝试：

```
# Basic instruction
{task}

# Persona-based
As a {persona}, {task}

# Format-specific
{task}
Format: {format_specification}

# Constraint-based
{task}
Constraints:
- {constraint_1}
- {constraint_2}
- {constraint_3}

# Step-by-step guided
{task}
Please follow these steps:
1. {step_1}
2. {step_2}
3. {step_3}
```

尝试测量应用于同一任务的每个模板的令牌计数和质量！
