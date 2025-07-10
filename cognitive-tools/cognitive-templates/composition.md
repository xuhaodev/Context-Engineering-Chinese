# 模板组合

> “整体大于其部分之和。”

## 概述

模板组合涉及组合多个认知模板来解决需要多个推理阶段的复杂问题。通过战略性地对模板进行排序，我们可以创建复杂的认知工作流，指导语言模型完成复杂的任务，同时保持结构和清晰度。

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  TEMPLATE COMPOSITION                                                │
│                                                                      │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐             │
│  │             │     │             │     │             │             │
│  │ Template A  │────►│ Template B  │────►│ Template C  │─────► ...   │
│  │             │     │             │     │             │             │
│  └─────────────┘     └─────────────┘     └─────────────┘             │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 基本合成模式

### 1. 线性序列

最简单的合成模式以固定的顺序链接模板。

```markdown
# Linear Sequence Template

Task: Solve the following complex problem through a structured multi-stage approach.

Problem: {{problem}}

## Stage 1: Understanding the Problem
{{understanding_template}}

## Stage 2: Planning the Solution
{{reasoning_template}}

## Stage 3: Executing the Plan
{{step_by_step_template}}

## Stage 4: Verifying the Solution
{{verification_template}}

## Stage 5: Final Answer
Based on the above analysis and verification, provide your final answer to the original problem.
```

**令牌计数**：因组件模板而异

**使用示例**：
- 用于解决数学问题
- 处理复杂的推理任务时
- 适用于任何多阶段问题解决过程

### 2. 条件分支

此模式引入了确定要应用的下一个模板的决策点。

```markdown
# Conditional Branching Template

Task: Analyze and solve the following problem using the appropriate approach based on problem characteristics.

Problem: {{problem}}

## Stage 1: Problem Analysis
{{understanding_template}}

## Stage 2: Approach Selection
Based on your analysis, determine which of the following approaches is most appropriate:

A) If this is primarily a mathematical calculation problem:
   {{mathematical_reasoning_template}}

B) If this is primarily a logical reasoning problem:
   {{logical_reasoning_template}}

C) If this is primarily a data analysis problem:
   {{data_analysis_template}}

## Stage 3: Solution Verification
{{verification_template}}

## Stage 4: Final Answer
Provide your final answer to the original problem.
```

**令牌计数**：因组件模板而异

**使用示例**：
- 对于可能需要不同方法的问题
- 当问题类型最初不明确时
- 对于处理各种查询类型的系统

### 3. 迭代优化

此模式会重复应用模板，直到获得满意的结果。

```markdown
# Iterative Refinement Template

Task: Iteratively develop and refine a solution to the following problem.

Problem: {{problem}}

## Iteration 1: Initial Solution
{{reasoning_template}}

## Evaluation of Iteration 1
{{evaluation_template}}

## Iteration 2: Refined Solution
Based on the evaluation of your first attempt, provide an improved solution.
{{reasoning_template}}

## Evaluation of Iteration 2
{{evaluation_template}}

## Iteration 3: Final Solution
Based on the evaluation of your second attempt, provide your final solution.
{{reasoning_template}}

## Final Verification
{{verification_template}}

## Final Answer
Provide your final answer to the original problem.
```

**Token Count**：因组件模板和迭代次数而异

**使用示例**：
- 适用于受益于 Refines 的创意任务
- 处理难题时
- 用于生成高质量的内容

## 高级合成模式

### 4. 分而治之

此模式将复杂问题分解为多个子问题，独立解决每个子问题，然后组合结果。

```markdown
# Divide and Conquer Template

Task: Solve the following complex problem by breaking it into manageable sub-problems.

Problem: {{problem}}

## Stage 1: Problem Decomposition
{{decomposition_template}}

## Stage 2: Solving Sub-Problems
For each sub-problem identified above:

### Sub-Problem 1:
{{reasoning_template}}

### Sub-Problem 2:
{{reasoning_template}}

### Sub-Problem 3:
{{reasoning_template}}
(Add additional sub-problems as needed)

## Stage 3: Solution Integration
{{integration_template}}

## Stage 4: Verification
{{verification_template}}

## Stage 5: Final Answer
Provide your final answer to the original problem.
```

