# 会话协议

> *“你的沟通质量决定了你的结果质量。”*
>
> **— 彼得·德鲁克**

## 会话协议简介

对话协议是结构化模板，用于指导您与 AI 系统的交互。他们将不可预测的、曲折的对话转化为高效、有目的的交流，并取得一致的结果。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            CONVERSATION PROTOCOL BENEFITS           │
│                                                     │
│  • Consistent outcomes across interactions          │
│  • Clear expectations for both human and AI         │
│  • Efficient use of context window                  │
│  • Reduced cognitive load for humans                │
│  • Trackable progress through complex discussions   │
│  • Portable templates across different AI systems   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

本指南为常见场景提供了实用的即用型对话协议，以及实施指南和性能指标。每个协议都遵循我们的 NOCODE 原则：导航、编排、控制、优化、部署和发展。

## 如何使用本指南

1. ** 从以下类别中**确定您的对话目标
2. **复制最符合您需求的**协议模板
3. ** 使用您的特定信息**自定义占位符
4. **在对话开始时**粘贴完整的协议
5. **监控指标** 以评估有效性
6. ** 根据结果**进行迭代和优化

**苏格拉底问题**：目前 AI 系统最让您感到沮丧的对话类型是什么？结构化方法的哪些好处最大？

---

## 1. 信息提取协议

### 目的
从非结构化内容或知识域中提取特定的结构化信息。

### 适用情形
- 分析文档或内容
- 收集特定数据点
- 从非结构化文本创建结构化数据集
- 从复杂的来源中提取关键点

### 协议模板

```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[PASTE_CONTENT_OR_DESCRIBE_DOMAIN]",
        target_structure={
            categories: ["[CATEGORY_1]", "[CATEGORY_2]", "[CATEGORY_3]"],
            format: "[FORMAT: table/list/JSON/etc.]",
            level_of_detail: "[brief/moderate/comprehensive]"
        },
        special_focus="[ANY_SPECIFIC_ASPECTS_TO_EMPHASIZE]"
    },
    process=[
        /analyze{action="Scan content for relevant information"},
        /categorize{action="Organize information into specified categories"},
        /structure{action="Format according to target structure"},
        /verify{action="Check completeness and accuracy"},
        /summarize{action="Provide overview of extracted information"}
    ],
    output={
        extracted_information="[Structured information according to specifications]",
        coverage_assessment="[Evaluation of information completeness]",
        confidence_metrics="[Reliability indicators for extracted information]"
    }
}

I'd like you to extract information from the content I've provided following this protocol. Please acknowledge and proceed with the extraction.
```

### 实施指南

1. **内容规格**：
   - 对于文档分析：粘贴全文或上传文档
   - 对于知识提取：清楚地描述领域（例如，“关于可再生能源技术的信息”）

2. **目标结构定义**：
   - 类别：定义 3-7 个特定类别（例如，“成本”、“收益”、“限制”）
   - 格式：指定最有用的输出格式（表格、列表、JSON 等）
   - 详细程度：根据您的需求选择（简要用于概述，全面用于深入分析）

3. **特别关注**：
   - 突出值得特别关注的任何特定方面
   - 可以包括时间范围、地理重点或特定的子主题

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 类别覆盖率 | 包含实质性信息的类别的百分比 | 100% |
| 信息密度 | 每个类别的相关数据点 | 最少 3-5 人 |
| 结构完整性 | 遵守请求的格式 | 100% |
| 置信度分数 | AI 对信息可靠性的评估 | >80% |

### 示例应用程序

```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[Research paper on climate change mitigation strategies]",
        target_structure={
            categories: ["Technology Solutions", "Policy Approaches", "Economic Impacts", "Implementation Challenges", "Success Metrics"],
            format: "markdown table with categories as rows",
            level_of_detail: "moderate"
        },
        special_focus="Solutions applicable to urban environments with limited resources"
    },
    process=[...],
    output={...}
}
```

---

## 2. 结构化辩论协议

### 目的
通过平衡、深思熟虑的分析，探索对复杂或有争议主题的多种观点。

### 适用情形
- 评估竞争方法或解决方案
- 了解有争议的话题
- 使用多种因素做出复杂的决策
- 测试论点和反论点的强度

### 协议模板

