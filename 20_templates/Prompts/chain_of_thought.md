# 思维链模板

## 总结
一个模板，用于指导 AI 系统完成明确的分步推理过程，从而提高复杂任务的准确性和透明度。

## 背景和应用
当任务需要仔细推理或得出结论的过程与结论本身一样重要时，请使用此模板。通过将复杂的思维分解为明确的步骤，思维链提示可以提高准确性，实现验证，并使推理过程透明。

此模板非常适合：
- 复杂的问题解决任务
- 需要逻辑推理的情况
- 多步骤计算或分析
- 解释 “为什么” 很重要的任务
- 减少具有挑战性的问题的错误

## 模板结构

```
# Task: {{task_description}}

## Approach
Think through this step-by-step:

1. {{first_reasoning_step}}
2. {{second_reasoning_step}}
3. {{additional_steps_as_needed}}
4. Formulate your conclusion based on this reasoning.

## Expected Output
Provide your complete reasoning process and then your final answer.
```

## 参数

- `{{task_description}}`：对要解决的问题或要回答的问题的明确描述
- `{{first_reasoning_step}}`： 推理过程的初始步骤（例如，“确定关键变量”）
- `{{second_reasoning_step}}`：下一个逻辑步骤（例如，“确定变量之间的关系”）
- `{{additional_steps_as_needed}}`：指导完整推理的进一步步骤

## 例子

### 示例 1：数学问题解决

```
# Task: Solve the following word problem

A store sells notebooks for $4 each and pens for $2 each. Emma bought some notebooks and twice as many pens. If she spent $24 in total, how many notebooks did she buy?

## Approach
Think through this step-by-step:

1. Define variables for what we're looking for
2. Set up equations based on the given information
3. Solve the equations to find the unknown values
4. Verify your answer makes sense with the original conditions

## Expected Output
Provide your complete reasoning process and then your final answer.
```

### 示例 2：道德决策分析

```
# Task: Analyze the ethical implications of the following scenario

A pharmaceutical company has developed a drug that shows promise for treating a rare disease. The clinical trials indicate 70% efficacy but also reveal potentially serious side effects in 15% of patients. The company needs to decide whether to bring this drug to market.

## Approach
Think through this step-by-step:

1. Identify the key stakeholders in this scenario
2. Analyze the potential benefits of making the drug available
3. Consider the potential harms and risks involved
4. Evaluate alternative options that might be available
5. Balance competing ethical principles (beneficence, non-maleficence, autonomy, justice)
6. Formulate a nuanced recommendation with potential safeguards or conditions

## Expected Output
Provide your complete reasoning process and then your final recommendation.
```

## 变化

### 自我提示的思维链
鼓励 AI 开发自己的推理步骤：

```
# Task: {{task_description}}

## Approach
- First, break this problem down into logical steps
- Work through each step systematically
- Show your complete reasoning process
- Only then provide your final answer

## Expected Output
Step-by-step reasoning followed by conclusion.
```

### 引导式问题分解
对于需要更结构化指导的高度复杂的问题：

```
# Task: {{task_description}}

## Problem Decomposition
1. Sub-problem 1: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

2. Sub-problem 2: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

3. Integration: Combine your analyses from the sub-problems

## Expected Output
Analysis of each sub-problem, integration of insights, and final conclusion.
```

### 情景分析思路链
对于需要考虑多种情况的决策：

```
# Task: {{decision_task}}

## Approach
Think through this step-by-step:

1. Scenario A: If {{condition_A}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

2. Scenario B: If {{condition_B}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

3. Compare scenarios and determine the most robust approach

## Expected Output
Analysis of each scenario and reasoned recommendation.
```

## 最佳实践

- **将推理步骤与问题类型相匹配** - 不同的问题需要不同的推理方法
- **明确推理过程** - 清楚地阐明每一步应该进行什么思考
- **包括验证步骤** - 添加用于检查工作或验证结论的步骤
- **对于数学问题**，包括检查单位和数量级的步骤
- **对于道德或主观分析**，包括考虑多个观点的步骤
- **不要跳过步骤** - 将推理分解为更小的步骤可以提高准确性
- **大多数问题使用 3-7 个步骤** - 太少缺乏指导，太多会让人不知所措
- **鼓励元认知** - 包括促使对推理过程本身进行反思的步骤
- **对于复杂问题**，请考虑在集成之前分解为子问题

## 相关模板

- **验证循环模板**：通过明确的验证步骤扩展思路链
- **Few-Shot 学习模板**：可以组合以展示思维链推理的示例
- **元认知反思模板**：对推理过程本身进行更深入的思考
