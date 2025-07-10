# 吸引子设计模板

## 总结
用于创建语义吸引子的模板，这些吸引子将 AI 推理引导到特定的概念框架、方法或结果，而无需明确说明。

## 背景和应用
当您想通过在语义空间中创建“吸引子”（自然地将思维拉向特定方向的概念引力井）来巧妙地引导 AI 推理到特定类型的响应时，请使用此模板。与直接指令不同，吸引子通过建立 AI 自然延续或完成的模式来工作。

此模板非常适合：
- 鼓励特定的思维方式或框架，但未明确要求
- 创建感觉自然而非强迫的微妙指导
- 建立“重心”以进行推理以绕其运行
- 在保持灵活性和创造力的同时指导推理
- 影响而不决定具体结果

## 模板结构

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider:*

{{primary_attractor_concept_1}}:
- {{supporting_element_1a}}
- {{supporting_element_1b}}
- {{supporting_element_1c}}

{{primary_attractor_concept_2}}:
- {{supporting_element_2a}}
- {{supporting_element_2b}}
- {{supporting_element_2c}}

{{resonant_concept}}:
- {{resonant_element_a}}
- {{resonant_element_b}}

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
{{output_specifications}}
```

## 参数

- `{{task_description}}`：未明确提及吸引子概念的任务描述
- `{{neutral_context}}`： 建立背景信息而不偏向吸引子
- `{{primary_attractor_concept_X}}`：您希望用作语义吸引子的主要概念
- `{{supporting_element_X}}`：强化和定义吸引子概念的元素
- `{{resonant_concept}}`：与主要吸引物产生共鸣并放大的概念
- `{{output_specifications}}`：输出的格式和结构规范

## 例子

### 示例 1：系统思维吸引子

```
# Task: Analyze the challenges facing urban transportation in growing cities

## Context
Urban areas worldwide are experiencing population growth, putting pressure on existing transportation infrastructure. Many cities are seeking solutions to mobility challenges.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Interconnectedness:
- Relationship between transportation and land use
- Impact of transportation choices on environmental systems
- Connection between mobility and economic opportunity

Feedback Loops:
- How infrastructure investments shape development patterns
- Relationship between congestion and behavior adaptation
- Environmental impacts that affect future transportation choices

Emergence:
- Patterns that arise from individual transportation decisions
- Unexpected consequences of transportation policies
- Self-organizing aspects of urban mobility

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A comprehensive analysis of urban transportation challenges that identifies key issues, explores underlying dynamics, and suggests potential approaches. Include both short-term and long-term perspectives.
```

### 示例 2：创意创新吸引器

```
# Task: Suggest product improvement ideas for a smart home thermostat

## Context
Smart thermostats have become increasingly common in homes, allowing temperature programming, remote control, and some learning capabilities. The company is looking to develop their next generation product.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Boundary Breaking:
- Extending functionality beyond traditional temperature control
- Integration with unexpected systems or services
- Challenging assumptions about what a thermostat should be

Recombination:
- Merging features from different product categories
- Novel combinations of existing technologies
- Unexpected applications of familiar capabilities

User-Centered Surprise:
- Features that anticipate needs users didn't know they had
- Delightful interactions that exceed expectations
- Transformative experiences rather than incremental improvements

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A list of 5-7 innovative product improvement ideas, each with a brief description, potential user benefit, and implementation considerations. Focus on distinctive ideas rather than obvious incremental improvements.
```

## 变化

### 多吸引子场
用于创建具有不同强度的多个吸引子：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider (in no particular order):*

{{primary_attractor}} [strength: high]:
- {{supporting_elements}}

{{secondary_attractor}} [strength: medium]:
- {{supporting_elements}}

{{tertiary_attractor}} [strength: low]:
- {{supporting_elements}}

## Approach
Consider these concepts in your response, giving each appropriate consideration.

## Expected Output
{{output_specifications}}
```

### 吸引子-排斥器动力学
为了创造吸引和排斥的概念力：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*Consider the following as you develop your response:*

Relevant Approaches:
- {{attractor_concept_1}}
- {{attractor_concept_2}}
- {{attractor_concept_3}}

Approaches to Avoid:
- {{repeller_concept_1}}
- {{repeller_concept_2}}

## Approach
Develop your response drawing from the relevant approaches while avoiding the limitations of approaches to avoid.

## Expected Output
{{output_specifications}}
```

### Resonant Field Attractor
为了创建相互放大的相辅相成的概念：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following interconnected concepts may be relevant:*

{{concept_1}} ↔ {{concept_2}}:
- How {{concept_1}} influences {{concept_2}}
- How {{concept_2}} reinforces {{concept_1}}

{{concept_2}} ↔ {{concept_3}}:
- Ways {{concept_2}} shapes {{concept_3}}
- Ways {{concept_3}} enhances {{concept_2}}

{{concept_3}} ↔ {{concept_1}}:
- The relationship between {{concept_3}} and {{concept_1}}
- Mutual amplification effects

## Approach
Consider these resonant relationships in your analysis.

## Expected Output
{{output_specifications}}
```

## 最佳实践

- **要微妙而不是粗暴** - 当吸引子感觉像是自然的考虑而不是强迫的要求时，它们效果最好
- **创建连贯的吸引子场** - 使用自然互补的概念
- **平衡特异性和开放性** - 太模糊不会产生足够的吸引力，太具体会成为规定性
- **使用支持元素来清楚地定义吸引子** - 帮助准确确定吸引子概念包含的内容
- **将吸引子定位为“要考虑的概念”而不是要求** - 在保持灵活性的同时创造微妙的引力
- **使用熟悉的概念作为通往不熟悉概念的桥梁** - 有助于创造通往新奇思维的道路
- **对于复杂的任务，使用多个谐振吸引子** - 创建一个丰富的概念场
- **测试吸引子强度** - 如果太弱，则增强支撑元件;如果太占主导地位，则降低特异性
- **使吸引子与真正的目标保持一致** - 拉力应该导致真正有用的方法
- **将吸引子设计为易于发现** - 它们应该感觉像是见解而不是说明

## 相关模板

- **场边界建立模板**：用于创建概念边界以补充吸引子
- **Resonance Prompting Template**：用于在概念之间创建共鸣效果
- **Persona Attractor Template**：用于将角色用作语义吸引器
- **Emergence 工程模板**：用于通过吸引子场培养 emergent 属性