```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="[TOPIC_OR_QUESTION]",
        perspectives=["[PERSPECTIVE_1]", "[PERSPECTIVE_2]", "[PERSPECTIVE_3_OPTIONAL]"],
        evaluation_criteria=["[CRITERION_1]", "[CRITERION_2]", "[CRITERION_3]"],
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /establish{action="Define key terms and establish shared foundations"},
        /present{action="Present each perspective with strongest arguments"},
        /challenge{action="Identify weaknesses in each perspective"},
        /evaluate{action="Assess each perspective against criteria"},
        /synthesize{action="Identify potential integrations or resolutions"},
        /conclude{action="Summarize key insights and implications"}
    ],
    output={
        perspective_analysis="[Structured analysis of each perspective]",
        comparative_evaluation="[Side-by-side assessment using criteria]",
        synthesis_insights="[Potential integrations or novel approaches]",
        key_takeaways="[Most important insights from the debate]"
    }
}

I'd like to explore this topic through a structured debate using the perspectives and criteria I've provided. Please acknowledge and proceed with the debate.
```

### 实施指南

1. **主题定义**：
   - 构图为明确的问题或陈述
   - 确保范围可管理但具有实质性

2. **透视选择**：
   - 包括 2-3 个不同的观点（越多越笨拙）
   - 选择在方法或价值观上真正不同的观点
   - 可以包括约定俗成的与非约定俗成的、理论与实践的等等。

3. **评价标准**：
   - 选择 3-5 项相关标准进行评估
   - 包括实际和原则性考虑因素的组合
   - 示例：成本效益、道德影响、实施可行性

4. **约束**：
   - 指定对范围的任何限制
   - 请注意应保持不变的任何假设

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 钢人 | 每个视角的参数强度 | 最好的案例 |
| 平衡 | 不同视角的同等深度和慈善 | <10% 变化 |
| 申请准则 | 全面应用所有标准 | 100% 覆盖率 |
| 集成质量 | 通过综合实现增值 | 发现新的见解 |

### 示例应用程序

```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="Should cities prioritize public transit or autonomous vehicles for future mobility?",
        perspectives=["Public Transit Focus", "Autonomous Vehicle Priority", "Hybrid Approach"],
        evaluation_criteria=["Environmental Impact", "Social Equity", "Economic Efficiency", "Implementation Timeline"],
        constraints="Focus on mid-sized urban areas in developed economies"
    },
    process=[...],
    output={...}
}
```

---

## 3. 渐进式反馈协议

### 目的
通过结构化的多阶段反馈迭代改进工作产品。

### 适用情形
- 完善书面内容的草稿
- 改进设计理念
- 增强问题解决方案
- 通过迭代开发想法

### 协议模板

```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[CONTENT_TO_IMPROVE]",
        improvement_focus=["[FOCUS_AREA_1]", "[FOCUS_AREA_2]", "[FOCUS_AREA_3]"],
        iteration_count="[NUMBER_OF_FEEDBACK_CYCLES]",
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /baseline{action="Establish strengths and weaknesses of current version"},
        /prioritize{action="Identify highest-impact improvement opportunities"},
        /iterate{
            action="For each focus area:",
            substeps=[
                /analyze{action="Identify specific improvement opportunities"},
                /suggest{action="Provide specific enhancement recommendations"},
                /implement{action="Apply recommended changes"},
                /review{action="Assess improvements and identify next steps"}
            ]
        },
        /synthesize{action="Integrate improvements across all focus areas"},
        /compare{action="Contrast final version with original baseline"}
    ],
    output={
        improved_work="[Enhanced version of original work]",
        improvement_summary="[Overview of changes and enhancements]",
        future_directions="[Recommendations for further development]",
        version_comparison="[Before/after analysis showing progress]"
    }
}

I'd like to improve this work through progressive feedback cycles. Please acknowledge and begin the feedback process.
```

### 实施指南

1. **工作产品规格**：
   - 提供完整的待改进工作
   - 对于较长的作品，请考虑指定部分以集中注意力

2. **改进重点领域**：
   - 定义 2-4 个具体方面进行增强
   - 写作示例：清晰度、结构、证据、说服力
   - 设计示例：可用性、美学、功能性、连贯性

3. **迭代计数**：
   - 指定要执行的反馈周期数（2-3 通常是最佳）
   - 对于复杂的工作，考虑在每个周期中关注不同的方面

4. **约束**：
   - 请注意应保持不变的所有元素
   - 指定要维护的任何样式或内容准则

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 改进 Delta | 相对于基线的可衡量增强 | 显著的积极变化 |
| 重点区域覆盖 | 关注所有指定的重点领域 | 100% 覆盖率 |
| 实施质量 | 应用反馈的彻底性 | 所有高优先级建议 |
| 相干 | 跨领域的改进整合 | 统一，而不是拼凑 |

