# 研究方案

> *“研究是正式的好奇心。它是有目的的戳戳和窥探。*
>
> **— 佐拉·尼尔·赫斯顿**

## 研究方案简介

研究方案将通常混乱的非线性知识发现过程转变为结构化、高效的工作流程，从而始终如一地产生可靠的见解。通过建立明确的调查和分析框架，这些协议可帮助您清晰、有目的地浏览复杂的信息环境。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            RESEARCH PROTOCOL BENEFITS               │
│                                                     │
│  • Systematic knowledge discovery and validation    │
│  • Reduced cognitive bias in analysis               │
│  • Efficient exploration of complex topics          │
│  • Clear progression from questions to insights     │
│  • Traceable reasoning and evidence paths           │
│  • Repeatable processes for knowledge development   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

本指南为寻求常识的场景提供了现成的研究方案，以及实施指南和性能指标。每个协议都遵循我们的 NOCODE 原则：导航、编排、控制、优化、部署和发展。

## 如何使用本指南

1. **选择符合您研究目标的**实验方案
2. **复制协议模板** （包括提示符）并进行自定义
3. ** 在交互开始时向 AI 助手**提供完整的协议
4. **遵循从初始问题到验证见解的**结构化流程
5. **监控指标** 以评估有效性
6. **迭代和完善** 您的实验方案，为将来的研究做好准备

**苏格拉底问题**：您目前认为哪些类型的研究最具挑战性或最耗时？您通常在知识发现过程中的哪些地方遇到瓶颈？

---

## 1. 文献综述协议

**何时使用此协议：**
需要全面了解某个主题的现有知识？该实验方案将指导您系统地探索可用信息，非常适合主题概述、最先进的评估或知识综合。

```
Prompt: I need to conduct a comprehensive literature review on recent advances in quantum machine learning algorithms. I'm particularly interested in developments over the last three years, practical applications emerging in the field, and the most significant technical challenges still to be overcome. Please help me develop a systematic overview of the current state of knowledge in this area.

Protocol:
/research.literature{
    intent="Develop comprehensive understanding of existing knowledge on a topic",
    input={
        research_topic="Recent advances in quantum machine learning algorithms (last three years)",
        key_questions=[
            "What are the most significant theoretical advances in quantum machine learning algorithms?",
            "What practical applications are emerging from these advances?",
            "What technical challenges remain to be overcome in the field?"
        ],
        scope_boundaries={
            timeframe: "Last three years (2022-2025)",
            inclusion: "Peer-reviewed research, technical reports from major labs, significant preprints",
            exclusion: "Popular science coverage, introductory materials, pre-2022 foundations"
        },
        organization_approach="Thematic analysis with chronological progression within themes"
    },
    process=[
        /map{
            action="Create conceptual framework of the field",
            elements=[
                "key theoretical foundations",
                "major research streams",
                "significant applications",
                "evolving terminology and concepts"
            ]
        },
        /explore{
            action="Identify and analyze key contributions",
            for_each="research_stream",
            elements=[
                "seminal works and breakthroughs",
                "methodological innovations",
                "empirical findings and results",
                "limitations and controversies"
            ]
        },
        /synthesize{
            action="Develop integrated understanding",
            approaches=[
                "identify emerging patterns and trends",
                "map relationships between research streams",
                "contrast competing theories or approaches",
                "note consensus views and open questions"
            ]
        },
        /evaluate{
            action="Assess quality and significance of research",
            criteria=[
                "methodological rigor",
                "empirical support",
                "theoretical coherence",
                "practical implications"
            ]
        },
        /organize{
            action="Structure findings into coherent framework",
            elements=[
                "thematic organization",
                "chronological progression within themes",
                "highlight relationships and contrasts",
                "identify gaps and opportunities"
            ]
        }
    ],
    output={
        knowledge_synthesis="Comprehensive overview of current state of knowledge",
        key_findings="Summary of most significant insights and developments",
        research_map="Visual or structured representation of the field",
        gap_analysis="Identification of unanswered questions and opportunities"
    }
}
```

### 实施指南

1. **主题定义**：
   - 定义特定的重点和范围
   - 构建关键问题以指导探索
   - 考虑广度和深度要求

2. **范围边界设置**：
   - 建立明确的时间框架参数
   - 定义纳入和排除标准
   - 考虑资源限制和优先级

3. **组织方法选择**：
   - 根据研究目标选择框架
   - 选项包括主题、时间顺序、方法
   - 考虑针对复杂主题的混合方法

4. **关键问题表述**：
   - 制定 3-5 个核心问题来指导审查
   - 确保问题具体而全面
   - 包括事实问题和分析问题

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 覆盖广度 | 跨主题领域的全面性 | 包括所有重要的子区域 |
| 源质量 | 来源的可信度和相关性 | 高质量、有代表性的来源 |
| 综合深度 | 将信息整合成连贯的整体 | 识别清晰的模式和关系 |
| 差距识别 | 识别知识局限性 | 未回答问题的显式映射 |

