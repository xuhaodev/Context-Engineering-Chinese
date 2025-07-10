# 验证模板

> “信任，但要验证。”— 俄罗斯谚语

## 概述

验证模板可帮助语言模型检查自己的工作、捕获错误并确保其输出的质量。这些模板对于提高可靠性、减少幻觉和提高整体准确性至关重要。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  VERIFICATION PROCESS                                        │
│                                                              │
│  Solution → Check Logic → Test Assumptions → Correct → Final │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 基本模板

### 1. 解决方案验证

用于检查解决方案或答案的基本模板。

```markdown
# Solution Verification Template

Task: Verify the correctness of the following solution.

Problem: {{problem}}
Proposed Solution: {{solution}}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
```

**Token Count**：~160 个代币（仅限模板）

**使用示例**：
- 对于数学解决方案
- 检查逻辑参数时
- 适用于精度至关重要的任何输出

### 2. 事实核查

用于验证事实声明和陈述。

```markdown
# Fact Checking Template

Task: Verify the accuracy of the following statement(s).

Statement(s): {{statements}}

Please follow this verification process:
1. **Break Down Claims**: Identify each distinct factual claim.
2. **Assess Knowledge Base**: Determine if you have reliable information about each claim.
3. **Verify Each Claim**:
   - Claim 1: [Restate the claim]
     - Assessment: [Accurate / Inaccurate / Partially Accurate / Uncertain]
     - Explanation: [Provide relevant facts and context]
     - Confidence: [High / Medium / Low]
   - Claim 2: [Continue for each claim]
4. **Check for Omissions**: Identify any relevant context that's missing.
5. **Overall Assessment**: Summarize the overall accuracy.
6. **Knowledge Limitations**: Note any claims you cannot verify with confidence.

Provide corrections for any inaccurate information.
```

**Token Count**：~150 个代币（仅限模板）

**使用示例**：
- 用于检查历史或科学声明
- 验证摘要中的信息时
- 对于包含事实断言的任何输出

### 3. 一致性检查

确保内容的内部一致性。

```markdown
# Consistency Check Template

Task: Check the following content for internal consistency.

Content: {{content}}

Please follow this verification process:
1. **Identify Key Elements**: Note the main claims, definitions, and arguments.
2. **Create Consistency Map**:
   - Element 1: [Description]
   - Element 2: [Description]
   - [Continue for all important elements]
3. **Check for Contradictions**:
   - Between Elements: Compare each element with others for compatibility
   - Within Elements: Check each element for internal contradictions
4. **Temporal Consistency**: Ensure events and developments follow a logical timeline.
5. **Terminology Consistency**: Verify that terms are used consistently throughout.
6. **Logical Flow**: Check that conclusions follow from premises.
7. **Final Assessment**: Summarize any inconsistencies found.

For each inconsistency, explain the contradiction and suggest a resolution.
```

**Token Count**：~160 个代币（仅限模板）

**使用示例**：
- 对于长篇内容
- 检查复杂参数时
- 对于基于多个本地构建的任何输出

## 高级模板

### 4. 综合误差分析

用于详细检查多个维度的潜在错误。

```markdown
# Comprehensive Error Analysis Template

Task: Perform a thorough error analysis on the following content.

Content: {{content}}
Context: {{context}}

Please examine for these error types:
1. **Factual Errors**:
   - Incorrect statements: [Identify and correct]
   - Outdated information: [Identify and update]
   - Misattributed statements: [Identify and correct]

2. **Logical Errors**:
   - False equivalences: [Identify]
   - Non sequiturs: [Identify]
   - Circular reasoning: [Identify]
   - Hasty generalizations: [Identify]

3. **Mathematical/Computational Errors**:
   - Calculation mistakes: [Identify and correct]
   - Formula application errors: [Identify and correct]
   - Unit conversion issues: [Identify and correct]

4. **Contextual Errors**:
   - Misunderstanding of context: [Clarify]
   - Inappropriate assumptions: [Identify]
   - Missing relevant information: [Supply]

5. **Linguistic Errors**:
   - Ambiguous statements: [Clarify]
   - Incorrect terminology: [Correct]
   - Inconsistent language: [Standardize]

6. **Structural Errors**:
   - Organizational problems: [Identify]
   - Missing components: [Identify]
   - Redundancies: [Identify]

For each error found, explain:
- What the error is
- Why it's problematic
- How it should be corrected

Conclude with an overall assessment of the content's accuracy and reliability.
```

**Token Count**：~240 个代币（仅限模板）

**使用示例**：
- 用于对重要内容的批判性审查
- 当需要最大精度时
- 用于同行评审或编辑流程

### 5. 另类视角分析

用于检查偏见和探索其他观点。

```markdown
# Alternative Perspective Analysis Template

Task: Analyze the following content from alternative perspectives to check for bias or blind spots.

Content: {{content}}

Please follow this process:
1. **Identify the Content's Perspective**: What worldview, assumptions, or values underlie the content?

2. **Explore Alternative Perspectives**:
   - Perspective A: [Description of a different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - Perspective B: [Description of another different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - [Continue with additional relevant perspectives]

3. **Identify Blind Spots**: What important considerations are missing from the original content?

4. **Check for Unstated Assumptions**: What does the content take for granted that might be questioned?

5. **Balance Assessment**: Is the content fair and balanced, or does it favor certain perspectives?

6. **Recommendations**: Suggest modifications that would make the content more comprehensive and balanced.

This analysis helps ensure that the content accounts for diverse viewpoints and avoids unintentional bias.
```