### 示例应用程序

```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[Draft marketing email for new productivity software]",
        improvement_focus=["Persuasiveness", "Clarity", "Call-to-action effectiveness"],
        iteration_count="3",
        constraints="Must maintain professional tone and stay under 300 words"
    },
    process=[...],
    output={...}
}
```

---

## 4. 决策分析协议

### 目的
系统地分析选项并为复杂的决策提出建议。

### 适用情形
- 通过权衡评估多个选项
- 做出高风险决策
- 分解复杂的选择场景
- 为重复出现的选择创建决策框架

### 协议模板

```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="[DECISION_SITUATION_DESCRIPTION]",
        options=["[OPTION_1]", "[OPTION_2]", "[OPTION_3_OPTIONAL]"],
        criteria={
            "[CRITERION_1]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_2]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_3]": {"weight": [1-10], "description": "[DESCRIPTION]"}
        },
        constraints="[ANY_LIMITATIONS_OR_REQUIREMENTS]",
        decision_maker_profile="[RELEVANT_PREFERENCES_OR_CONTEXT]"
    },
    process=[
        /frame{action="Clarify decision context and goals"},
        /evaluate{
            action="For each option:",
            substeps=[
                /assess{action="Evaluate against each weighted criterion"},
                /identify{action="Determine key strengths and weaknesses"},
                /quantify{action="Assign scores based on criteria performance"}
            ]
        },
        /compare{action="Conduct comparative analysis across options"},
        /analyze{action="Examine sensitivity to assumption changes"},
        /recommend{action="Provide structured recommendation with rationale"}
    ],
    output={
        option_analysis="[Detailed assessment of each option]",
        comparative_matrix="[Side-by-side comparison using criteria]",
        recommendation="[Primary recommendation with rationale]",
        sensitivity_notes="[How recommendation might change with different assumptions]",
        implementation_considerations="[Key factors for executing the decision]"
    }
}

I'd like to analyze this decision using the options and criteria I've provided. Please acknowledge and proceed with the analysis.
```

### 实施指南

1. **决策上下文**：
   - 描述需要决策的情况
   - 包括相关的背景和约束
   - 明确要做出的具体决定

2. **选项定义**：
   - 列出所有可行的替代方案（通常为 2-5 个）
   - 提供足够的细节以进行有意义的比较
   - 确保选项真正不同

3. **标准规范**：
   - 定义 3-7 个评估标准
   - 分配权重以反映相对重要性（1-10 分制）
   - 包括描述以确保应用程序一致

4. **决策者简介**：
   - 包括相关的偏好、风险承受能力、价值观
   - 记下任何特定的优先级或约束
   - 提及时间线或资源限制

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 标准覆盖率 | 全面应用所有标准 | 100% 覆盖率 |
| 分析深度 | 对每个选项的实质性评估 | 不同选项的深度相当 |
| 定量质量 | 有意义的评分和理由 | 所有分数的明确理由 |
| 建议清晰度 | 带有理由的明确指导 | 具体、可作的建议 |

### 示例应用程序

```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="Selecting a technology stack for a new e-commerce platform",
        options=["MERN Stack (MongoDB, Express, React, Node.js)", "Python/Django with PostgreSQL and React", "Ruby on Rails with React and PostgreSQL"],
        criteria={
            "Development Speed": {"weight": 8, "description": "How quickly can we build and iterate"},
            "Scalability": {"weight": 9, "description": "Ability to handle growing user base and traffic"},
            "Maintenance Complexity": {"weight": 7, "description": "Ease of ongoing maintenance and updates"},
            "Talent Availability": {"weight": 6, "description": "Ease of finding developers"}
        },
        constraints="Must be able to integrate with existing payment processing system",
        decision_maker_profile="Mid-sized company with limited in-house development team, moderate technical debt aversion, timeline of 6 months to launch"
    },
    process=[...],
    output={...}
}
```

---

## 5. 对齐协议

### 目的
确保相互理解并建立共同的目标、术语和方法。

### 适用情形
- 开始复杂的项目
- 建立协作框架
- 明确期望和可交付成果
- 在问题定义和成功标准上保持一致

### 协议模板