## 2. 分析协议

**何时使用此协议：**
需要从复杂的信息或数据中提取有意义的见解？该方案可指导您完成系统的分析过程，非常适合用于趋势分析、比较评估、模式识别或批判性评估。

```
Prompt: I need to analyze the key factors driving the rapid growth of renewable energy adoption in different global markets. I have data on policy frameworks, technology costs, market structures, and investment trends across several regions. I want to understand which factors are most influential, how they interact, and how they vary across markets to develop strategic insights for our clean energy investment portfolio.

Protocol:
/research.analyze{
    intent="Extract meaningful insights through systematic analytical process",
    input={
        analysis_subject="Factors driving renewable energy adoption across global markets",
        analytical_framework={
            dimensions: ["Policy frameworks", "Technology costs", "Market structures", "Investment trends"],
            regions: ["North America", "Europe", "Asia-Pacific", "Emerging markets"],
            timeframe: "Last 5 years (2020-2025)"
        },
        key_questions=[
            "Which factors most strongly correlate with rapid renewable adoption?",
            "How do these factors interact and influence each other?",
            "How do influential factors vary across different market contexts?",
            "What patterns emerge in markets with highest adoption rates?"
        ],
        analysis_approach="Multi-dimensional comparative analysis with causal relationship mapping"
    },
    process=[
        /decompose{
            action="Break subject into analyzable components",
            elements=[
                "identify constituent factors and variables",
                "establish relevant metrics and indicators",
                "map relationships and dependencies",
                "define analytical boundaries and limitations"
            ]
        },
        /examine{
            action="Analyze each component systematically",
            for_each="dimension",
            approaches=[
                "comparative analysis across regions",
                "trend analysis over time",
                "pattern identification",
                "correlation and possible causation mapping"
            ]
        },
        /contextualize{
            action="Consider relevant context and influences",
            elements=[
                "historical development and precedents",
                "external factors and influences",
                "systemic constraints and enablers",
                "competing or alternative perspectives"
            ]
        },
        /integrate{
            action="Synthesize component analyses into holistic understanding",
            techniques=[
                "identify cross-component patterns",
                "map causal or influence networks",
                "develop explanatory frameworks",
                "test alternative interpretations"
            ]
        },
        /validate{
            action="Critically evaluate analytical conclusions",
            approaches=[
                "check against available evidence",
                "identify assumptions and limitations",
                "consider counter-arguments or exceptions",
                "assess confidence levels for findings"
            ]
        }
    ],
    output={
        key_insights="Primary analytical findings with supporting evidence",
        factor_analysis="Detailed examination of each key factor and its influence",
        relationship_map="Visual or structured representation of how factors interact",
        strategic_implications="Practical applications of analytical findings"
    }
}
```

### 实施指南

1. **主题定义**：
   - 清晰地阐明分析重点
   - 定义范围和边界
   - 确定需要检查的具体方面

2. **分析框架选择**：
   - 选择合适的维度进行分析
   - 定义要比较的类别或区域
   - 建立相关的时间框架

3. **关键问题表述**：
   - 制定具体问题以指导分析
   - 包括描述性问题、比较性问题和因果问题
   - 专注于具有战略或实际价值的问题

4. **分析方法选择**：
   - 选择适合主题和问题的方法
   - 考虑比较、时间、因果或系统方法
   - 定义适当的分析粒度级别

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 分析严谨性 | 系统、循证检查 | 清晰的逻辑进展 |
| 洞察价值 | 研究结果的意义和有用性 | 不明显、可作的见解 |
| 关系映射 | 因子交互作用的清晰度 | 明确的因果或影响途径 |
| 验证质量 | 结论的批判性检验 | 多种验证方法 |

## 3. 战略远见协议

**何时使用此协议：**
需要预测未来发展并为新出现的机遇或挑战做好准备？该协议指导您进行系统的未来探索，非常适合趋势分析、情景开发、战略规划或创新预测。

