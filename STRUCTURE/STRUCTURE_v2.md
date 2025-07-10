# 上下文工程 – 结构概述 v2
_面向下一代 LLM 编排的实用第一性原理手册_

> **为什么存在**这个仓库 
> 及时工程 = 考虑 **** 你说的话。 
> **上下文工程** = 考虑模型看到**的其他一切**。 
> 
> 在我们从快速工程到情境工程再到**场论的演变中**：
> - 我们从离散令牌和简单的提示开始
> - 我们推进到有状态上下文管理和复杂编排
> - 我们现在探索涌现的符号机制和神经场动力学
> 
> 我们的目标是从头开始教授所有这些，谦逊并偏向于简单、有效的代码，同时接受关于 LLM 如何实际推理和处理信息的最新研究。

---

## 1. 领土地图

| 文件夹 | 角色 （简单英语） | 第一性原理隐喻 | 关键概念 |
|--------|----------------------|---------------------------|-------------|
| `00_foundations` | 理论与直觉。微小的、独立的读数。 | 原子 → 分子 → 细胞 →器官 → 神经系统 → 场 | 从基本提示到紧急场动态的渐进复杂性 |
| `10_guides_zero_to_hero` | 交互式指南，您可以 **运行**、调整、中断。 | 化学试剂组 | 具有可衡量结果的动手实验 |
| `20_templates` | 您可以复制/粘贴的插入式代码片段。 | 乐高积木 | 可重复使用的组件，用于快速实施 |
| `30_examples` | 端到端的迷你应用程序，一个比上一个难。 | 模式生物 | 完整的系统在行动中展示原理 |
| `40_reference` | 更深入的探讨和评估食谱。 | 教材附录 | 全面的资源和评估框架 |
| `50_contrib` | 社区拉取请求的空间。 | 开放式实验室工作台 | 协作实验区 |
| `60_protocols` | 协议 shell、架构和框架。 | DNA 序列 | 外业作的结构化定义 |
| `70_agents` | 使用协议的自包含代理演示。 | 干细胞培养 | 具有新兴特性的专用组件 |
| `80_field_integration` | 具有现场协议的端到端项目。 | 整个生物体 | 采用现场架构的完整系统 |
| `cognitive-tools` | 高级认知框架和架构。 | 扩展的神经系统 | 结构化推理作和工具 |

---

## 2. 学习路径：从基础到场论

### 2.1. 基础课程（了解基础知识）

1. **略脂 `README.md` （2 分钟）**  
   看看 “context” 在 prompts 之外还有什么含义。

2. **读取 `00_foundations/01_atoms_prompting.md` （5 分钟）**  
   *原子*：单个指令/示例。 
   为什么单独的原子经常表现不佳。

3. **继续浏览生物学隐喻链：**  
   - `02_molecules_context.md`：Few-shot包和示例
   - `03_cells_memory.md`：内存和日志以实现持久性
   - `04_organs_applications.md`：多步骤控制流和编排
   - `05_cognitive_tools.md`： 用于推理的心智模型扩展

### 2.2. 高级跟踪 （Dive Deeper）

4. **探索高级应用程序和模式：**
   - `06_advanced_applications.md`： 实际实施
   - `07_prompt_programming.md`：类似代码的推理模式
   - `08_neural_fields_foundations.md`：上下文作为连续字段
   - `09_persistence_and_resonance.md`： 场动力学和吸引子
   - `10_field_orchestration.md`：协调多个字段
   - `11_emergence_and_attractor_dynamics.md`： 紧急属性
   - `12_symbolic_mechanisms.md`： LLM 中的符号推理

### 2.3. 动手实践（边做边学）