```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="[TOPIC_OR_PROJECT_DESCRIPTION]",
        key_terms=["[TERM_1]", "[TERM_2]", "[TERM_3_OPTIONAL]"],
        goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]",
        success_criteria="[HOW_SUCCESS_WILL_BE_MEASURED]"
    },
    process=[
        /define{action="Establish clear definitions for key terms"},
        /clarify{action="Ensure mutual understanding of goals and success criteria"},
        /explore{action="Identify potential misalignments or ambiguities"},
        /resolve{action="Address and clarify any identified misalignments"},
        /confirm{action="Establish explicitly shared understanding"},
        /document{action="Record aligned definitions, goals, and criteria"}
    ],
    output={
        term_definitions="[Explicit definitions of key terms]",
        goal_clarifications="[Detailed understanding of each goal]",
        boundary_conditions="[Clear articulation of constraints and limitations]",
        success_metrics="[Specific, measurable indicators of success]",
        alignment_summary="[Confirmation of mutual understanding]"
    }
}

I'd like to establish alignment on this topic using the terms, goals, and criteria I've provided. Please acknowledge and proceed with the alignment process.
```

### 实施指南

1. **主题规范**：
   - 明确定义对齐主题
   - 对于项目，请包括 scope 和 general purpose
   - 对于概念，确定域和重要性

2. **关键术语选择**：
   - 确定 3-7 个需要明确定义的术语
   - 关注可能产生歧义的术语
   - 包含需要澄清的特定领域术语

3. **目标表达**：
   - 列出 2-5 个具体目标
   - 确保目标足够具体，以便可作
   - 在相关时包括过程目标和结果目标

4. **成功标准**：
   - 定义如何衡量成就
   - 包括定性和定量指标
   - 指定时间范围（如果适用）

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 定义 清晰度 | 术语定义的精度和有用性 | 明确的作定义 |
| 目标特异性 | 目标的具体性和可作性 | 具体、可衡量、可实现 |
| 边界清晰度 | 约束定义的精度 | 清除限制参数 |
| 对齐确认 | 相互理解的程度 | 明确确认共同理解 |

### 示例应用程序

```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="Development of a customer feedback analysis system",
        key_terms=["Customer Sentiment", "Actionable Insight", "Implementation Priority", "Success Metric"],
        goals=["Create automated sentiment analysis", "Identify top customer pain points", "Develop prioritization framework for addressing feedback"],
        constraints="Must work with existing CRM system and respect customer privacy regulations",
        success_criteria="System should identify 90% of actionable feedback and reduce manual analysis time by 70%"
    },
    process=[...],
    output={...}
}
```

---

## 6. 问题定义协议

### 目的
精确定义和构建问题，以确保有效的解决方案开发。

### 适用情形
- 当面临复杂或模棱两可的问题时
- 开始解决方案开发之前
- 当利益相关者对问题有不同理解时
- 重新构建看似棘手的问题

### 协议模板

```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="[CURRENT_PROBLEM_DESCRIPTION]",
        context="[RELEVANT_BACKGROUND_INFORMATION]",
        stakeholders=["[STAKEHOLDER_1]", "[STAKEHOLDER_2]", "[STAKEHOLDER_3_OPTIONAL]"],
        attempted_solutions="[PREVIOUS_APPROACHES_IF_ANY]",
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]"
    },
    process=[
        /analyze{action="Examine initial problem statement for clarity and accuracy"},
        /deconstruct{action="Break down problem into components and dimensions"},
        /reframe{action="Consider alternative problem framings and perspectives"},
        /validate{action="Test problem definition against stakeholder needs"},
        /synthesize{action="Develop comprehensive problem definition"},
        /scope{action="Establish clear boundaries and success criteria"}
    ],
    output={
        refined_problem_statement="[Clear, precise problem definition]",
        root_causes="[Identified underlying factors]",
        success_criteria="[How a successful solution will be recognized]",
        constraints_and_boundaries="[Explicit limitations and scope]",
        reframing_insights="[Alternative perspectives that provide new approaches]",
        solution_directions="[Potential solution paths based on problem definition]"
    }
}

I'd like to clearly define this problem using the information I've provided. Please acknowledge and proceed with the problem definition process.
```

### 实施指南

1. **初始问题陈述**：
   - 陈述当前理解的问题
   - 包括症状和明显的挑战
   - 请注意当前理解中嵌入的任何假设

2. **上下文规定**：
   - 提供相关的背景信息
   - 包括组织、历史或技术背景
   - 注意任何最近的更改或发展

3. **利益相关者识别**：
   - 列出受问题影响或对问题感兴趣的主要参与方
   - 包括他们的观点和优先事项（如果知道）
   - 注意任何利益相关方利益冲突

