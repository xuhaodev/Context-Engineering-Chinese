# 环境工程 – 结构概述
_面向下一代 LLM 编排的实用第一性原理手册_

> **为什么存在**这个仓库 
> 及时工程 = 考虑 **** 你说的话。 
> **上下文工程** = 考虑模型看到**的其他一切**。 
> 我们的目标是从头开始教授“其他一切”，以谦逊的态度和对简单、有效的代码的偏见。
> 
> 随着模型的发展，我们的方法也在发展：从离散标记到连续场，从静态提示到共振模式。

---

## 1. 领土地图

| 文件夹 | 角色 （简单英语） | 第一性原理隐喻 |
|--------|----------------------|---------------------------|
| `00_foundations` | 理论与直觉。微小的、独立的读数。 | 原子 → 分子 → 细胞 →器官 → 神经系统 → 场 |
| `10_guides_zero_to_hero` | 交互式指南，您可以 **运行**、调整、中断。 | 化学试剂组 |
| `20_templates` | 您可以复制/粘贴的插入式代码片段。 | 乐高积木 |
| `30_examples` | 端到端的迷你应用程序，一个比上一个难。 | 模式生物 |
| `40_reference` | 更深入的探讨和评估食谱。 | 教材附录 |
| `50_contrib` | 社区拉取请求的空间。 | 开放式实验室工作台 |
| `60_protocols` | 协议 shell、架构和框架。 | DNA 序列 |
| `70_agents` | 使用协议的自包含代理演示。 | 干细胞培养 |
| `80_field_integration` | 具有现场协议的端到端项目。 | 整个生物体 |
| `cognitive-tools` | 高级认知框架和架构。 | 扩展的神经系统 |

---

## 2. 学习路径（0 → 零 → 英雄）

### 基础 （了解基础知识）

1. **略脂 `README.md` （2 分钟）**  
   看看 “context” 在 prompts 之外还有什么含义。

2. **读取 `00_foundations/01_atoms_prompting.md` （5 分钟）**  
   *原子*：单个指令/示例。 
   为什么单独的原子经常表现不佳。

3. **继续浏览生物学隐喻链：**  
   - `02_molecules_context.md`： 少发包
   - `03_cells_memory.md`： 内存 & 日志
   - `04_organs_applications.md`：多步骤控制流
   - `05_cognitive_tools.md`： 心智模型扩展
   - `06_advanced_applications.md`： 实际实施
   - `07_prompt_programming.md`：类似代码的推理模式
   - `08_neural_fields_foundations.md`：上下文作为连续字段
   - `09_persistence_and_resonance.md`： 场动力学和吸引子
   - `10_field_orchestration.md`：协调多个字段

### 动手实践 （Learn by Doing）

4. **打开 `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   运行、修改、观察令牌计数。 
   笔记本单元格突出显示 **了** 为什么每行额外的行有帮助（或有害）。

5. **通过渐进式笔记本进行试验：**
   - 基本上下文作
   - 控制流和推理模式
   - 检索增强策略
   - 提示编程技术
   - 架构设计原则
   - 递归上下文模式
   - 神经场实现

### 应用技能（构建真正的解决方案）

6. **从以下位置 `20_templates/`**  复制模板 
   用作项目的起点：
   - `minimal_context.yaml` 用于基本项目
   - `control_loop.py` 用于交互式系统
   - `scoring_functions.py` 用于评估
   - `prompt_program_template.py` 用于推理任务
   - `schema_template.yaml` 对于结构化数据
   - `recursive_framework.py` 用于自我改进的系统
   - `neural_field_context.yaml` 用于基于现场的方法

7. **研究示例 `30_examples/`**  
   查看渐进式复杂系统的完整实现：
   - 基本对话代理
   - 数据注释系统
   - 多代理编排
   - 认知助手
   - RAG 实施
   - 神经场编排器

### 高级主题（掌握工艺）

8. **探索认知工具和协议：**
   - 高级推理框架 `cognitive-tools/`
   - 中的协议 shell 和 schema `60_protocols/`
   - 代理演示 `70_agents/`
   - 完成现场集成项目 `80_field_integration/`

9. **回馈社区：**
   - 查看 中的贡献准则 `50_contrib/README.md`
   - 检查评估标准 `40_reference/eval_checklist.md`
   - 打开包含您的改进或扩展的 PR

---

## 3. 生物隐喻进化

我们的存储库围绕一个扩展的生物学隐喻进行组织，这有助于使抽象概念具体化，并展示简单的组件如何构建到复杂的系统中：

```
                                   ┌───────────────────┐
                                   │  Neural Fields    │  08_neural_fields_foundations.md
                                   │  (Continuous      │  09_persistence_and_resonance.md
                                   │   Context Medium) │  10_field_orchestration.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                                   ┌───────┴───────────┐
                                   │ Neurobiological   │  05_cognitive_tools.md
                                   │ Systems           │  06_advanced_applications.md
                                   │ (Cognitive Tools) │  07_prompt_programming.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Organs            │  04_organs_applications.md
                             │  (Multi-Agent Systems)    │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Cells             │  03_cells_memory.md
                             │   (Memory Systems)        │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │       Molecules           │  02_molecules_context.md
                             │   (Few-Shot Examples)     │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Atoms             │  01_atoms_prompting.md
                             │    (Single Prompts)       │
                             └───────────────────────────┘