```
Prompt: I need to develop a strategic foresight analysis for the healthcare technology sector over the next decade. Our organization needs to understand emerging technologies, shifting patient and provider needs, potential regulatory changes, and how these factors might reshape healthcare delivery models. We want to identify strategic opportunities and potential disruption risks to inform our long-term R&D investments.

Protocol:
/research.foresight{
    intent="Systematically explore future developments and strategic implications",
    input={
        domain="Healthcare technology sector",
        time_horizon="10 years (2025-2035)",
        focal_areas=[
            "Emerging technologies and their adoption trajectories",
            "Evolving patient and provider needs and expectations",
            "Regulatory environment and policy developments",
            "Healthcare delivery model transformation"
        ],
        key_uncertainties=[
            "Pace and direction of AI integration in clinical decision-making",
            "Patient data ownership and privacy regulation evolution",
            "Healthcare payment model transformation",
            "Public vs. private sector roles in healthcare innovation"
        ],
        strategic_context="Informing long-term R&D investment decisions for healthcare technology company"
    },
    process=[
        /scan{
            action="Identify and assess signals of change",
            elements=[
                "emerging trends and developments",
                "potential disruptive forces",
                "weak signals of systemic change",
                "stabilizing and constraining factors"
            ]
        },
        /analyze{
            action="Evaluate implications and interactions of trends",
            approaches=[
                "systems analysis of interrelated factors",
                "stakeholder impact assessment",
                "adoption and diffusion pattern analysis",
                "regulatory and policy evolution mapping"
            ]
        },
        /construct{
            action="Develop multiple plausible future scenarios",
            technique="Critical uncertainties matrix",
            elements=[
                "scenario narratives and evolution paths",
                "key milestones and indicators",
                "stakeholder positions and responses",
                "critical success factors in each scenario"
            ]
        },
        /assess{
            action="Evaluate strategic implications of scenarios",
            for_each="scenario",
            elements=[
                "opportunities and challenges",
                "required capabilities and resources",
                "competitive positioning",
                "risk factors and vulnerabilities"
            ]
        },
        /recommend{
            action="Develop strategic options and monitoring framework",
            elements=[
                "robust strategies across multiple futures",
                "hedging and option-creating approaches",
                "early indicator monitoring system",
                "adaptive strategy framework"
            ]
        }
    ],
    output={
        trend_analysis="Assessment of key trends and driving forces",
        scenario_portfolio="Set of distinct, plausible future scenarios",
        strategic_implications="Opportunities, challenges, and strategic options",
        monitoring_framework="Early indicators and adaptation triggers"
    }
}
```

### 实施指南

1. **域定义**：
   - 明确指定焦点区域和边界
   - 考虑相关的相邻域
   - 定义适当的粒度级别

2. **时间范围设置**：
   - 选择与规划需求相关的时间范围
   - 在适当的时候考虑多个水平
   - 与组织规划周期保持一致

3. **焦点区域选择**：
   - 确定要探索的关键域
   - 包括内部和外部因素
   - 考虑技术、社会、经济和监管维度

4. **不确定性识别**：
   - 查明影响较大的关键不确定性
   - 关注真正不确定的元素，而不是趋势
   - 考虑二阶不确定性和交互作用

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 情景合理性 | 逻辑连贯性和可信度 | 没有神奇的想法或矛盾 |
| 情景独特性 | futures 之间的有意义差异 | 清晰、对比鲜明的未来 |
| 战略相关性 | 对决策的可行影响 | 与战略选择的明确联系 |
| 监控值 | 早期预警框架的有用性 | 可观察的领先指标 |

## 4. 问题调查协议

**何时使用此协议：**
需要了解原因或维度不明确的复杂问题？该协议指导您完成系统性的问题探索，非常适合用于根本原因分析、问题框架、问题诊断或挑战映射。

```
Prompt: I need to investigate the underlying causes of our company's declining customer retention rates over the past 18 months. Despite several improvement initiatives, retention continues to drop across most customer segments. I want to develop a comprehensive understanding of the problem, including potential root causes, systemic factors, and relationship to other business metrics before we develop our next intervention strategy.

Protocol:
/research.problem{
    intent="Systematically investigate and understand complex problems",
    input={
        problem_statement="Declining customer retention rates over past 18 months despite improvement initiatives",
        problem_context="B2B SaaS company with enterprise customers across multiple industries",
        known_elements={
            symptoms: ["Increasing churn across most segments", "Declining product usage metrics", "Reduced expansion revenue"],
            attempted_solutions: ["Customer success team expansion", "User interface improvements", "New feature additions"],
            affected_stakeholders: ["Existing customers", "Account management team", "Product development", "Executive leadership"]
        },
        investigation_goals=["Identify root causes", "Map systemic factors", "Understand past solution failures", "Develop comprehensive problem frame"]
    },
    process=[
        /define{
            action="Clarify problem boundaries and manifestations",
            elements=[
                "precise problem definition and scope",
                "key metrics and indicators",
                "historical pattern and progression",
                "variation across contexts or segments"
            ]
        },
        /explore{
            action="Investigate potential causal factors",
            approaches=[
                "stakeholder perspective analysis",
                "comparative assessment across segments",
                "temporal correlation with external factors",
                "system relationship mapping"
            ]
        },
        /hypothesize{
            action="Develop potential explanations",
            techniques=[
                "multiple hypothesis formulation",
                "causal chain mapping",
                "system dynamics modeling",
                "contributing factor weighting"
            ]
        },
        /test{
            action="Evaluate hypotheses against available evidence",
            methods=[
                "evidence mapping to hypotheses",
                "identification of confirming/disconfirming data",
                "assessment of explanation power",
                "consideration of alternative interpretations"
            ]
        },
        /synthesize{
            action="Develop integrated problem understanding",
            elements=[
                "root cause identification",
                "systemic factor mapping",
                "interrelationship analysis",
                "comprehensive problem frame"
            ]
        }
    ],
    output={
        problem_analysis="Comprehensive assessment of the problem and its dimensions",
        causal_model="Map of root causes and contributing factors with relationships",
        evidence_assessment="Evaluation of supporting evidence for key findings",
        reframed_problem="Clarified problem statement with systemic context"
    }
}
```