4. **尝试的解决方案**：
   - 描述以前的方法及其结果
   - 注意特定的限制或失败
   - 包括部分成功和学习

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 清晰 | 问题定义的精确性和可理解性 | 明确、简洁的陈述 |
| 根本原因深度 | 识别潜在因素 | 超越症状，走向根本原因 |
| 利益相关者验证 | 与利益相关者的观点保持一致 | 解决所有关键利益相关者的问题 |
| 可作性 | 定义如何直接支持解决方案开发 | 明确的解决方案路径 |

### 示例应用程序

```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="Customer churn rate has increased by 15% over the past quarter",
        context="SaaS business with subscription model, recent UI redesign, and price increase of 10%",
        stakeholders=["Product Team", "Customer Success Team", "Executive Leadership", "Customers"],
        attempted_solutions="Implemented win-back campaigns and exit surveys with limited success",
        constraints="Solutions must work within existing technology stack and maintain current pricing strategy"
    },
    process=[...],
    output={...}
}
```

---

## 7. 学习促进协议

### 目的
构建学习过程以实现有效的知识获取和技能发展。

### 适用情形
- 学习新科目或技能时
- 向他人教授复杂的主题
- 创建教育材料
- 开发学习路径或课程

### 协议模板

```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="[TOPIC_OR_SKILL_TO_LEARN]",
        current_knowledge="[EXISTING_KNOWLEDGE_LEVEL]",
        learning_goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        learning_style_preferences="[PREFERRED_LEARNING_APPROACHES]",
        time_constraints="[AVAILABLE_TIME_AND_SCHEDULE]"
    },
    process=[
        /assess{action="Evaluate current knowledge and identify gaps"},
        /structure{action="Organize subject into logical learning sequence"},
        /scaffold{action="Build progressive framework from fundamentals to advanced concepts"},
        /contextualize{action="Connect abstract concepts to real applications"},
        /reinforce{action="Design practice activities and knowledge checks"},
        /adapt{action="Tailor approach based on progress and feedback"}
    ],
    output={
        learning_path="[Structured sequence of topics and skills]",
        key_concepts="[Fundamental ideas and principles to master]",
        learning_resources="[Recommended materials and sources]",
        practice_activities="[Exercises to reinforce learning]",
        progress_indicators="[How to measure learning advancement]",
        next_steps="[Guidance for continuing development]"
    }
}

I'd like to structure a learning experience for this subject based on the information I've provided. Please acknowledge and proceed with developing the learning facilitation.
```

### 实施指南

1. **主题规格**：
   - 明确定义要学习的主题或技能
   - 包括特定的重点子领域（如果适用）
   - 记下任何感兴趣的特定应用程序或上下文

2. **当前知识评估**：
   - 诚实地评估现有的熟悉度和能力
   - 注意具体的优势或劣势领域
   - 确定需要解决的任何误解

3. **学习目标定义**：
   - 指定 2-5 个具体的学习成果
   - 包括知识和应用程序目标
   - 为可用时间设定适当的雄心水平

4. **学习风格首选项**：
   - 注意首选方法（视觉、动手、理论等）
   - 指定任何特别有效的过去学习经历
   - 确定要避免的任何方法

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| Sequencing Logic | 概念的适当进展 | 遵守明确的依赖项 |
| 参与级别 | 与学习偏好保持一致 | 包括多种模式 |
| 执业质量 | 强化活动的有效性 | 主动学习机会 |
| 目标对齐 | 活动与既定目标之间的联系 | 实现目标的直接途径 |

### 示例应用程序

```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="Data visualization with Python (matplotlib and seaborn)",
        current_knowledge="Intermediate Python programming, basic statistics, no visualization experience",
        learning_goals=["Create publication-quality visualizations", "Develop interactive dashboards", "Implement automated visualization pipelines"],
        learning_style_preferences="Hands-on projects with practical applications, visual examples, iterative building",
        time_constraints="10 hours per week for 4 weeks"
    },
    process=[...],
    output={...}
}
```

---

## 8. 情景规划协议

### 目的
探索可能的未来并为不确定的环境制定稳健的策略。

### 适用情形
- 不确定环境中的战略规划
- 风险评估和应急计划
- 创新和面向未来的努力
- 具有长期影响的决策

### 协议模板