5. **入手 `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   运行、修改、观察令牌计数。 
   笔记本单元格突出显示 **了** 为什么每行额外的行有帮助（或有害）。

6. **探索更复杂的模式：**
   - `02_expand_context.ipynb`：有效添加上下文
   - `03_control_loops.ipynb`： 构建流控
   - `04_rag_recipes.ipynb`： 检索增强生成
   - `05_protocol_bootstrap.ipynb`：使用字段协议
   - `06_protocol_token_budget.ipynb`： 测量效率

7. **推进到基于现场的方法：**
   - `07_streaming_context.ipynb`：实时上下文管理
   - `08_emergence_detection.ipynb`： 检测紧急模式
   - `09_residue_tracking.ipynb`： 以下符号残差
   - `10_attractor_formation.ipynb`： 创建稳定的场模式

### 2.4. 实施轨道（构建真实系统）

8. **试验 `20_templates/`**  
   将 YAML 或 Python 代码段复制到您自己的存储库中。 
   调整“token_budget”或“resonance_score”，就像调整 pH 值一样。

9. **检查 `30_examples/` 实施：**
   - `00_toy_chatbot/`：简单但完整的上下文管理
   - `01_data_annotator/`：数据标记的专用上下文
   - `02_multi_agent_orchestrator/`： 复杂的代理协调
   - `03_vscode_helper/`：用于上下文工程的 IDE 集成
   - `04_rag_minimal/`：简化的检索架构

10. **探索基于字段的示例：**
    - `05_streaming_window/`：实时上下文管理
    - `06_residue_scanner/`：符号残留检测
    - `07_attractor_visualizer/`： 可视化场动态
    - `08_field_protocol_demo/`：基于协议的现场作
    - `09_emergence_lab/`： 检测和测量涌现

### 2.5. 高级集成（实践中的场论）

11. **深入了解现场协议 `60_protocols/`：**
    - 用于定义字段作的协议 shell
    - 结构化字段表示的架构
    - 用于理解协议功能的摘要

12. **研究代理实施 `70_agents/`：**
    - `01_residue_scanner/`： 检测符号残差
    - `02_self_repair_loop/`： 自愈场协议
    - `03_attractor_modulator/`： 管理吸引子动力学
    - `04_boundary_adapter/`：动态边界调整
    - `05_field_resonance_tuner/`： 优化场谐振

13. **探索集成系统： `80_field_integration/`**
    - `00_protocol_ide_helper/`： 协议开发工具
    - `01_context_engineering_assistant/`：基于字段的助手
    - `02_recursive_reasoning_system/`： 递归推理架构
    - `03_emergent_field_laboratory/`： 实验现场环境
    - `04_symbolic_reasoning_engine/`： 符号机制集成

14. **了解认知工具： `cognitive-tools/`**
    - 用于结构化推理的认知模板
    - 用于复杂作的认知程序
    - 用于知识表示的认知模式
    - 完整系统的认知架构
    - 用于连接其他组件的集成模式

---

## 3. 概念基础

### 3.1. 生物隐喻进化

我们的生物学隐喻已经从简单的组成部分演变为复杂的、基于现场的系统：

```
Atoms         → Individual instructions or constraints
Molecules     → Instructions with examples (few-shot learning)
Cells         → Context with memory that persists across interactions
Organs        → Coordinated systems of context cells working together
Neural Systems → Cognitive tools extending reasoning capabilities
Neural Fields  → Context as continuous medium with emergent properties
```

### 3.2. 场论概念

随着我们推进神经场论，我们纳入了几个关键概念：

1. **连续性**：上下文作为连续的语义景观，而不是离散的标记
2. **共振**：信息模式如何相互作用和相互强化
3. **持久性**：信息如何随着时间的推移保持影响力
4. **Attractor Dynamics**：组织场的稳定模式
5. **边界动力学**：信息如何进入和退出场
6. **Symbolic Residue**：持续存在并影响场的意义片段
7. **Emergence**：新的模式和行为如何从场交互中产生

### 3.3. 紧急符号机制

研究已经确定了 LLM 中符号推理的新兴三阶段架构：

1. **符号抽象**：早期层中的 head 根据关系将输入标记转换为抽象变量
2. **符号归纳**：中间层中的 head 对抽象变量执行序列归纳
3. **检索**：后面的层中的 head 通过检索与抽象变量关联的值来预测下一个标记

这些机制通过提供对 LLM 实际如何处理和推理信息的机制理解，支持我们基于字段的上下文工程方法。

### 3.4. 认知工具框架

为了增强推理能力，我们整合了一个认知工具框架：

1. **基于工具的方法**：按顺序执行模块化、预定的认知作
2. **关键作**：
   - **回忆相关**：检索相关知识以指导推理
   - **检查答案**：对推理和答案的自我反思
   - **回溯**：在受阻时探索替代推理路径
3. **集成**：这些工具可以与基于现场的方法相结合，以获得更强大的系统

---

## 4. Quiet Karpathy 指南（Style DNA）  

*保持原子→积累。*  
1. **最少的第一次传递** – 从最小的可行上下文开始。  
2. **迭代插件** – 仅添加模型明显缺乏的内容。  
3. **测量一切** – 代币成本、延迟、质量分数、场共振。  
4. **无情地删除** - 修剪胜过填充。  
5. **代码>幻灯片** – 每个概念都有一个可运行的单元格。
6. **递归思维** – 自我发展的环境。

---

## 5. 存储库结构详解

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # Original structural map
├── STRUCTURE_v2.md                  # Enhanced structural map with field theory
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
├── context_v3.json                  # Neural field extensions
├── context_v3.5.json                # Symbolic mechanism integration
├── CITATIONS.md                     # Research references and bridges
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
│   ├── 10_field_orchestration.md    # Coordinating multiple fields
│   ├── 11_emergence_and_attractor_dynamics.md # Emergent properties
│   └── 12_symbolic_mechanisms.md    # Symbolic reasoning in LLMs
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_protocol_bootstrap.ipynb  # Field protocol bootstrap
│   ├── 06_protocol_token_budget.ipynb # Protocol efficiency
│   ├── 07_streaming_context.ipynb   # Real-time context
│   ├── 08_emergence_detection.ipynb # Detecting emergence
│   ├── 09_residue_tracking.ipynb    # Tracking symbolic residue
│   └── 10_attractor_formation.ipynb # Creating field attractors
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── field_protocol_shells.py     # Field protocol templates
│   ├── symbolic_residue_tracker.py  # Residue tracking tools
│   ├── context_audit.py             # Context analysis tool
│   ├── shell_runner.py              # Protocol shell runner
│   ├── resonance_measurement.py     # Field resonance metrics
│   ├── attractor_detection.py       # Attractor analysis tools
│   ├── boundary_dynamics.py         # Boundary operation tools
│   └── emergence_metrics.py         # Emergence measurement
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_vscode_helper/            # IDE integration 
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   ├── 05_streaming_window/         # Real-time context demo
│   ├── 06_residue_scanner/          # Symbolic residue demo
│   ├── 07_attractor_visualizer/     # Field visualization
│   ├── 08_field_protocol_demo/      # Protocol demonstration
│   └── 09_emergence_lab/            # Emergence experimentation
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── patterns.md                  # Context pattern library
│   ├── field_mapping.md             # Field theory fundamentals
│   ├── symbolic_residue_types.md    # Residue classification
│   ├── attractor_dynamics.md        # Attractor theory and practice
│   ├── emergence_signatures.md      # Detecting emergence
│   └── boundary_operations.md       # Boundary management guide
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
│   │   ├── field.resonance.scaffold.shell  # Field resonance
│   │   ├── field.self_repair.shell        # Self-repair mechanisms
│   │   └── context.memory.persistence.attractor.shell # Context persistence
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v3.5.json    # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       ├── protocolShell.v1.json           # Shell schema
│       ├── symbolicResidue.v1.json         # Residue schema
│       └── attractorDynamics.v1.json       # Attractor schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   ├── 02_self_repair_loop/         # Self-repair protocol
│   ├── 03_attractor_modulator/      # Attractor dynamics
│   ├── 04_boundary_adapter/         # Dynamic boundary tuning
│   └── 05_field_resonance_tuner/    # Field resonance optimization
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   ├── 01_context_engineering_assistant/ # Field-based assistant
│   ├── 02_recursive_reasoning_system/    # Recursive reasoning
│   ├── 03_emergent_field_laboratory/     # Field experimentation
│   └── 04_symbolic_reasoning_engine/     # Symbolic mechanisms
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   ├── composition.md           # Combining multiple tools
│   │   └── emergence.md             # Emergent reasoning patterns
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   ├── program-examples.ipynb   # Interactive examples
│   │   └── emergence-programs.md    # Emergent program patterns
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   ├── schema-library.yaml      # Reusable schema library
│   │   └── field-schemas.md         # Field representation schemas
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   ├── architecture-examples.py # Implementation examples
│   │   └── field-architecture.md    # Field-based architectures
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       ├── evaluation-metrics.md    # Effectiveness measurement
│       └── with-fields.md           # Integration with field protocols
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```