**Token Count**：根据组件模板和子问题的数量而变化

**使用示例**：
- 对于具有不同组件的复杂问题
- 当处理具有多个相互作用部件的系统时
- 适用于需要多种分析类型的项目

### 5. 辩证推理

这种模式探索了相反的观点，以得出一个微妙的结论。

```markdown
# Dialectical Reasoning Template

Task: Analyze the following issue through a dialectical approach to reach a nuanced conclusion.

Issue: {{issue}}

## Stage 1: Issue Analysis
{{understanding_template}}

## Stage 2: Thesis (Position A)
{{argument_template}}

## Stage 3: Antithesis (Position B)
{{argument_template}}

## Stage 4: Synthesis
{{synthesis_template}}

## Stage 5: Verification
{{verification_template}}

## Stage 6: Conclusion
Provide your final conclusion on the issue.
```

**令牌计数**：因组件模板而异

**使用示例**：
- 对于有争议或复杂的主题
- 当存在多个有效透视时
- 用于哲学或伦理问题

### 6. 多智能体模拟

此模式通过不同的 “代理” 模拟不同的专业知识或观点。

```markdown
# Multi-Agent Simulation Template

Task: Analyze the following problem from multiple expert perspectives to reach a comprehensive solution.

Problem: {{problem}}

## Stage 1: Problem Analysis
{{understanding_template}}

## Stage 2: Expert Perspectives

### Perspective 1: {{expert_1}} (e.g., "Mathematician")
{{reasoning_template}}

### Perspective 2: {{expert_2}} (e.g., "Economist")
{{reasoning_template}}

### Perspective 3: {{expert_3}} (e.g., "Historian")
{{reasoning_template}}
(Add additional perspectives as needed)

## Stage 3: Collaborative Integration
{{integration_template}}

## Stage 4: Verification
{{verification_template}}

## Stage 5: Final Solution
Provide your final solution to the problem, incorporating insights from all perspectives.
```

**令牌计数**：因组件模板和透视图数量而异

**使用示例**：
- 针对跨学科问题
- 当多样化的专业知识很有价值时
- 用于复杂情况的全面分析

## 实现模式

这是一个实现基本线性序列组合的 Python 函数：

```python
def linear_sequence(problem, templates):
    """
    Create a prompt that composes multiple templates in a linear sequence.
    
    Args:
        problem (str): The problem to solve
        templates (dict): A dictionary of template functions keyed by stage names
        
    Returns:
        str: A formatted prompt for a linear sequence of templates
    """
    prompt = f"""
Task: Solve the following complex problem through a structured multi-stage approach.

Problem: {problem}
"""
    
    for i, (stage_name, template_func) in enumerate(templates.items()):
        prompt += f"\n## Stage {i+1}: {stage_name}\n"
        
        # For each template, we only include the instructions, not the problem statement again
        template_content = template_func(problem)
        # Extract just the instructions, assuming the problem statement is at the beginning
        instructions = "\n".join(template_content.split("\n")[3:])
        
        prompt += instructions
    
    prompt += """
## Final Answer
Based on the above analysis, provide your final answer to the original problem.
"""
    
    return prompt

# Example usage
from cognitive_templates import understanding, step_by_step_reasoning, verify_solution

templates = {
    "Understanding the Problem": understanding,
    "Solving Step by Step": step_by_step_reasoning,
    "Verifying the Solution": verify_solution
}

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
composed_prompt = linear_sequence(problem, templates)
```

## 模板合成策略

组合模板时，请考虑以下策略以获得最佳结果：

### 1. 状态管理

确保信息在模板之间正确流动：