```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="[CENTRAL_STRATEGIC_QUESTION]",
        time_horizon="[PLANNING_TIMEFRAME]",
        key_uncertainties=["[UNCERTAINTY_1]", "[UNCERTAINTY_2]", "[UNCERTAINTY_3_OPTIONAL]"],
        driving_forces=["[FORCE_1]", "[FORCE_2]", "[FORCE_3_OPTIONAL]"],
        current_situation="[RELEVANT_CONTEXT_AND_STARTING_POINT]"
    },
    process=[
        /identify{action="Define key factors and driving forces"},
        /analyze{action="Assess impact and uncertainty of factors"},
        /construct{
            action="Develop 3-4 distinct, plausible scenarios",
            substeps=[
                /name{action="Create memorable scenario title"},
                /narrate{action="Describe scenario evolution and key events"},
                /detail{action="Explore implications for stakeholders"}
            ]
        },
        /identify{action="Extract strategic insights across scenarios"},
        /develop{action="Create robust strategies and early indicators"}
    ],
    output={
        scenarios=[
            {name="[SCENARIO_1_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_2_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_3_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"}
        ],
        robust_strategies="[APPROACHES_EFFECTIVE_ACROSS_SCENARIOS]",
        early_indicators="[SIGNS_INDICATING_SCENARIO_EMERGENCE]",
        key_uncertainties="[CRITICAL_FACTORS_TO_MONITOR]",
        strategic_recommendations="[IMMEDIATE_AND_LONG-TERM_ACTIONS]"
    }
}

I'd like to develop scenario plans around this focal question using the information I've provided. Please acknowledge and proceed with the scenario planning process.
```

### 实施指南

1. **焦点问题定义**：
   - 明确构建中心战略问题
   - 确保适当的范围和相关性
   - 关注决策需求

2. **时间范围选择**：
   - 选择合适的时间范围（通常为 3-10 年）
   - 在可预见的未来和有意义的变化之间取得平衡
   - 考虑行业特定的时序因素

3. **关键不确定性识别**：
   - 选择 2-4 个影响较大的关键不确定性
   - 关注真正不确定的因素（非预先确定的）
   - 包括多种类型（技术、社会、经济等）

4. **驱动力分析**：
   - 确定影响环境的主要趋势和因素
   - 包括外力和内力
   - 考虑 STEEP 因素（社会、技术、经济、环境、政治）

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 情景合理性 | 逻辑连贯性和可信度 | 没有神奇的想法或矛盾 |
| 情景独特性 | 场景之间有意义的差异 | 清晰、对比鲜明的未来 |
| 战略效用 | 从场景中获得的可作见解 | 对决策的具体影响 |
| 指标质量 | 早期预警信号的有用性 | 可观察的领先指标 |

### 示例应用程序

```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="How should our retail business adapt to changing consumer behavior and technology over the next decade?",
        time_horizon="10 years (2025-2035)",
        key_uncertainties=["Pace and nature of AI/automation adoption", "Consumer preferences for physical vs. digital experiences", "Regulatory environment for data and privacy"],
        driving_forces=["Aging demographics in core markets", "Climate change impacts on supply chains", "Increasing economic inequality", "Metaverse and virtual reality development"],
        current_situation="Mid-sized retail chain with 60% revenue from physical stores, growing e-commerce presence, limited data analytics capabilities"
    },
    process=[...],
    output={...}
}
```

---

## 高级协议集成

### 组合协议以进行复杂交互

对于复杂的需求，协议可以按顺序组合或嵌套：

```
/sequence{
    steps=[
        /problem.define{...},
        /debate.structured{...},
        /decision.analyze{...}
    ]
}
```

### 协议适配指南

1. **添加专门的流程步骤**：
   ```
   /extract.information{
       ...
       process=[
           ...,
           /specialize{action="Domain-specific analysis step"}
       ]
   }
   ```

2. **扩展输入参数**：
   ```
   /learning.facilitate{
       ...
       input={
           ...,
           accessibility_needs="[SPECIFIC_ACCESSIBILITY_REQUIREMENTS]"
       }
   }
   ```

3. **增强输出规格**：
   ```
   /scenario.plan{
       ...
       output={
           ...,
           visual_timeline="[GRAPHICAL_REPRESENTATION_OF_SCENARIOS]"
       }
   }
   ```

## 性能优化提示

### Token 效率

1. **确定输入元素的优先级**：
   - 仅包含基本上下文
   - 对列表使用项目符号而不是叙述
   - 尽可能引用外部信息

2. **流程简化**：
   - 对于更简单的任务，减少流程步骤
   - 在适当时合并相关步骤
   - 删除不增加价值的子步骤

3. **输出焦点**：
   - 仅指定所需的输出元素
   - 请求适当的详细程度
   - 使用结构化格式提高效率

### 方案选择的心智模型