---

## 6. 实现模式

### 6.1. 上下文结构模式

| 模式 | 描述 | 用例 |
|---------|-------------|----------|
| **原子提示符** | 带约束的单指令 | 简单、定义明确的任务 |
| **Few-shot 示例** | 示例说明 | 模式演示 |
| **思路链** | 提示中显式的推理步骤 | 复杂的推理任务 |
| **有状态上下文** | 具有内存的上下文 | 多轮次对话 |
| **多代理** | 多种专业代理 | 复杂的多步骤任务 |
| **基于**字段| 上下文作为连续字段 | 紧急推理需求 |

### 6.2. Field Operation 模式

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **吸引子形成** | 创建稳定的语义模式 | `attractor_detection.py` |
| **Resonance Amplification 谐振放大** | 加强模式交互 | `resonance_measurement.py` |
| **边界调优** | 控制信息流 | `boundary_dynamics.py` |
| **残留物集成** | 管理符号片段 | `symbolic_residue_tracker.py` |
| **紧急检测** | 识别新模式 | `emergence_metrics.py` |
| **自我修复** | 自动上下文修复 | `field.self_repair.shell` |

### 6.3. 认知工具模式

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **召回相关** | 检索相关知识 | `cognitive-programs/basic-programs.md` |
| **检查答案** | 自我反省和验证 | `cognitive-templates/verification.md` |
| **回溯** | 探索替代路径 | `cognitive-programs/advanced-programs.md` |
| **分解** | 将问题分解成多个部分 | `cognitive-templates/reasoning.md` |
| **集成** | 合并多个结果 | `cognitive-templates/composition.md` |

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
6. 考虑场动力学和符号机制