```python
def managed_sequence(problem, llm):
    """
    Execute a sequence of templates with explicit state management.
    
    Args:
        problem (str): The problem to solve
        llm: LLM interface for generating responses
        
    Returns:
        dict: Complete solution with intermediate results
    """
    # Initialize state
    state = {"problem": problem, "stages": {}}
    
    # Stage 1: Understanding
    understanding_prompt = understanding(problem)
    understanding_result = llm.generate(understanding_prompt)
    state["stages"]["understanding"] = understanding_result
    
    # Stage 2: Planning with context from understanding
    planning_prompt = f"""
Task: Plan a solution approach based on this problem analysis.

Problem: {problem}

Problem Analysis:
{understanding_result}

Please outline a step-by-step approach to solve this problem.
"""
    planning_result = llm.generate(planning_prompt)
    state["stages"]["planning"] = planning_result
    
    # Stage 3: Execution with context from planning
    execution_prompt = f"""
Task: Execute the solution plan for this problem.

Problem: {problem}

Problem Analysis:
{understanding_result}

Solution Plan:
{planning_result}

Please implement this plan step by step to solve the problem.
"""
    execution_result = llm.generate(execution_prompt)
    state["stages"]["execution"] = execution_result
    
    # Stage 4: Verification with context from execution
    verification_prompt = verify_solution(problem, execution_result)
    verification_result = llm.generate(verification_prompt)
    state["stages"]["verification"] = verification_result
    
    # Return complete solution with all intermediate stages
    return state
```

### 2. 自适应选择

根据问题特征动态选择模板：

```python
def adaptive_composition(problem, llm):
    """
    Adaptively select and compose templates based on problem characteristics.
    
    Args:
        problem (str): The problem to solve
        llm: LLM interface for generating responses
        
    Returns:
        dict: Complete solution with template selection rationale
    """
    # Stage 1: Problem classification
    classification_prompt = f"""
Task: Classify the following problem to determine the most appropriate solution approach.

Problem: {problem}

Please classify this problem into ONE of the following categories:
1. Mathematical Calculation
2. Logical Reasoning
3. Data Analysis
4. Creative Writing
5. Decision Making

Provide your classification and a brief explanation of your reasoning.
"""
    classification_result = llm.generate(classification_prompt)
    
    # Parse the classification (in a real implementation, use more robust parsing)
    problem_type = "Unknown"
    for category in ["Mathematical", "Logical", "Data", "Creative", "Decision"]:
        if category in classification_result:
            problem_type = category
            break
    
    # Select templates based on problem type
    if "Mathematical" in problem_type:
        templates = {
            "Understanding": understanding,
            "Solution": step_by_step_reasoning,
            "Verification": verify_solution
        }
    elif "Logical" in problem_type:
        templates = {
            "Understanding": understanding,
            "Argument Analysis": lambda p: logical_argument_template(p),
            "Verification": verify_solution
        }
    # Add more conditions for other problem types
    
    # Execute the selected template sequence
    result = {
        "problem": problem,
        "classification": classification_result,
        "selected_approach": problem_type,
        "stages": {}
    }
    
    for stage_name, template_func in templates.items():
        prompt = template_func(problem)
        response = llm.generate(prompt)
        result["stages"][stage_name] = response
    
    return result
```

### 3. 反馈驱动的优化

使用评估结果指导模板选择和优化：

```python
def feedback_driven_composition(problem, llm, max_iterations=3):
    """
    Use feedback to drive template selection and refinement.
    
    Args:
        problem (str): The problem to solve
        llm: LLM interface for generating responses
        max_iterations (int): Maximum number of refinement iterations
        
    Returns:
        dict: Complete solution with refinement history
    """
    # Initialize state
    state = {
        "problem": problem,
        "iterations": [],
        "final_solution": None,
        "quality_score": 0
    }
    
    # Initial solution
    solution = llm.generate(step_by_step_reasoning(problem))
    
    for i in range(max_iterations):
        # Evaluate current solution
        evaluation_prompt = f"""
Task: Evaluate the quality and correctness of this solution.

Problem: {problem}

Proposed Solution:
{solution}

Please evaluate this solution on a scale of 1-10 for:
1. Correctness (is the answer right?)
2. Clarity (is the reasoning clear?)
3. Completeness (are all aspects addressed?)

For each criterion, provide a score and brief explanation.
Then suggest specific improvements that could be made.
"""
        evaluation = llm.generate(evaluation_prompt)
        
        # Extract quality score (in a real implementation, use more robust parsing)
        quality_score = 0
        for line in evaluation.split("\n"):
            if "Correctness" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
            if "Clarity" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
            if "Completeness" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
        
        quality_score = quality_score / 3  # Average score
        
        # Record this iteration
        state["iterations"].append({
            "solution": solution,
            "evaluation": evaluation,
            "quality_score": quality_score
        })
        
        # Check if quality is satisfactory
        if quality_score >= 8:
            break
        
        # Select template for improvement based on evaluation
        if "Correctness" in evaluation and "clarity" not in evaluation.lower():
            # If correctness is the main issue, focus on verification
            improvement_template = verify_solution
        elif "clarity" in evaluation.lower():
            # If clarity is the main issue, focus on explanation
            improvement_template = lambda p: step_by_step_reasoning(p, steps=["Understand", "Plan", "Execute with clear explanations", "Verify", "Conclude"])
        else:
            # Default to general improvement
            improvement_template = step_by_step_reasoning
        
        # Generate improved solution
        improvement_prompt = f"""
Task: Improve the following solution based on this evaluation feedback.

Problem: {problem}

Current Solution:
{solution}

Evaluation:
{evaluation}

Please provide an improved solution that addresses the issues identified in the evaluation.
"""
        solution = llm.generate(improvement_prompt)
    
    # Select best solution based on quality score
    best_iteration = max(state["iterations"], key=lambda x: x["quality_score"])
    state["final_solution"] = best_iteration["solution"]
    state["quality_score"] = best_iteration["quality_score"]
    
    return state
```