### 实施指南

1. **问题陈述表述：**
   - 清楚地阐明观察到的问题
   - 关注症状而不是假设的原因
   - 包括范围和边界

2. **上下文描述**：
   - 提供相关的组织和环境因素
   - 注意历史发展和变化
   - 包括利益相关者环境

3. **已知元素文档**：
   - 列出观察到的症状和表现
   - 记录以前的解决方案尝试和结果
   - 确定受影响的利益相关者和影响

4. **调查目标设定**：
   - 定义调查所需的具体结果
   - 包括分析和实践目标
   - 考虑决策的信息需求

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 因果深度 | 确定根本原因 | 超越症状到根驱动 |
| 系统视角 | 考虑更广泛的背景 | 映射关系和交互 |
| 证据质量 | 支持结论 | 主要发现的多个证据来源 |
| 解决方案途径 | 从理解到行动的明确路径 | 干预的可作影响 |

## 5. 比较评估协议

**何时使用此协议：**
需要系统地比较多个选项、方法或实体？该协议可指导您进行结构化比较，非常适合解决方案评估、竞争分析、方法评估或决策支持。

```
Prompt: I need to conduct a comprehensive comparison of the three leading enterprise database technologies (Oracle, Microsoft SQL Server, and PostgreSQL) to determine the best fit for our organization's new data platform. We need to evaluate performance characteristics, cost structures, scalability, security features, ecosystem support, and future development roadmaps to make an informed technology selection decision.

Protocol:
/research.compare{
    intent="Systematically compare multiple options or entities with structured framework",
    input={
        comparison_subjects=["Oracle Database", "Microsoft SQL Server", "PostgreSQL"],
        evaluation_dimensions=[
            {name: "Performance", weight: 9, criteria: ["Query execution speed", "Indexing efficiency", "Concurrency handling"]},
            {name: "Cost structure", weight: 8, criteria: ["Licensing model", "Operational costs", "Scaling costs"]},
            {name: "Scalability", weight: 7, criteria: ["Vertical scaling capabilities", "Horizontal scaling options", "Performance at scale"]},
            {name: "Security", weight: 9, criteria: ["Access control granularity", "Encryption options", "Compliance capabilities"]},
            {name: "Ecosystem", weight: 6, criteria: ["Tool availability", "Talent pool", "Community support"]},
            {name: "Future roadmap", weight: 7, criteria: ["Innovation trajectory", "Vendor stability", "Feature development pace"]}
        ],
        comparison_context="Enterprise data platform selection for financial services organization",
        decision_criteria="Balance of performance, security, and total cost of ownership with consideration for future scalability needs"
    },
    process=[
        /establish{
            action="Create structured comparison framework",
            elements=[
                "comparison dimensions and criteria",
                "evaluation methodology",
                "scoring or assessment approach",
                "contextual considerations"
            ]
        },
        /analyze{
            action="Assess each subject across dimensions",
            for_each="comparison_subject",
            elements=[
                "detailed assessment against each criterion",
                "identification of strengths and weaknesses",
                "contextual performance factors",
                "distinctive characteristics or capabilities"
            ]
        },
        /compare{
            action="Conduct direct comparison across subjects",
            approaches=[
                "dimension-by-dimension comparative analysis",
                "relative strength assessment",
                "gap analysis",
                "trade-off identification"
            ]
        },
        /contextualize{
            action="Evaluate relevance to specific situation",
            elements=[
                "alignment with specific requirements",
                "implementation considerations",
                "organizational fit factors",
                "risk and opportunity assessment"
            ]
        },
        /synthesize{
            action="Develop integrated comparative assessment",
            elements=[
                "overall comparison summary",
                "key differentiating factors",
                "decision-relevant insights",
                "contextual recommendations"
            ]
        }
    ],
    output={
        comparison_matrix="Structured assessment across all dimensions and subjects",
        key_differentiators="Critical factors that distinguish the options",
        contextual_assessment="Evaluation of fit for specific situation",
        recommendation_framework="Decision support with conditional recommendations"
    }
}
```

### 实施指南

1. **主题选择**：
   - 确定适当的比较候选者
   - 确保相似的类别或分类
   - 考虑相关替代方案

2. **尺寸定义**：
   - 选择 4-8 个关键比较类别
   - 分配相对重要性权重
   - 在每个维度中定义特定标准

3. **上下文规范**：
   - 描述相关情况或要求
   - 注意特定的约束或首选项
   - 包括决策参数

4. **决策标准澄清**：
   - 阐明比较将如何为决策提供信息
   - 注意优先因素或要求
   - 包含任何不可协商的要素

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 框架全面性 | 相关维度的覆盖范围 | 包括所有决策关键因素 |
| 评估深度 | 受试者评估的彻底性 | 对每项标准进行实质性分析 |
| 比较净度 | 选项之间的明显对比 | 关键维度的明确区分 |
| 上下文相关性 | 与特定情况的联系 | 明确应用于决策上下文 |

