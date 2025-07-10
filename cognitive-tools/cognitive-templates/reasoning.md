# 推理模板

> “逻辑是思想的解剖学。”

## 概述

推理模板通过结构化的思维过程指导语言模型解决问题、生成见解或做出决策。这些模板通过提供系统的方法来处理信息和得出结论，从而建立在理解模板的基础上。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  REASONING PROCESS                                           │
│                                                              │
│  Input → Structure → Apply Logic → Step-by-Step → Conclusion │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 基本模板

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

**使用示例**：
- 用于解决数学问题
- 处理复杂的逻辑参数时
- 对于任何需要透明推理的任务

### 2. 比较和对比

用于评估相似性和差异性的分析推理。

```markdown
# Compare and Contrast Template

Task: Analyze the similarities and differences between the following items.

Items to Compare: {{item_a}} and {{item_b}}

Please follow this structured approach:
1. **Background**: Briefly introduce both items and their context.
2. **Criteria Selection**: Identify the key dimensions for comparison.
3. **Systematic Comparison**:
   - Dimension 1: [Explain how both items relate to this dimension]
   - Dimension 2: [Explain how both items relate to this dimension]
   - Dimension 3: [Continue with additional dimensions as needed]
4. **Key Similarities**: Explicitly list the most important similarities.
5. **Key Differences**: Explicitly list the most important differences.
6. **Synthesis**: Explain what these similarities and differences reveal.
7. **Conclusion**: Summarize the most significant insights from this comparison.
```

**Token Count**：~140 个代币（仅限模板）

**使用示例**：
- 用于比较理论、产品或方法
- 分析竞争解决方案时
- 用于评估替代解释

### 3. 因果分析

用于推理因果关系。

```markdown
# Causal Analysis Template

Task: Analyze the causes and effects related to the following situation or phenomenon.

Situation: {{situation}}

Please follow this structured approach:
1. **Describe the Phenomenon**: Clearly state what needs to be explained.
2. **Identify Potential Causes**:
   - Immediate Causes: [Direct factors that led to the situation]
   - Underlying Causes: [Deeper factors that created conditions for the situation]
   - Contributory Factors: [Elements that amplified or enabled the causes]
3. **Evaluate Each Cause**:
   - Evidence: [What evidence supports this as a cause?]
   - Significance: [How important was this cause?]
   - Mechanism: [How did this cause lead to the effect?]
4. **Analyze Effects**:
   - Immediate Effects: [Direct consequences]
   - Long-term Effects: [Ongoing or future consequences]
   - Secondary Effects: [Indirect consequences]
5. **Examine Interactions**: How do these causes and effects interact with each other?
6. **Conclusion**: Summarize the most significant causal relationships.
```

**Token Count**：~160 个代币（仅限模板）

**使用示例**：
- 用于历史分析
- 研究复杂系统时
- 用于理解社会或经济现象

## 高级模板

### 4. 假设检验

根据证据系统地评估假设。

```markdown
# Hypothesis Testing Template

Task: Systematically evaluate the following hypothesis based on available evidence.

Hypothesis: {{hypothesis}}

Evidence: {{evidence}}

Please follow this structured approach:
1. **Clarify the Hypothesis**: Restate the hypothesis in precise terms.
2. **Identify Testable Predictions**: What should be true if the hypothesis is correct?
3. **Evaluate Evidence**:
   - Supporting Evidence: [Evidence that confirms predictions]
     - Strength: [How strongly does this evidence support the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Contradictory Evidence: [Evidence that contradicts predictions]
     - Strength: [How strongly does this evidence oppose the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Missing Evidence: [Evidence that should exist but isn't present]
4. **Consider Alternative Hypotheses**: What other explanations could account for the evidence?
5. **Weigh Comparative Explanatory Power**: How well does the hypothesis explain the evidence compared to alternatives?
6. **Conclusion**: Assess the overall credibility of the hypothesis.
7. **Confidence Level**: Indicate your level of confidence in this assessment.
```

**Token Count**：~180 个代币（仅限模板）

**使用示例**：
- 用于科学推理
- 评估理论或主张时
- 用于循证决策

### 5. 决策矩阵

用于跨多个标准的结构化决策。

```markdown
# Decision Matrix Template

Task: Evaluate options against criteria to make a structured decision.

Decision Context: {{decision_context}}
Options: {{options}}
Criteria: {{criteria}}

Please follow this structured approach:
1. **Define the Decision**: Clearly state what decision needs to be made.
2. **Establish Criteria Weights**:
   - Criterion 1: [Importance weight (1-10)]
   - Criterion 2: [Importance weight (1-10)]
   - [Continue for all criteria]
3. **Evaluate Each Option**:
   Create a matrix with options as rows and criteria as columns.
   
   | Option | Criterion 1 | Criterion 2 | ... | Total |
   |--------|-------------|-------------|-----|-------|
   | Option A | [Score] | [Score] | ... | [Sum] |
   | Option B | [Score] | [Score] | ... | [Sum] |
   
   For each cell, provide:
   - Score: [Rating (1-10)]
   - Justification: [Brief explanation]
   
4. **Calculate Weighted Scores**: Multiply each score by the criterion weight.
5. **Rank Options**: Order options based on their total weighted scores.
6. **Sensitivity Analysis**: How would the ranking change if weights were adjusted?
7. **Recommendation**: State the recommended option with justification.
```

