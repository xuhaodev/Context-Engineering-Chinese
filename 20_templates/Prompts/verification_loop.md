# 验证循环模板

## 总结
一个模板，用于实施自我验证流程，这些流程通过结构化检查机制来捕获错误、验证结果并提高整体可靠性。

## 背景和应用
当准确性至关重要并且您希望在推理过程中构建显式验证时，请使用此模板。验证循环鼓励在最终结果之前对假设、计算和结论进行系统检查，从而减少错误。

此模板非常适合：
- 高风险任务，错误可能代价高昂
- 复杂的计算或逻辑推理链
- 容易出现常见推理谬误的情况
- 彻底性比速度更重要的情况
- 结果的可验证性很重要的任何任务

## 模板结构

```
# Task: {{task_description}}

## Approach
Complete this task using a verification loop:

1. Initial Solution
   - {{solution_approach}}
   - Develop your initial answer

2. Verification Process
   - Check assumptions: {{assumption_verification}}
   - Verify calculations/logic: {{process_verification}}
   - Test edge cases: {{edge_case_verification}}
   - Consider alternatives: {{alternative_verification}}

3. Error Correction
   - Identify any issues found during verification
   - Make necessary corrections

4. Final Answer
   - Present your verified solution
   - Note any uncertainty or limitations

## Expected Output
Show your complete process including initial solution, verification steps, any corrections, and final verified answer.
```

## 参数

- `{{task_description}}`：要完成的任务的明确描述
- `{{solution_approach}}`：用于初始解的方法（例如，“使用代数方程”）
- `{{assumption_verification}}`：如何验证假设（例如，“确认所有变量都被正确解释”）
- `{{process_verification}}`：如何检查计算或逻辑（例如，“使用其他方法重新计算”）
- `{{edge_case_verification}}`：要检查的特定边缘情况（例如，“使用边界值测试”）
- `{{alternative_verification}}`： 验证结果的替代方法（例如，“使用不同的技术解决”）

## 例子

### 示例 1：数学问题验证

```
# Task: Calculate the future value of an investment of $10,000 with an annual interest rate of 5% compounded monthly over 10 years.

## Approach
Complete this task using a verification loop:

1. Initial Solution
   - Use the compound interest formula: P(1 + r/n)^(nt)
   - Calculate the result with the given values

2. Verification Process
   - Check assumptions: Verify the formula is appropriate for this problem
   - Verify calculations: Recalculate step by step, checking each arithmetic operation
   - Test edge cases: Calculate for 1 year and confirm it matches expected growth
   - Consider alternatives: Calculate using the FV = P * e^(rt) formula as a cross-check

3. Error Correction
   - Identify any discrepancies between the two calculation methods
   - Check for common errors (decimal place mistakes, incorrect exponents)
   - Make corrections if needed

4. Final Answer
   - Present the verified future value
   - Express with appropriate precision and units

## Expected Output
Show your complete process including initial solution, verification steps, any corrections, and final verified answer.
```

### 示例 2：代码审查验证

```
# Task: Review the following Python function that calculates the factorial of a number and identify any bugs or issues.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

## 方法
使用验证循环完成此任务：

1. 初步审查
   - 逐行分析代码
   - 确定实施中的任何潜在问题

2. 验证流程
   - 检查假设：验证递归方法是否合适
   - 验证逻辑：跟踪样本输入的执行情况（n=3、n=0）
   - 测试边缘情况：考虑负数、大输入和非整数输入
   - 考虑替代方案：与迭代实现进行比较

3. 问题识别
   - 列出发现的所有错误、边缘情况或性能问题
   - 按严重性（严重、中等、次要）对问题进行分类

4. 最终评估
   - 提供经过验证的代码质量评估
   - 提出具体的改进或修复建议

## 预期输出
展示您的完整流程，包括初始审核、验证步骤、发现的问题以及带有建议的最终评估。
```

## Variations

### Triple Check Verification
For critical tasks requiring multiple verification approaches:

```
# 任务：{{task_description}}

## 方法
通过三重验证完成此任务：

1. 初始解决方案
   - {{solution_approach}}

2. 第一次验证：替代方法
   - 使用不同的方法解决相同的问题
   - 将结果与初始解决方案进行比较

3. 第二次验证：误差分析
   - 识别两种方法中的潜在错误源
   - 检查这些特定错误

4. 第三次验证：测试用例
   - 使用 {{test_case_1}} 进行测试
   - 使用 {{test_case_2}} 进行测试

5. 最终答案
   - 协调验证方法之间的任何差异
   - 提供经过验证的最终解决方案

## 预期输出
包含所有三种验证方法的完整过程和最终对账答案。
```

### Peer Review Simulation
For stimulating different perspectives on the same problem:

```
# 任务：{{task_description}}

## 方法
模拟同行评审过程：

1. 初始解决方案
   - 使用 {{primary_method}} 解决问题

2. 审稿人 A Perspective
   - 从 {{reviewer_A_expertise}} 的角度批判性地检查解决方案
   - 确定潜在问题或改进

3. 审阅者 B 透视
   - 从 {{reviewer_B_expertise}} 的角度检查解决方案
   - 确定不同的潜在问题或改进

4. 和解
   - 解决所有提出的问题
   - 采纳有效的建议

5. 最终解决方案
   - 在审阅后提出改进的解决方案

## 预期输出
初始解决方案，包括审阅者视角、对账流程和最终改进的解决方案。
```

### Progressive Refinement Verification
For iteratively improving solutions:

```
# 任务：{{task_description}}

## 方法
使用渐进式细化：

1. 草稿解决方案（第 1 版）
   - 快速首次尝试解决问题

2. 版本 1 的分析
   - 确定弱点和改进领域

3. 优化解决方案 （版本 2）
   - 解决已发现的问题

4. 版本 2 的验证
   - 根据原始要求进行测试
   - 检查引入的新问题

5. 最终解决方案（第 3 版）
   - 进行最终优化
   - 验证完整性和正确性

## 预期输出
所有三个版本都有版本之间的分析和验证步骤。
```

## Best Practices

- **Use different methods for verification** than for the initial solution
- **Include both conceptual and computational verification** - check both the approach and the execution
- **Anticipate common errors** specific to the task type and verify against them
- **For mathematical problems**, verify with different formulas or approximation methods
- **For logical arguments**, check for fallacies and test with counterexamples
- **For complex tasks**, verify components separately before verifying the whole
- **Document verification steps explicitly** - don't just say "verified" but explain how
- **Consider both false positives and false negatives** in your verification
- **Use order-of-magnitude checks** for numerical problems to catch major errors
- **For critical tasks**, implement multiple independent verification methods

## Related Templates

- **Chain of Thought Template**: The foundation that verification loops build upon
- **Task Decomposition Template**: Useful for breaking complex verification into manageable parts
- **Adversarial Thinking Template**: For verification through challenging assumptions
- **Recursive Self-Improvement Template**: For iteratively enhancing verification processes