1. **花园模型**：
   - 哪种方案最能培养我需要的想法？
   - 需要什么照料和修剪？
   - 如何确保可持续增长？

2. **河流模型**：
   - 信息流的来源是什么？
   - 我希望对话流向何处？
   - 哪些障碍可能会改变流程？

3. **预算模型**：
   - 我为这次互动准备的代币预算是多少？
   - 哪些投资会产生最高回报？
   - 如何最大限度地减少浪费？

## 持续改进

### 协议细化过程

1. **捕获结果**：
   - 记录协议输出
   - 注意任何偏差或挑战
   - 在整个交互过程中跟踪 AI 行为

2. **评估性能**：
   - 与指定指标进行比较
   - 确定优势和劣势
   - 注意意想不到的好处或限制

3. **优化元素**：
   - 调整输入参数以提高清晰度和完整性
   - 根据观察到的有效性修改流程步骤
   - 更新输出规格以更好地满足需求

4. **测试迭代**：
   - 将优化协议应用于类似场景
   - 比较不同迭代的性能
   - 记录渐进式改进

### 协议版本控制系统

要跟踪协议演变，请使用简单的版本控制表示法：

```
/protocol.name.v1.2{...}
```

哪里：
- 第一个数字 （1）：主要版本（结构更改）
- 第二个数字 （2）：次要版本（参数或流程优化）

包括每个版本的更改说明：

```
/extract.information.v1.2{
    meta={
        version_history=[
            {version="1.0", date="2025-02-10", changes="Initial release"},
            {version="1.1", date="2025-03-15", changes="Added confidence metrics to output"},
            {version="1.2", date="2025-04-22", changes="Enhanced special_focus parameter"}
        ]
    },
    ...
}
```

## 对话协议中的场动态

> *“你的田地的质量决定了它里面出现的东西的性质。”*

对话协议创建语义场，以微妙但强大的方式塑造交互。了解场动力学可以帮助您设计更有效的方案。

### Field Dynamics 关键概念

1. **吸引子**：对话自然而然地倾向于的稳定模式
   - 每个协议都创建特定的吸引子盆地
   - 精心设计的方案可维持所需的吸引子

2. **边界**：定义对话空间的限制
   - 清晰的边界可防止漂移并保持焦点
   - 可渗透边界允许有益的勘探

3. **共鸣**：某些主题或模式的放大
   - 协议可以产生增强某些品质的共振场
   - 有意共鸣提高了连贯性和深度

4. **残余**：延续的持续效应
   - 有效的方案可留下生产残留物
   - 符号残差为未来的交互奠定了基础

### 应用场动力学

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            FIELD DYNAMICS ENHANCEMENT               │
│                                                     │
│  Add to any protocol:                               │
│                                                     │
│  field_dynamics={                                   │
│    attractors: ["[PRIMARY_ATTRACTOR]", "[SECONDARY]"],│
│    boundaries: {                                    │
│      firm: ["[FIRM_BOUNDARY]"],                     │
│      permeable: ["[PERMEABLE_BOUNDARY]"]            │
│    },                                               │
│    resonance: ["[RESONANCE_PATTERN]"],              │
│    residue: {                                       │
│      target: "[DESIRED_SYMBOLIC_RESIDUE]",          │
│      persistence: "[HIGH|MEDIUM|LOW]"               │
│    }                                                │
│  }                                                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**应用示例**：

```
/debate.structured{
    ...
    field_dynamics={
        attractors: ["evidence-based reasoning", "charitable interpretation"],
        boundaries: {
            firm: ["personal attacks", "logical fallacies"],
            permeable: ["creative analogies", "interdisciplinary connections"]
        },
        resonance: ["intellectual curiosity", "nuanced understanding"],
        residue: {
            target: "multiple valid perspectives can coexist",
            persistence: "HIGH"
        }
    },
    ...
}
```

## 协议库管理

在开发协议集合时，组织它们对于重用和改进变得至关重要。

### 个人方案库模板

创建个人库 Markdown 文件：

```markdown
# Personal Protocol Library

## Conversation Protocols

### Daily Use
- [Extract Information v1.2](#extract-information)
- [Structured Debate v2.0](#structured-debate)

### Special Purpose
- [Scenario Planning v1.0](#scenario-planning)
- [Problem Definition v1.3](#problem-definition)

## Protocol Definitions

### Extract Information
```
/extract.information.v1.2{
    完整的协议定义
}
```

### Structured Debate
```
/debate.structured.v2.0{
    完整的协议定义
}
```
```