**Token Count**：~180 个代币（仅限模板）

**使用示例**：
- 在备选方案之间进行选择
- 平衡多个因素时
- 用于透明的决策流程

### 6. 论点构建

用于构建结构良好的论点。

```markdown
# Argument Construction Template

Task: Construct a well-reasoned argument for the following position.

Position: {{position}}

Please follow this structured approach:
1. **Thesis Statement**: Clearly articulate the main claim or position.
2. **Define Key Terms**: Clarify any ambiguous or technical terms.
3. **Establish Premises**:
   - Premise 1: [State first supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - Premise 2: [State second supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - [Continue with additional premises as needed]
4. **Logical Structure**: Explain how these premises lead to the conclusion.
5. **Address Counterarguments**:
   - Counterargument 1: [Potential objection]
     - Response: [Rebuttal or accommodation]
   - Counterargument 2: [Potential objection]
     - Response: [Rebuttal or accommodation]
6. **Conclusion**: Restate the thesis and summarize the supporting arguments.
```

**Token Count**：~170 个代币（仅限模板）

**使用示例**：
- 用于有说服力的写作
- 制定立场文件时
- 用于构造逻辑 case

## 实现模式

下面是一个用于实现 Step-by-Step Reasoning 模板的简单 Python 函数：

```python
def step_by_step_reasoning(problem, steps=None):
    """
    Create a prompt that guides through step-by-step reasoning.
    
    Args:
        problem (str): The problem to solve
        steps (list, optional): Custom steps for the reasoning process
        
    Returns:
        str: A formatted prompt for step-by-step reasoning
    """
    if steps is None:
        steps = [
            "Understand: Restate the problem and identify what you need to find.",
            "Plan: Outline your approach to solving the problem.",
            "Execute: Work through each step of your plan in detail.",
            "Verify: Check your solution against the original problem.",
            "Conclude: State your final answer or conclusion clearly."
        ]
    
    steps_text = "\n".join([f"{i+1}. **{step.split(':', 1)[0]}**:{step.split(':', 1)[1]}" 
                           for i, step in enumerate(steps)])
    
    return f"""
Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {problem}

Please follow this process:
{steps_text}

Show all your work and explain your reasoning at each step.
"""
```

## 测量和优化

使用推理模板时，请通过以下方式衡量其有效性：

1. **逻辑效度**：结论是否得到前提的适当支持？
2. **完整性**：推理是否解决了问题的所有方面？
3. **透明度**：每个步骤是否得到明确解释和合理解释？
4. **效率**：推理是否采用直接路径找到解决方案？
5. **正确性**：推理是否导致正确的答案或结论？

通过以下方式优化您的模板：
- 根据问题复杂度调整细节级别
- 为专业域添加特定于域的推理步骤
- 为特定类型的问题定制评估标准

## 与其他工具结合使用

推理模板作为完整认知工作流的一部分效果最佳：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```

例如，使用 Understanding 模板分析问题，应用 Reasoning 模板解决问题，然后使用 Verification 模板检查解决方案。

## 高级推理模式

对于复杂问题，请考虑以下高级模式：

### 分而治之

将问题分解为独立的子问题，分别解决每个子问题，然后组合结果。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Main Problem                                                 │
│       │                                                       │
│       ├────────────────┬────────────────┬────────────────┐    │
│       │                │                │                │    │
│       ▼                ▼                ▼                ▼    │
│  Sub-Problem 1    Sub-Problem 2    Sub-Problem 3    Sub-Problem 4 │
│       │                │                │                │    │
│       ├────────────────┼────────────────┼────────────────┘    │
│       │                │                │                     │
│       ▼                ▼                ▼                     │
│  Combine Solutions and Integrate Results                      │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 迭代优化

从简单的解决方案开始，然后迭代改进它。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Initial Solution                                             │
│       │                                                       │
│       ▼                                                       │
│  Identify Weaknesses                                          │
│       │                                                       │
│       ▼                                                       │
│  Improve Solution           ◄─────────────┐                   │
│       │                                    │                   │
│       ▼                                    │                   │
│  Evaluate Improvement                      │                   │
│       │                                    │                   │
│       └────────────────────────────────────┘                   │
│       │                                                        │
│       ▼                                                        │
│  Final Solution (when satisfactory)                            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 类比推理

将已知域中的推理模式应用于新问题。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Target Problem                                               │
│       │                                                       │
│       ▼                                                       │
│  Identify Similar Solved Problem                              │
│       │                                                       │
│       ▼                                                       │
│  Map Elements from Solved Problem to Target Problem           │
│       │                                                       │
│       ▼                                                       │
│  Apply Similar Solution Strategy                              │
│       │                                                       │
│       ▼                                                       │
│  Adapt as Needed for Target Problem                           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## 后续步骤

- 探索 [verification.md](./verification.md) 以获取检查推理的模板
- 请参阅 [composition.md](./composition.md) 了解组合多个模板的方法
- 查看 [../cognitive-programs/advanced-programs.md](../cognitive-programs/advanced-programs.md) 获取利用这些推理模式的编程方法
