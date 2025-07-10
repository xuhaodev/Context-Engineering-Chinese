# 提示：面向目标的 AI 交互模板

> “正确的提示不仅仅是一个请求，而是一个思考的架构。”

## 概述

欢迎来到 **PROMPTS**，这是一个精心设计的程序库，通过战略有效的模板和多模式代理系统提示帮助您实现目标。与传统的提示集合不同，这些模板是围绕您想要实现的目标组织的，并通过多模式提示使整个代理栩栩如生。

该库基于对人类与 AI 交互的广泛研究，旨在弥合前沿 AI 功能与实际日常使用之间的差距。每个模板都体现了上下文工程的原则，同时保持可访问性并立即有用。

## 库结构 （正在建设中）

```
PROMPTS/
├── agentic
│
├── everyday/                          # Templates for common everyday needs
│   ├── expert_guides.md               # Getting expert advice on any topic
│   ├── step_by_step.md                # Breaking down any process into clear steps
│   ├── content_creation.md            # Creating various types of content
│   ├── idea_generation.md             # Brainstorming creative ideas and solutions
│   ├── decision_helper.md             # Making better decisions with structure
│   └── feedback_coach.md              # Getting helpful feedback and suggestions
│
├── creating/                          # Templates for creating content
│   ├── writing_articles.md            # Creating blog posts and long-form content
│   ├── marketing_copy.md              # Creating ads, emails, and promotional content
│   ├── creative_writing.md            # Fiction, stories, and creative pieces
│   ├── professional_docs.md           # Reports, proposals, and business documents
│   └── visual_content.md              # Guidance for visuals and presentations
│
├── building/                          # Templates for building and making
│   ├── coding_help.md                 # Programming assistance and code generation
│   ├── project_planning.md            # Planning and structuring projects
│   ├── system_design.md               # Designing systems and architectures
│   └── product_development.md         # Creating and improving products
│
├── thinking/                          # Templates for better thinking
│   ├── analysis_frameworks.md         # Structured approaches to analysis
│   ├── research_assistant.md          # Help with research and investigation
│   ├── mental_models.md               # Applying powerful thinking tools
│   ├── critical_thinking.md           # Evaluating ideas and avoiding biases
│   └── data_insights.md               # Making sense of information and data
│
├── improving/                         # Templates for making things better
│   ├── content_editing.md             # Improving written content
│   ├── code_refinement.md             # Refactoring and optimizing code
│   ├── process_optimization.md        # Making workflows more efficient
│   ├── feedback_systems.md            # Getting and giving better feedback
│   └── iteration_cycles.md            # Structured approach to improvement
│
├── solving/                           # Templates for solving problems
│   ├── troubleshooting.md             # Diagnosing and fixing issues
│   ├── creative_solutions.md          # Finding innovative approaches
│   ├── decision_frameworks.md         # Making complex decisions
│   ├── tradeoff_analysis.md           # Balancing competing priorities
│   └── risk_assessment.md             # Identifying and mitigating risks
│
├── teaching/                          # Templates for education and learning
│   ├── explaining_concepts.md         # Making complex ideas understandable
│   ├── course_creation.md             # Designing educational experiences
│   ├── learning_materials.md          # Creating helpful learning resources
│   └── simplifying_complexity.md      # Breaking down difficult topics
│
├── collaborating/                     # Templates for working with others
│   ├── meeting_facilitation.md        # Running more effective meetings
│   ├── team_coordination.md           # Improving team communication
│   ├── conflict_resolution.md         # Addressing disagreements constructively
│   └── feedback_sessions.md           # Structured feedback conversations
│
└── specialized/                       # Templates for specific advanced uses
    ├── ai_research.md                 # Templates for AI researchers
    ├── prompt_engineering.md          # Advanced prompt design techniques
    ├── safety_alignment.md            # Working with AI safety considerations
    ├── template_creation.md           # Creating your own custom templates
    └── template_combinations.md       # Combining templates effectively
```
## 如何使用此库

### 找到您的目标

首先确定您要完成的目标：