### 与笔记系统集成

协议可以与流行的笔记和知识管理系统集成：

1. **黑曜石**：
   - 创建专用协议文件夹
   - 使用模板插件快速插入
   - 将实验方案链接到相关说明

2. **概念**：
   - 创建协议数据库
   - 包括元数据，如用例、有效性评级
   - 使用模板快速添加到页面

3. **漫游研究**：
   - 使用块引用创建协议块
   - 针对不同使用案例的标记协议
   - 构建包含实验方案的工作流程模板

## 协议开发过程

创建自己的协议遵循结构化路径：

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            PROTOCOL DEVELOPMENT CYCLE               │
│                                                     │
│  1. IDENTIFY NEED                                   │
│     • Recognize recurring conversation pattern      │
│     • Identify frustrations or inefficiencies       │
│     • Define desired outcomes                       │
│                                                     │
│  2. DESIGN STRUCTURE                                │
│     • Define core components (input, process, output)│
│     • Outline key process steps                     │
│     • Determine required parameters                 │
│                                                     │
│  3. PROTOTYPE & TEST                                │
│     • Create minimal viable protocol                │
│     • Test with various AI systems                  │
│     • Document performance                          │
│                                                     │
│  4. REFINE & OPTIMIZE                               │
│     • Enhance based on test results                 │
│     • Optimize for token efficiency                 │
│     • Improve clarity and usability                 │
│                                                     │
│  5. DOCUMENT & SHARE                                │
│     • Create usage guidelines                       │
│     • Define performance metrics                    │
│     • Share with community                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 协议设计工作表

使用此工作表开发新方案：

```
## Protocol Design Worksheet

### 1. Basic Information
- Protocol Name: _______________
- Purpose: _______________
- Use Cases: _______________

### 2. Core Components
- Input Parameters:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Process Steps:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Output Elements:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________

### 3. Field Dynamics
- Primary Attractors: _______________
- Firm Boundaries: _______________
- Desired Resonance: _______________
- Target Residue: _______________

### 4. Implementation Notes
- Token Efficiency Considerations: _______________
- Integration With Other Protocols: _______________
- Version History Plan: _______________

### 5. Evaluation Plan
- Success Metrics: _______________
- Testing Approach: _______________
- Refinement Criteria: _______________
```

## 结论：对话协议的未来

对话协议代表了人机交互的根本转变。通过明确的协议构建对话，我们从不可预测的临时交流转变为一致、高效和有目的的协作。

在构建协议库时，请记住以下原则：

1. **从简单开始**：从满足常见需求的基本方案开始
2. **持续迭代**：根据实际使用情况进行优化
3. **共享和协作**：与他人交换协议
4. **在字段中思考**：考虑您正在创建的对话字段
5. **优先考虑清晰度**：清晰的结构带来明确的结果

借助本指南中的这些原则和协议模板，您可以很好地将 AI 对话从不可预测的交流转变为可靠、高效的协作。

**反思性问题**：这些协议不仅会如何改变您与 AI 的交互，还会改变您对有效沟通的一般理解？

---

> *“一次好的对话和一次精彩的对话之间的区别不在于运气，而在于建筑。”*

---

## 附录：快速参考

### 协议基本结构

```
/protocol.name{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```

### 常见流程作

- `/analyze`： 系统地检查信息
- `/synthesize`：将元素组合成连贯的整体
- `/evaluate`：根据标准进行评估
- `/prioritize`：确定相对重要性
- `/structure`：有逻辑地组织信息
- `/verify`：确认准确性或有效性
- `/explore`：研究可能性
- `/refine`：通过迭代进行改进

### Field Dynamics 快速设置

```
field_dynamics={
    attractors: ["focus", "clarity"],
    boundaries: {
        firm: ["off-topic", "vagueness"],
        permeable: ["relevant examples", "useful analogies"]
    },
    resonance: ["understanding", "insight"],
    residue: {
        target: "actionable knowledge",
        persistence: "MEDIUM"
    }
}
```

### 实验方案选择指南

| 需要 | 推荐方案 |
|------|----------------------|
| 提取特定信息 | `/extract.information` |
| 探索多个视角 | `/debate.structured` |
| 通过反馈改进工作 | `/feedback.progressive` |
| 做出复杂的决策 | `/decision.analyze` |
| 建立共识 | `/align.mutual` |
| 明确定义问题 | `/problem.define` |
| 构建学习体验 | `/learning.facilitate` |
| 探索可能的未来 | `/scenario.plan` |