## 衡量组合效果

使用模板合成时，请通过以下方式衡量其有效性：

1. **端到端准确性**：完整合成是否产生正确的结果？
2. **阶段贡献**：每个模板对最终质量的贡献有多大？
3. **信息流**：模板之间是否保留了重要的上下文？
4. **效率**：与更简单的方法相比，组合的代币开销是多少？
5. **适应性**：组合处理不同问题变化的能力如何？

## 有效构图的技巧

1. **从简单开始**：从线性序列开始，然后再尝试更复杂的 pattern
2. **最大限度地减少冗余**：避免跨模板重复指令
3. **保留上下文**：确保模板之间的关键信息流动
4. **平衡结构与灵活性**：过于僵化的构图限制了模型的优势
5. **使用变体进行测试**：验证您的合成是否适用于问题变体
6. **包括自我纠正**：内置验证和优化机会

## 后续步骤

- 看看这些组合模式是如何在 [../认知程序/program-library.py](../cognitive-programs/program-library.py)
- 在 .. 中探索完整的认知架构 [/cognitive-architectures/solver-architecture.md 中](../cognitive-architectures/solver-architecture.md)
- 学习如何将这些作品与检索和记忆整合在一起[。/integration/with-rag.md](../integration/with-rag.md) 和 [../integration/with-memory.md 中](../integration/with-memory.md)

---

## 深入探讨：使用模板进行元编程

高级从业者可以创建动态生成模板的系统：

```python
def generate_specialized_template(domain, complexity, llm):
    """
    Generate a specialized template for a specific domain and complexity level.
    
    Args:
        domain (str): The domain area (e.g., "mathematics", "legal")
        complexity (str): The complexity level (e.g., "basic", "advanced")
        llm: LLM interface for generating the template
        
    Returns:
        function: A generated template function
    """
    prompt = f"""
Task: Create a specialized cognitive template for solving {complexity} problems in the {domain} domain.

The template should:
1. Include appropriate domain-specific terminology and concepts
2. Break down the reasoning process into clear steps
3. Include domain-specific verification checks
4. Be calibrated for {complexity} complexity level

Format the template as a markdown document with:
1. A clear task description
2. Structured steps for solving problems in this domain
3. Domain-specific guidance for each step
4. Verification criteria specific to this domain

Please generate the complete template text.
"""
    
    template_text = llm.generate(prompt)
    
    # Create a function that applies this template
    def specialized_template(problem):
        return f"""
Task: Solve the following {complexity} {domain} problem using a specialized approach.

Problem: {problem}

{template_text}
"""
    
    return specialized_template

# Example usage
legal_reasoning_template = generate_specialized_template("legal", "advanced", llm)
math_template = generate_specialized_template("mathematics", "intermediate", llm)

# Apply the generated template
legal_problem = "Analyze the liability implications in this contract clause..."
legal_prompt = legal_reasoning_template(legal_problem)
```

这种元级方法可以创建针对特定领域和复杂程度定制的高度专业化的模板。