```

这种演变遵循生物系统复杂性的自然发展，并反映了日益复杂的环境工程方法的发展。

---

## 4. 高级上下文框架

### 协议 Shell 框架

协议为编排复杂的上下文作提供结构化的 shell。在目录中找到 `60_protocols/` ：

```
/recursive.field{
    intent="Define field properties and operations",
    input={
        field_state=<current_state>,
        new_information=<incoming_data>
    },
    process=[
        /field.measure{resonance, coherence, entropy},
        /pattern.detect{across="field_state"},
        /attractor.form{where="pattern_strength > threshold"},
        /field.evolve{with="new_information"}
    ],
    output={
        updated_field=<new_state>,
        metrics={resonance_score, coherence_delta}
    }
}
```

这些协议 shell 支持：
- 上下文作的声明性定义
- 递归自我提升模式
- 基于字段的上下文作
- 通过明确的流程步骤实现可审计性

### 认知工具框架

认知工具提供可重用的推理模式，以扩展模型功能。在目录中找到 `cognitive-tools/` ：

```
cognitive-tools/
├── cognitive-templates/     # Pattern templates for different reasoning modes
├── cognitive-programs/      # Structured prompt programs with code-like patterns
├── cognitive-schemas/       # Knowledge representation formats
├── cognitive-architectures/ # Complete reasoning systems
└── integration/            # Guides for integrating with other components
```

此框架支持：
- 模块化推理组件
- 特定于域的推理模式
- 与检索和记忆系统集成
- 推理质量的评估指标

### 神经场框架

神经场将上下文表示为连续的媒介，而不是离散的标记。实施方式：

```
00_foundations/08_neural_fields_foundations.md  # Conceptual foundation
00_foundations/09_persistence_and_resonance.md  # Field dynamics
00_foundations/10_field_orchestration.md        # Multi-field coordination
20_templates/neural_field_context.yaml          # Implementation template
30_examples/05_neural_field_orchestrator/       # Complete example
```

关键概念包括：
- 上下文作为连续的语义场
- 通过共振实现信息持久性
- 吸引子的形成和动力学
- 用于复杂任务的现场编排

---

## 5. Quiet Karpathy 指南（Style DNA）  

*保持原子→积累。*  
1. **最少的第一次传递** – 从最小的可行上下文开始。  
2. **迭代插件** – 仅添加模型明显缺乏的内容。  
3. **测量一切** – 代币成本、延迟、质量分数、场共振。  
4. **无情地删除** - 修剪胜过填充。  
5. **代码>幻灯片** – 每个概念都有一个可运行的单元格。
6. **递归思维** – 自我发展的环境。

---

## 6. 存储库结构详解

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # This structural map
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
│
├── 00_foundations/                  # First-principles theory
│   ├── 01_atoms_prompting.md        # Atomic instruction units
│   ├── 02_molecules_context.md      # Few-shot examples/context
│   ├── 03_cells_memory.md           # Stateful conversation layers
│   ├── 04_organs_applications.md    # Multi-step control flows
│   ├── 05_cognitive_tools.md        # Mental model extensions
│   ├── 06_advanced_applications.md  # Real-world implementations
│   ├── 07_prompt_programming.md     # Code-like reasoning patterns
│   ├── 08_neural_fields_foundations.md # Context as continuous fields
│   ├── 09_persistence_and_resonance.md # Field dynamics and attractors
│   └── 10_field_orchestration.md    # Coordinating multiple fields
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_prompt_programs.ipynb     # Structured reasoning programs
│   ├── 06_schema_design.ipynb       # Schema creation patterns
│   ├── 07_recursive_patterns.ipynb  # Self-referential contexts
│   └── 08_neural_fields.ipynb       # Working with field-based contexts
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── neural_field_context.yaml    # Field-based context template
│   ├── field_resonance_measure.py   # Field property measurement
│   └── context_audit.py             # Context analysis tool
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_cognitive_assistant/      # Advanced reasoning assistant
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   └── 05_neural_field_orchestrator/ # Field-based orchestration
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── neural_field_theory.md       # Comprehensive field theory
│   ├── symbolic_residue_guide.md    # Guide to residue tracking
│   └── protocol_reference.md        # Protocol shell reference
│
├── 50_contrib/                      # Community contributions
│   └── README.md                    # Contribution guidelines
│
├── 60_protocols/                    # Protocol shells and frameworks
│   ├── README.md                    # Protocol overview
│   ├── shells/                      # Protocol shell definitions
│   │   ├── attractor.co.emerge.shell      # Attractor co-emergence
│   │   ├── recursive.emergence.shell      # Recursive field emergence
│   │   ├── recursive.memory.attractor.shell # Memory persistence
│   │   └── field.resonance.scaffold.shell  # Field resonance
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v1.json     # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       └── protocolShell.v1.json           # Shell schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   └── 02_self_repair_loop/         # Self-repair protocol
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   └── 01_context_engineering_assistant/ # Field-based assistant
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   └── composition.md           # Combining multiple tools
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   └── program-examples.ipynb   # Interactive examples
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   └── schema-library.yaml      # Reusable schema library
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   └── architecture-examples.py # Implementation examples
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       └── evaluation-metrics.md    # Effectiveness measurement
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```

---

## 7. 如何贡献

在  中打开一个 PR。`50_contrib/` 
Checklist exists in `40_reference/eval_checklist.md`— 在提交之前运行它。

投稿时：
1. 遵循 Karpathy 风格指南
2. 包含可运行的代码示例
3. 衡量令牌使用情况和性能
4. 保持生物隐喻的一致性
5. 为任何新功能添加测试

---

## 8. 许可和归属

麻省理工学院。没有把关：复制、重新混合、重新分发。 
向 Andrej Karpathy 致敬，感谢他创造了这个框架。 
所有错误都是我们的错误;欢迎改进。