**Token Count**：~220 个代币（仅限模板）

**使用示例**：
- 用于策略分析
- 检查是否存在文化或意识形态偏见时
- 对于涉及有争议主题的任何内容

### 6. 实施验证

用于检查解决方案是否确实可以实施。

```markdown
# Implementation Verification Template

Task: Verify that the following solution can be practically implemented.

Proposed Solution: {{solution}}
Implementation Context: {{context}}

Please follow this verification process:
1. **Feasibility Assessment**:
   - Technical feasibility: Can this be built with available technology?
   - Resource requirements: What resources (time, money, skills) would be needed?
   - Scalability: Would the solution work at the required scale?

2. **Constraints Check**:
   - Technical constraints: Does the solution respect technical limitations?
   - Regulatory constraints: Does it comply with relevant regulations?
   - Operational constraints: Can it be implemented within operational parameters?

3. **Risk Analysis**:
   - Implementation risks: What could go wrong during implementation?
   - Operational risks: What could go wrong once implemented?
   - Mitigation strategies: How could these risks be addressed?

4. **Dependency Analysis**:
   - External dependencies: What does this solution depend on?
   - Critical path: Which dependencies are on the critical path?
   - Vulnerability points: Where could dependencies cause problems?

5. **Testing Approach**:
   - Validation methods: How could the implementation be tested?
   - Success criteria: How would success be measured?
   - Failure scenarios: How would failures be detected and addressed?

6. **Overall Assessment**: Is the solution implementable as described? What modifications would improve implementability?

This verification ensures that solutions are not just theoretically sound but practically viable.
```

**Token Count**：~240 个代币（仅限模板）

**使用示例**：
- 对于工程解决方案
- 评估项目提案时
- 适用于任何需要实际实施的解决方案

## 实现模式

下面是一个用于实现 Solution Verification 模板的简单 Python 函数：

```python
def verify_solution(problem, solution):
    """
    Create a prompt that verifies a proposed solution.
    
    Args:
        problem (str): The original problem
        solution (str): The proposed solution to verify
        
    Returns:
        str: A formatted prompt for solution verification
    """
    return f"""
Task: Verify the correctness of the following solution.

Problem: {problem}
Proposed Solution: {solution}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
"""
```

## 自校正循环

验证模板最强大的应用之一是自我更正循环：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Initial Solution                                                   │
│       │                                                             │
│       ▼                                                             │
│  Apply Verification Template                                        │
│       │                                                             │
│       ▼                                                             │
│  Errors Found?                                                      │
│       │                                                             │
│       ├─────────────Yes─────────────┐                               │
│       │                             │                               │
│       ▼                             ▼                               │
│  No   │                        Apply Corrections                    │
│       │                             │                               │
│       ▼                             ▼                               │
│  Final Verified Solution ◄──────────┘                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

实现示例：

```python
def self_correction_loop(problem, max_iterations=3):
    """
    Implement a self-correction loop for problem solving.
    
    Args:
        problem (str): The problem to solve
        max_iterations (int): Maximum number of correction iterations
        
    Returns:
        dict: The final solution and verification history
    """
    # Initial solution
    solution = llm.generate(f"Solve this problem: {problem}")
    
    history = [{"type": "solution", "content": solution}]
    iteration = 0
    
    while iteration < max_iterations:
        # Verify the current solution
        verification = llm.generate(verify_solution(problem, solution))
        history.append({"type": "verification", "content": verification})
        
        # Check if corrections are needed
        if "Correct: The solution is completely accurate" in verification:
            break
        
        # Generate corrected solution
        correction_prompt = f"""
        Based on the verification feedback below, provide a corrected solution to the original problem.
        
        Original Problem: {problem}
        
        Previous Solution: {solution}
        
        Verification Feedback: {verification}
        
        Please provide a fully corrected solution that addresses all issues identified in the verification.
        """
        
        corrected_solution = llm.generate(correction_prompt)
        history.append({"type": "correction", "content": corrected_solution})
        
        # Update solution for next iteration
        solution = corrected_solution
        iteration += 1
    
    return {
        "problem": problem,
        "final_solution": solution,
        "verification_history": history,
        "iterations": iteration
    }
```

## 测量和优化

使用验证模板时，请通过以下方式衡量其有效性：

1. **错误检测率**：捕获到的注入错误百分比是多少？
2. **误报率**：错误标记正确元素的频率如何？
3. **更正质量**：建议的更正效果如何？
4. **迭代效率**：需要多少次迭代才能得到正确的解决方案？

通过以下方式优化您的模板：
- 为专业域添加特定于域的验证步骤
- 根据准确性的重要性调整审查级别
- 关注特定任务的常见错误类型

## 与其他工具结合使用

验证模板完成了认知工作流：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
          ▲                                                │
          │                                                │
          └────────────────────────────────────────────────┘
                        (Correction Loop)
```

这创建了一个完整的认知系统，该系统可以：
1. 了解问题
2. 生成解决方案
3. 验证并更正解决方案
4. 迭代，直到获得满意的结果

## 后续步骤

- 探索 [composition.md](./composition.md) 以了解组合多个模板的方法
- 看看这些模板如何可以集成到完整的认知程序中 [。/认知程序/basic-programs.md](../cognitive-programs/basic-programs.md)
- 了解完整的认知架构 [/cognitive-architectures/solver-architecture.md 中](../cognitive-architectures/solver-architecture.md)