## 6. 研究合成协议

**何时使用此协议：**
需要将不同的信息整合到连贯、有意义的框架中？该协议指导您完成知识合成 - 非常适合跨学科集成、构建概念模型、创建框架或开发理论。

```
Prompt: I need to synthesize research findings from multiple disciplines (psychology, behavioral economics, neuroscience, and social media studies) to develop a comprehensive framework for understanding digital behavior change mechanisms. The goal is to create an integrated model that explains how different interventions influence online user behavior, particularly around sustainable consumption choices.

Protocol:
/research.synthesize{
    intent="Integrate diverse information into coherent frameworks or models",
    input={
        synthesis_goal="Develop comprehensive framework for digital behavior change mechanisms",
        knowledge_domains=[
            {domain: "Psychology", elements: ["Cognitive biases", "Motivation theory", "Habit formation"]},
            {domain: "Behavioral Economics", elements: ["Choice architecture", "Incentive structures", "Temporal discounting"]},
            {domain: "Neuroscience", elements: ["Reward pathways", "Attention mechanisms", "Decision processes"]},
            {domain: "Social Media Studies", elements: ["Engagement patterns", "Social influence", "Platform design effects"]}
        ],
        integration_level="Theoretical framework with practical application dimensions",
        application_context="Digital interventions for sustainable consumption choices"
    },
    process=[
        /map{
            action="Create knowledge landscape across domains",
            elements=[
                "key concepts and principles",
                "established relationships and mechanisms",
                "complementary and contradictory perspectives",
                "research quality and consensus levels"
            ]
        },
        /identify{
            action="Discover integration points and patterns",
            approaches=[
                "cross-domain concept mapping",
                "shared mechanism identification",
                "complementary explanation recognition",
                "gap and contradiction analysis"
            ]
        },
        /construct{
            action="Develop integrated framework or model",
            elements=[
                "organizing principles and structure",
                "key components and relationships",
                "causal or influence pathways",
                "boundary conditions and contexts"
            ]
        },
        /validate{
            action="Evaluate synthesis against evidence",
            methods=[
                "explanatory power assessment",
                "empirical support mapping",
                "logical consistency checking",
                "domain expert perspective consideration"
            ]
        },
        /refine{
            action="Enhance framework clarity and utility",
            approaches=[
                "conceptual clarity improvement",
                "practical application dimension development",
                "visual representation creation",
                "explanatory narrative construction"
            ]
        }
    ],
    output={
        integrated_framework="Comprehensive model synthesizing multi-domain insights",
        key_mechanisms="Core processes identified across domains",
        application_guidance="Practical implementation of theoretical framework",
        research_implications="Future research directions and open questions"
    }
}
```

### 实施指南

1. **综合目标定义**：
   - 清晰地阐明集成目的
   - 定义预期的输出类型和级别
   - 指定预期应用

2. **知识域映射**：
   - 确定相关领域和学科
   - 从每个域中选择关键元素
   - 注意相对发展和证据水平

3. **集成级别选择**：
   - 选择合适的合成深度
   - 选项范围从概念图到理论构建
   - 同时考虑理论和实践两个维度

4. **应用程序上下文规范**：
   - 定义预期的用例或场景
   - 注意特定要求或限制
   - 考虑利益相关者的需求和观点

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 集成质量 | 跨域的有意义连接 | 连贯而不是强制集成 |
| 框架实用程序 | 综合的实用价值 | 可作的含义和应用 |
| 解释力 | 能够解释各种现象 | 关键机制的全面解释 |
| 创新价值 | 来自集成的新见解 | 在单个域中不可见的新透视 |

## 7. 专家咨询协议

**何时使用此协议：**
需要从领域专家那里提取和构建专业知识？该方案指导您完成系统的知识获取，非常适合专家访谈、专业知识文档、最佳实践收集或智慧采集。