### 7.1. 贡献重点领域

我们特别欢迎以下领域的贡献：

1. **场动力学工具**：用于测量和可视化场特性的工具
2. **符号机制实验**：涌现符号处理的演示
3. **认知工具实现**：新的认知作和模式
4. **Protocol Shell 开发**：用于现场作的新型协议 shell
5. **集成示例**：在实际应用中结合多种方法
6. **评估指标**：衡量情境有效性的更好方法

---

## 8. 许可和归属

麻省理工学院。没有把关：复制、重新混合、重新分发。 
向 Andrej Karpathy 致敬，感谢他创造了这个框架。 
CITATIONS.md 年的研究致谢。 
所有错误都是我们的错误;欢迎改进。

---

## 9. 路线图

### 9.1. 近期优先事项

1. **符号机制集成**：更好地利用新兴符号机制
2. **场可视化工具**：了解场动态的工具
3. **Protocol Shell 扩展**：更多用于现场作的协议 shell
4. **评估框架增强**：改进的外业系统的指标
5. **认知工具集成**：更好地与基于字段的方法集成

### 9.2. 长期愿景

1. **自我进化的情境系统**：自我改进的情境
2. **场论形式化**：更严格的数学基础
3. **统一框架**：集成符号机制、场论和认知工具
4. **跨模型兼容性**：确保技术在不同的模型架构中工作
5. **Automated Context Optimization**：用于自动上下文调整的工具