- **创造什么？** → 探索 `creating/` 目录
- **建造还是制作？** → 查看 `building/` 目录
- **思考还是分析？** → 访问 `thinking/` 目录
- **改进什么？** → 浏览 `improving/` 目录
- **解决问题？** → 浏览 `solving/` 目录
- **教学还是解释？** → 查看 `teaching/` 目录
- **与他人合作？** → 探索 `collaborating/` 目录
- **只是需要一些快速的东西？** → 从 `everyday/` 模板开始

### 选择模板

找到目标类别后，选择符合您需求的特定模板。每个文件都包含多个相关模板，并提供有关何时以及如何使用它们的明确指导。

### 自定义和使用

模板多种多样，包括：
- 关于何时使用它的明确说明
- 带有占位符的模板本身
- 自定义的分步指南
- 实际示例
- 获得最佳结果的提示
- 不同场景的变化

只需复制模板，将占位符替换为您的特定信息，然后将其与您喜欢的 AI 系统一起使用即可。

## 特色模板

以下是我们一些最通用的模板，可帮助您入门：

### 获得专家指导

```
# Expert Consultation: {{field_of_expertise}}

## Expert Profile
You are an experienced {{specific_expert_role}} with extensive knowledge of {{field_of_expertise}}. Your background includes {{relevant_experience}} and you're especially knowledgeable about {{specific_specialization}}.

## My Question/Request
{{your_specific_question_or_request}}

## Additional Context
{{any_relevant_background_information}}

## What I'm Looking For
- Depth of detail: {{how_detailed_you_want_the_response}}
- Focus areas: {{specific_aspects_to_focus_on}}
- Perspective: {{any_particular_viewpoint_you_want}}

Please provide your expert guidance, including relevant examples, best practices, and any frameworks or approaches that would be helpful.
```

### 分步过程指南

```
# Step-by-Step Guide: {{process_name}}

## Goal
Create a clear step-by-step guide for {{specific_goal}}.

## Target Audience
This guide is for {{audience_description}} who need to {{audience_need}}.

## Guide Requirements
- Expertise level: {{beginner_intermediate_advanced}}
- Comprehensiveness: {{quick_overview_or_detailed_walkthrough}}
- Style: {{instructional_tone}}
- Include: {{special_elements_to_include}}

## Process Context
{{background_information_about_the_process}}

Please create a clear, well-structured step-by-step guide that helps the reader accomplish this goal successfully. Include any necessary warnings, tips, or common pitfalls.
```

## 设计原则

这些模板基于几个核心原则构建：

1. **以目标为导向**：按您想要完成的任务进行组织
2. **以人为本**：从您的角度设计，而不是 AI 的角度
3. **实用**：即用型，定制最少
4. **多功能**：跨域和 AI 系统适应性强
5. **渐进式**：简单核心，可选复杂性
6. **透明**：清楚每个部分的作用和原因

## 贡献

此库专为扩展而设计。要做出贡献：

1. **Add to existing files（添加到现有文件**）：将新模板添加到相关的现有文件
2. **创建新文件**：如果您有新子类别的模板，请在相应的目录中创建新文件
3. **建议新目录**：如果您有全新目标类别的模板，请建议新目录

确保新模板遵循既定的格式和设计原则。

## 起源和未来方向

PROMPTS 库源于上下文工程研究和实际 AI 应用的交叉点。它代表了我们正在进行的工作，将理论框架与日常实用性联系起来。

该资源将与前沿的 AI 功能一起发展，并在出现新的交互模式和模板结构时将其纳入其中。我们致力于维护一个既有理论基础又立即实用的库。

## 超越模板

这些模板只是一个开始。真正的力量来自：

1. **适应：**根据您的特定需求修改模板
2. **组合：**合并复杂任务的模板
3. **迭代**：根据结果优化模板
4. **扩展：**使用演示的原则创建自己的模板

## 反馈与发展

这个库是一个旨在发展和适应的活资源。您的反馈和贡献有助于塑造其发展。

---

> 此库中的模板与 AI 无关，旨在与任何功能强大的 AI 系统配合使用。它们体现了上下文工程的原则，同时每个人都可以访问。