```
Prompt: I need to conduct an expert consultation to document best practices in cybersecurity incident response for financial institutions. I'm preparing for a structured interview with our organization's Chief Information Security Officer and want to ensure I capture their expertise comprehensively, especially regarding the initial detection and containment phases of incidents involving potential data breaches.

Protocol:
/research.expert{
    intent="Extract and structure specialized knowledge from domain expertise",
    input={
        domain="Cybersecurity incident response for financial institutions",
        expertise_focus="Best practices for detection and containment of potential data breaches",
        expert_context="Chief Information Security Officer with 15+ years experience",
        knowledge_goals=[
            "Critical first-response procedures and decision points",
            "Common pitfalls and their prevention",
            "Effective containment strategies and their situational application",
            "Communication protocols during breach investigation",
            "Evaluation frameworks for incident severity and scope"
        ],
        knowledge_structure="Procedural framework with decision criteria and contextual factors"
    },
    process=[
        /prepare{
            action="Develop knowledge extraction strategy",
            elements=[
                "domain map and terminology",
                "hierarchical question framework",
                "critical incident technique preparation",
                "knowledge validation approach"
            ]
        },
        /extract{
            action="Systematically elicit expert knowledge",
            techniques=[
                "scenario-based exploration",
                "process tracing and think-aloud protocols",
                "comparative case analysis",
                "tacit knowledge surfacing",
                "decision criteria elicitation"
            ]
        },
        /clarify{
            action="Ensure precise understanding of expert input",
            approaches=[
                "terminology and concept verification",
                "boundary condition exploration",
                "exception and edge case identification",
                "confidence level assessment"
            ]
        },
        /structure{
            action="Organize extracted knowledge into coherent framework",
            elements=[
                "procedural sequences and workflows",
                "decision frameworks and criteria",
                "contextual factors and considerations",
                "causal relationships and dependencies"
            ]
        },
        /validate{
            action="Verify knowledge accuracy and completeness",
            methods=[
                "expert review and correction",
                "scenario-based testing",
                "internal consistency checking",
                "comprehensiveness assessment"
            ]
        }
    ],
    output={
        knowledge_framework="Structured representation of expert knowledge",
        best_practices="Documented procedures and approaches",
        decision_guidance="Criteria and considerations for key decisions",
        application_contexts="Situational factors affecting implementation"
    }
}
```

### 实施指南

1. **域规范**：
   - 明确定义知识领域和边界
   - 专注于特定方面而不是整个领域
   - 考虑广度和深度要求

2. **专业重点定义**：
   - 阐明要提取的特定知识
   - 优先考虑最有价值或最紧迫的领域
   - 考虑显性和隐性知识

3. **专家上下文文档**：
   - 注意相关背景和经验
   - 包括特定角色或职责
   - 考虑独特的视角或专业化

4. **知识目标设定**：
   - 定义所需的具体结果
   - 包括事实和程序知识
   - 考虑决策和情境理解

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 知识深度 | 捕获的专业技能水平 | 从表面到深厚的专业知识 |
| 知识结构 | 组织和辅助功能 | 清晰、合乎逻辑的知识框架 |
| 隐性捕获 | 隐性知识的提取 | 阐明“know-how”而不仅仅是“know-what” |
| 情境理解 | 情境应用因素 | 关于何时以及如何应用知识的明确指导 |

## 8. 研究设计协议

**何时使用此协议：**
需要开发一种系统的方法来回答研究问题吗？该方案指导您完成研究方法开发——非常适合研究设计、调查计划、方法选择或研究计划开发。

```
Prompt: I'm planning a research study to understand how gamification elements impact user engagement and retention in health and wellness apps. I need to design a comprehensive methodology that will provide reliable insights into which game mechanics most effectively drive sustained engagement across different user demographics and health goals.

Protocol:
/research.design{
    intent="Develop systematic methodology to answer research questions",
    input={
        research_questions=[
            "Which gamification elements most effectively increase engagement in health apps?",
            "How do demographic factors moderate gamification effectiveness?",
            "What is the relationship between specific game mechanics and long-term retention?",
            "How do different health goals affect optimal gamification approaches?"
        ],
        research_context="Understanding engagement drivers in health and wellness mobile applications",
        methodological_constraints=[
            "Must be implementable within 4-month timeframe",
            "Access to existing app users for testing and data collection",
            "Mixed methods approach preferred",
            "Ethical considerations for health-related behavioral research"
        ],
        desired_outcomes="Actionable insights to guide gamification feature development priorities"
    },
    process=[
        /frame{
            action="Refine research questions and approach",
            elements=[
                "question specificity and testability",
                "conceptual framework development",
                "variable identification and operationalization",
                "hypothesis formulation"
            ]
        },
        /design{
            action="Develop research methodology",
            components=[
                "research approach selection (qualitative, quantitative, mixed)",
                "study design specification",
                "sampling strategy and participant selection",
                "data collection methods and instruments",
                "analytical approach planning"
            ]
        },
        /validate{
            action="Evaluate methodological quality and appropriateness",
            criteria=[
                "validity and reliability assessment",
                "bias identification and mitigation",
                "ethical consideration review",
                "feasibility and resource alignment",
                "limitations acknowledgment"
            ]
        },
        /plan{
            action="Create detailed implementation framework",
            elements=[
                "phased research timeline",
                "resource allocation and requirements",
                "research instruments and protocols",
                "data management and analysis plan",
                "contingency and adaptation strategies"
            ]
        },
        /communicate{
            action="Develop research documentation",
            components=[
                "methodology justification and rationale",
                "detailed procedure descriptions",
                "anticipated outcomes and applications",
                "limitations and constraints acknowledgment",
                "ethical and quality assurance measures"
            ]
        }
    ],
    output={
        research_design="Comprehensive methodology with rationale",
        implementation_plan="Detailed framework for execution",
        measurement_approach="Data collection and analysis methods",
        research_limitations="Acknowledged constraints and mitigations"
    }
}
```

