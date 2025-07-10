# 用于情境工程的认知工具

> “给我一个足够长的杠杆和一个放置它的支点，我就会移动世界。”

## 什么是认知工具？
> “为 GPT-4.1 提供我们的”认知工具”
将其在 AIME2024 上的 pass@1 性能从 26.7% 提高到 43.3%，使其非常接近 o1-preview 的性能。— [IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)

<div align="center">
    
![图像](https://github.com/user-attachments/assets/a6402827-8bc0-40b5-93d8-46a07154fa4e)

“该工具通过识别手头的主要概念、提取问题中的相关信息以及突出显示可能有助于解决问题的有意义的属性、定理和技术来分解问题。”— [使用认知工具在语言模型中引发推理 — IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)


</div>

认知工具是结构化的提示模式，通过特定的推理作指导语言模型。就像人类用来解决问题的心理工具（类比、心智模型、启发式）一样，这些工具为模型提供了用于复杂推理任务的脚手架。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CONTEXT ENGINEERING PROGRESSION                             │
│                                                              │
│  Atoms       → Molecules   → Cells       → Organs      → Cognitive Tools  │
│  (Prompts)     (Few-shot)    (Memory)      (Multi-agent)  (Reasoning Patterns) │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 结构
```
cognitive-tools/
├── README.md                       # Overview and quick-start guide
├── cognitive-templates/            # Templates for cognitive processes
│   ├── understanding.md            # Comprehension templates
│   ├── reasoning.md                # Reasoning templates
│   ├── verification.md             # Verification templates
│   ├── composition.md              # Composition templates
│   ├── emergence.md                # Emergence templates
│   ├── quantum_interpretation.md   # Quantum semantics templates
│   ├── unified_field_reasoning.md  # Unified field templates
│   ├── meta_recursive_reasoning.md # Self-improvement templates
│   ├── interpretability_scaffolding.md # Transparency templates
│   ├── collaborative_co_evolution.md # Human-AI templates
│   └── cross_modal_integration.md  # Multi-modal templates
├── cognitive-programs/             # Executable cognitive processes
│   ├── basic-programs.md           # Fundamental programs
│   ├── advanced-programs.md        # Complex programs
│   ├── program-library.py          # Program collection
│   ├── program-examples.ipynb      # Program demonstrations
│   ├── emergence-programs.md       # Emergence programs
│   ├── quantum_semantic_programs.md # Quantum semantics programs
│   ├── unified_field_programs.md   # Unified field programs
│   ├── meta_recursive_programs.md  # Self-improvement programs
│   ├── interpretability_programs.md # Transparency programs
│   ├── collaborative_evolution_programs.md # Human-AI programs
│   └── cross_modal_programs.md     # Multi-modal programs
├── cognitive-schemas/              # Knowledge representation structures
│   ├── user-schemas.md             # User modeling schemas
│   ├── domain-schemas.md           # Domain knowledge schemas
│   ├── task-schemas.md             # Task representation schemas
│   ├── schema-library.yaml         # Schema collection
│   ├── field-schemas.md            # Field theory schemas
│   ├── quantum_schemas.md          # Quantum semantics schemas
│   ├── unified_schemas.md          # Unified field schemas
│   ├── meta_recursive_schemas.md   # Self-improvement schemas
│   ├── interpretability_schemas.md # Transparency schemas
│   ├── collaborative_schemas.md    # Human-AI schemas
│   └── cross_modal_schemas.md      # Multi-modal schemas
├── cognitive-architectures/        # System-level frameworks
│   ├── solver-architecture.md      # Problem-solving architecture
│   ├── tutor-architecture.md       # Educational architecture
│   ├── research-architecture.md    # Research assistant architecture
│   ├── architecture-examples.py    # Architecture demonstrations
│   ├── field-architecture.md       # Field theory architecture
│   ├── quantum_architecture.md     # Quantum semantics architecture
│   ├── unified_architecture.md     # Unified field architecture
│   ├── meta_recursive_architecture.md # Self-improvement architecture
│   ├── interpretability_architecture.md # Transparency architecture
│   ├── collaborative_architecture.md # Human-AI architecture
│   └── cross_modal_architecture.md # Multi-modal architecture
├── integration/                    # Integration with other systems
│   ├── with-rag.md                 # Retrieval integration
│   ├── with-memory.md              # Memory system integration
│   ├── with-agents.md              # Agent system integration
│   ├── evaluation-metrics.md       # Evaluation methods
│   ├── with-fields.md              # Field theory integration
│   ├── with-quantum.md             # Quantum semantics integration
│   ├── with-unified.md             # Unified field integration
│   ├── with-meta-recursion.md      # Self-improvement integration
│   ├── with-interpretability.md    # Transparency integration
│   ├── with-collaboration.md       # Human-AI integration
│   └── with-cross-modal.md         # Multi-modal integration
└── meta-cognition/                 # Meta-cognitive capabilities
    ├── self-reflection.md          # Self-analysis systems
    ├── recursive-improvement.md    # Self-enhancement methods
    ├── meta-awareness.md           # System self-awareness
    ├── attribution-engines.md      # Causal attribution systems
    ├── symbolic-echo-processing.md # Symbolic pattern processing
    ├── meta-interpretability.md    # Meta-level transparency
    ├── meta-collaboration.md       # Meta-level human-AI partnership
    └── meta-modal-integration.md   # Meta-level modal integration
```
## 为什么认知工具很重要

研究表明，使用认知工具进行结构化推理可以显著提高模型性能：

- **性能**：与数学推理基准相比，性能提升高达 16.6%
- **可靠性**：显著减少推理错误和幻觉
- **效率**：使用更少的总令牌获得更好的结果
- **灵活性**：适用于从数学到创意写作的跨领域

## 快速开始

要使用认知工具，请从中选择`cognitive-templates/`与您的任务匹配的模板：

```python
# Example: Using the "understand_question" cognitive tool
from cognitive_tools.templates import understand_question

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
understanding = llm.generate(understand_question(problem))
print(understanding)
```

对于更复杂的推理，请使用结构化提示程序 `cognitive-programs/`：

```python
# Example: Using a multi-step reasoning program
from cognitive_tools.programs import solve_math_problem

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
solution = solve_math_problem(problem, llm=my_llm_interface)
print(solution.steps)  # View step-by-step reasoning
print(solution.answer)  # View final answer
```

## 目录结构

- `cognitive-templates/`：用于不同推理作的可重用模板
- `cognitive-programs/`：具有类似代码模式的结构化提示程序
- `cognitive-schemas/`：不同领域的知识表示格式
- `cognitive-architectures/`： 结合多种工具的完整推理系统
- `integration/`：与其他组件（RAG、内存等）集成的指南

## 学习路径

1. **从模板开始**：了解基本的认知作
2. **探索程序**：了解如何将作组合到推理流中
3. **研究模式**：了解如何有效地构建知识
4. **主架构**：构建完整的推理系统
5. **集成组件**：与 RAG、内存和其他上下文工程组件相结合

## 衡量有效性

始终衡量认知工具对特定任务的影响：

```python
# Example: Measuring performance improvement
from cognitive_tools.evaluation import measure_reasoning_quality

baseline_score = measure_reasoning_quality(problem, baseline_prompt)
tool_score = measure_reasoning_quality(problem, cognitive_tool_prompt)

improvement = (tool_score / baseline_score - 1) * 100
print(f"Cognitive tool improved performance by {improvement:.1f}%")
```

## 研究基础

这些工具基于以下方面的研究：

- Brown et al. （2025）：“使用认知工具在语言模型中引发推理”
- Wei et al. （2023）：“在大型语言模型中提示引发推理的思维链”
- Huang et al. （2022）：“内心独白：在语言模型中体现知识和推理”

## 贡献

有运行良好的新认知工具模式吗？有关 [](../../.github/CONTRIBUTING.md) 提交模板、程序或体系结构的指南，请参阅 CONTRIBUTING.md。

## 后续步骤

- 请参阅 [understanding.md](./cognitive-templates/understanding.md) 了解基本理解工具
- 尝试 [basic-programs.md](./cognitive-programs/basic-programs.md) 基本程序结构
- 探索 [solver-architecture.md](./cognitive-architectures/solver-architecture.md) 以获得完整的问题解决系统
