# 最小上下文模板

## 总结
一个简化的模板，用于为 AI 系统创建最小但有效的上下文，侧重于清晰度和基本信息。
## 背景和应用
当您需要为 AI 系统提供足够的上下文以有效执行而无需不必要的信息时，请使用此模板。它以结构化格式建立明确的界限、期望和基本信息。

此模板非常适合：
- 首次与 AI 系统交互
- 定义明确的任务和明确的可交付成果
- 最小化提示长度很重要的情况
- 为更复杂的提示建立基线

## 模板结构

```
# Task: {{specific_task}}

## Context
- {{key_background_point_1}}
- {{key_background_point_2}}
- {{additional_context_if_needed}}

## Constraints
- {{constraint_1}}
- {{constraint_2}}

## Expected Output
- Format: {{output_format}}
- Length: {{approximate_length}}
- Style: {{style_guidelines}}

## Examples
{{optional_example}}
```

## 参数

- `{{specific_task}}`：明确描述您希望 AI 执行的作（例如，“编写产品描述”或“分析以下数据”）
- `{{key_background_point_X}}`：正确完成任务所需的基本信息（限 2-4 分）
- `{{constraint_X}}`： 必须遵守的限制或要求（例如，“不包含定价信息”）
- `{{output_format}}`：输出的结构、格式或文件类型（例如，“项目符号列表”或“JSON 对象”）
- `{{approximate_length}}`：关于输出应有多广泛的指南（例如，“300-400 字”或“5 个要点”）
- `{{style_guidelines}}`：语气、声音和风格期望（例如，“专业和正式”或“对话和参与”）
- `{{optional_example}}`：预期输出样本（强烈建议首次任务使用）

## 例子

### 示例 1：数据分析报告

```
# Task: Analyze the provided sales data and create a summary report

## Context
- Data represents quarterly sales figures for 2022
- Company has 3 product lines: Basic, Premium, and Enterprise
- Previous year showed seasonal trends with Q4 strongest

## Constraints
- Focus on significant changes year-over-year
- Do not speculate beyond what the data shows
- Include at least one actionable recommendation

## Expected Output
- Format: Executive summary followed by bullet points
- Length: Approximately 300-400 words
- Style: Professional, data-focused, actionable

## Examples
Executive Summary:
Q2 2022 shows a 15% increase in overall sales compared to Q2 2021, with the Premium product line showing the strongest growth at 23%. This continues the upward trend observed in Q1...
```

### 示例 2：创意内容创作

```
# Task: Write a product description for our new wireless headphones

## Context
- Target audience: tech-savvy professionals ages 25-40
- Key features: noise cancellation, 30-hour battery life, voice assistant integration
- Main selling points: comfort for all-day wear, premium sound quality

## Constraints
- Keep technical specifications to a minimum
- Don't mention competitors by name
- Focus on benefits, not just features

## Expected Output
- Format: Two paragraphs of flowing text
- Length: 150-200 words
- Style: Modern, enthusiastic but not overly promotional

## Examples
Experience music as it was meant to be heard with our new XDR Wireless Headphones. Designed for professionals who demand the best, these headphones deliver crystal-clear sound while intelligent noise cancellation technology creates your own personal sanctuary of sound—whether you're in a busy office or on a crowded commute...
```

## 变化

### 技术规格模板
对于需要精确说明的技术任务：

```
# Task: {{specific_technical_task}}

## Context
- {{technical_background_point_1}}
- {{technical_background_point_2}}
- {{system_dependencies}}

## Requirements
- {{functional_requirement_1}}
- {{functional_requirement_2}}
- {{performance_requirement}}

## Technical Constraints
- {{technical_limitation_1}}
- {{compatibility_requirement}}

## Expected Output
- Format: {{technical_format}}
- Testing Criteria: {{validation_method}}
- Documentation: {{documentation_requirements}}

## Examples
{{technical_example}}
```

### 创意简报模板
对于写作或设计等创意任务：

```
# Task: {{creative_task}}

## Context
- Audience: {{target_audience}}
- Purpose: {{communication_goal}}
- Brand Voice: {{brand_personality}}

## Creative Direction
- {{inspiration_point_1}}
- {{inspiration_point_2}}
- {{emotional_response_desired}}

## Constraints
- {{brand_guideline_1}}
- {{content_restriction}}
- {{technical_limitation}}

## Expected Output
- Format: {{creative_format}}
- Length/Size: {{dimension_guidelines}}
- Style: {{stylistic_direction}}

## Examples
{{creative_example}}
```

## 最佳实践

- **具体说明任务** - 避免使用模糊的说明，例如“写一些关于耳机的内容”;而是使用“为面向年轻专业人士的无线耳机编写产品描述”
- **仅提供必要的上下文** - 过多的信息会分散重点并导致不太相关的输出
- **使用项目符号以清晰** - 将信息分解为项目符号比密集的段落更容易处理
- **尽可能至少包含一个示例** - 示例极大地提高了对期望的理解
- **显式列出约束** ，而不是将它们嵌入到段落中 - 使它们更难错过
- **对于复杂的任务，将任务分解为明确的步骤** 或组件 - 有助于保持专注和结构
- **将上下文与输出预期匹配** - 确保提供的上下文支持预期的输出格式和样式

## 相关模板

- **Few-Shot 学习模板**：当您需要通过多个示例教授 AI 时
- **Chain of Thought Template**：当任务需要逐步推理时
- **基于角色的上下文模板**：当采用特定角色或视角会改善结果时