### 实施指南

1. **研究问题制定**：
   - 提出清晰、具体、可回答的问题
   - 确保适当的范围和重点
   - 同时考虑理论和实践两个维度

2. **研究背景描述**：
   - 提供相关背景和设置
   - 注意现有知识和差距
   - 考虑利益相关者的利益和需求

3. **约束标识**：
   - 列出实际限制和界限
   - 包括时间范围、资源和访问权限
   - 注意道德或监管注意事项

4. **结果定义**：
   - 阐明预期的研究成果
   - 定义如何使用结果
   - 同时考虑学术成果和应用成果

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 方法论对齐 | 问题和方法之间的匹配 | 从方法到答案的直接路径 |
| 设计严谨性 | 科学的方法质量 | 符合学科标准 |
| 可行性 | 实施的实用性 | 在约束范围内可执行 |
| 预期有效期 | 结果的可能可信度 | 强大的内部和外部效度 |

## 高级协议集成

### 为复杂项目组合研究方案

为了满足复杂的研究需求，方案可以按顺序组合或嵌套：

```
Prompt: I'm leading a major research initiative to understand the future of remote work and its implications for organizational design, technology infrastructure, and employee well-being. We need to analyze current trends, anticipate future developments, synthesize cross-disciplinary insights, and develop strategic recommendations for organizations adapting to distributed work models.

Protocol:
/research.integrated{
    components=[
        /research.literature{
            intent="Establish current state of knowledge on remote work",
            input={
                research_topic="Remote work impacts across organizational, technological, and human dimensions",
                key_questions=[
                    "What are the established impacts of remote work on productivity, collaboration, and innovation?",
                    "How have organizations successfully adapted structures and processes for distributed work?",
                    "What technologies have proven most effective for supporting remote work?"
                ],
                scope_boundaries={
                    timeframe: "Focus on last 5 years with acceleration during pandemic",
                    inclusion: "Academic research, industry studies, organizational case studies",
                    exclusion: "Speculative or non-evidence-based commentary"
                }
            }
            // Process and output details
        },
        /research.foresight{
            intent="Anticipate future remote work developments",
            input={
                domain="Future of work with focus on remote/hybrid models",
                time_horizon="5-10 years (2025-2035)",
                focal_areas=[
                    "Technology evolution and adoption",
                    "Organizational structure and process transformation",
                    "Workforce expectations and needs",
                    "Regulatory and policy environment"
                ],
                key_uncertainties=[
                    "Extent of remote work normalization across industries",
                    "Impact of emerging technologies on virtual collaboration",
                    "Evolution of management and leadership approaches",
                    "Geographic redistribution of talent"
                ]
            }
            // Process and output details
        },
        /research.synthesize{
            intent="Integrate insights across disciplines",
            input={
                synthesis_goal="Develop comprehensive framework for remote work adaptation",
                knowledge_domains=[
                    {domain: "Organizational Psychology", elements: ["Team dynamics", "Culture formation", "Well-being factors"]},
                    {domain: "Management Science", elements: ["Coordination mechanisms", "Performance management", "Organizational design"]},
                    {domain: "Technology Studies", elements: ["Collaboration tools", "Digital infrastructure", "Human-computer interaction"]},
                    {domain: "Workplace Strategy", elements: ["Physical-digital integration", "Space utilization", "Experience design"]}
                ]
            }
            // Process and output details
        }
    ],
    integration_framework={
        sequence="Literature review → Foresight analysis → Cross-disciplinary synthesis",
        connection_points="Each phase builds on previous findings with explicit linkages",
        knowledge_building="Progressive development from current state to future possibilities to integrated framework"
    }
}
```

### 协议适配指南

1. **添加专门的流程步骤**：
   ```
   /research.analyze{
       ...
       process=[
           ...,
           /specialized{action="Industry-specific analytical techniques"}
       ]
   }
   ```

2. **扩展输入参数**：
   ```
   /research.literature{
       ...
       input={
           ...,
           methodological_filter="Focus on empirical studies with n>100"
       }
   }
   ```

3. **增强输出规格**：
   ```
   /research.expert{
       ...
       output={
           ...,
           training_framework="Knowledge structured for educational transfer"
       }
   }
   ```

## 研究方案中的场动力学

对于高级研究过程，结合场动力学来塑造知识空间：

```
Prompt: I'm conducting research into emerging business models for decentralized autonomous organizations (DAOs) and want to ensure I explore both conventional and radical perspectives while maintaining analytical rigor. I'd like to use field dynamics to create a research space that balances established business theory with innovative concepts from the web3 ecosystem.

Protocol:
/research.literature{
    ...
    field_dynamics={
        attractors: [
            "business model innovation", 
            "governance mechanisms", 
            "value creation and capture"
        ],
        boundaries: {
            firm: ["unsubstantiated claims", "purely ideological arguments"],
            permeable: ["emerging concepts without extensive validation", "cross-disciplinary frameworks"]
        },
        resonance: ["organizational adaptation", "distributed decision-making"],
        residue: {
            target: "tension between centralized efficiency and decentralized resilience",
            persistence: "HIGH"
        }
    },
    ...
}
```

## 研究方案库管理

当您开发研究方案集合时，组织它们对于重用和改进变得至关重要。

### 组织架构

创建个人研究方案库：

```markdown
# Research Protocol Library

## By Research Phase
- [Literature Review v2.1](#literature-review)
- [Research Design v1.3](#research-design)
- [Expert Consultation v2.0](#expert-consultation)

## By Research Approach
- [Quantitative Research](#quantitative-research)
- [Qualitative Research](#qualitative-research)
- [Mixed Methods](#mixed-methods)

## Protocol Definitions

### Literature Review
```
/research.literature.v2.1{
    完整的协议定义
}
```

### Research Design
```
/research.design.v1.3{
    完整的协议定义
}
```
```

## 研究方案开发过程

创建自己的研究方案遵循以下开发路径：

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│       RESEARCH PROTOCOL DEVELOPMENT CYCLE           │
│                                                     │
│  1. IDENTIFY NEED                                   │
│     • Recognize recurring research pattern          │
│     • Identify friction points in research process  │
│     • Define methodological requirements            │
│                                                     │
│  2. DESIGN STRUCTURE                                │
│     • Define research process components            │
│     • Outline key methodological stages             │
│     • Determine required input parameters           │
│                                                     │
│  3. PROTOTYPE & TEST                                │
│     • Create minimal viable protocol                │
│     • Test with realistic research questions        │
│     • Document effectiveness and limitations        │
│                                                     │
│  4. REFINE & OPTIMIZE                               │
│     • Enhance based on test results                 │
│     • Optimize for research quality and efficiency  │
│     • Improve adaptability across contexts          │
│                                                     │
│  5. SHARE & ITERATE                                 │
│     • Create usage guidelines                       │
│     • Define quality metrics                        │
│     • Evolve based on diverse applications          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 平衡严谨性和创造力

研究方案提供了结构，但又不妨碍发现。请考虑以下平衡原则：

1. **开放的方法**：建立方法的严谨性，同时对意外发现保持开放态度
2. **使用探索构建：**创建包括发散调查的结构化流程
3. **精确且适应性**强：开发能够适应新出现的见解的精确方法
4. **高效而彻底**：构建高效的工作流程，保持全面覆盖

成功的研究方案会创建框架，在确保质量的同时支持发现。

## 结论：知识发现的演变

研究方案将通常混乱的调查过程转变为结构化、可靠的洞察途径，而不会牺牲发现和创造力的基本要素。通过为研究过程提供明确的架构，它们实现了更系统、更高效和高质量的知识发展。

在构建研究方案库时，请记住以下原则：

1. **从关键问题开始**：关注最能从结构中受益的研究挑战
2. **平衡严谨性和发现**性：在不限制探索的情况下创建足够的方法结构
3. **根据结果进行迭代**：根据研究结果优化方案
4. **适应上下文**：修改特定域和问题的协议
5. **内置质量**：在多个阶段整合验证和关键评估

凭借本指南中的这些原则和研究方案，您有能力将不可预测的研究过程转化为可靠、严格的调查，从而始终如一地产生有价值的见解。

**反思性问题**：这些研究方案如何不仅改变您的调查过程，而且改变您对知识发现质量的理解？

---

> *“研究不仅仅是寻找答案，而是以更好的方式提出更好的问题。”*

---

## 附录：快速参考

### 协议基本结构

```
/research.type{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```

### 常见流程作

- `/analyze`： 系统地检查信息
- `/synthesize`：将信息整合成连贯的整体
- `/evaluate`：根据特定标准进行评估
- `/map`：创建域的结构化表示
- `/explore`： 调查可能性或因素
- `/validate`：验证质量、准确性或适当性
- `/contextualize`：考虑相关的背景或情况

### Field Dynamics 快速设置

```
field_dynamics={
    attractors: ["knowledge focus", "methodological approach"],
    boundaries: {
        firm: ["excluded approaches", "out-of-scope elements"],
        permeable: ["adjacent considerations", "emerging concepts"]
    },
    resonance: ["conceptual frameworks", "explanatory models"],
    residue: {
        target: "key tension or insight",
        persistence: "MEDIUM"
    }
}
```

### 研究实验方案选择指南

| 需要 | 推荐方案 |
|------|----------------------|
| 了解现有知识 | `/research.literature` |
| 从信息中提取洞察 | `/research.analyze` |
| 探索未来发展 | `/research.foresight` |
| 了解复杂问题 | `/research.problem` |
| 比较多个选项 | `/research.compare` |
| 整合不同的知识 | `/research.synthesize` |
| 提取专业知识 | `/research.expert` |
| 开发研究方法 | `/research.design` |
