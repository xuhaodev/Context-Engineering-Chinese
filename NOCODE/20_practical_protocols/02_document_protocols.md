# 记录协议

> *“写作就是思考。写得好就是想得清楚。这就是为什么它如此困难。*
>
> **— 大卫·麦卡洛**

## Document 协议简介

文档协议将混乱的内容创建过程转变为结构化、高效的工作流程，从而始终如一地产生高质量的结果。它们提供了一个架构框架，用于组织想法、管理信息和制作引人注目的内容，同时优化您与 AI 系统的交互。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            DOCUMENT PROTOCOL BENEFITS               │
│                                                     │
│  • Consistent document quality and structure        │
│  • Reduced cognitive overhead during creation       │
│  • Efficient collaboration between human and AI     │
│  • Clear progression from concept to completion     │
│  • Optimized token usage for complex documents      │
│  • Maintainable and evolvable content over time     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

本指南为常见内容创建方案提供了现成的文档协议，并提供了实施指南和性能指标。每个协议都遵循我们的 NOCODE 原则：导航、编排、控制、优化、部署和发展。

## 如何使用本指南

1. **选择与您的文档创建目标相匹配**的协议
2. **复制协议模板** 并自定义占位符
3. ** 在交互开始时向 AI 助手**提供协议
4. **遵循从初始概念到最终文档的**结构化流程
5. **监控指标** 以评估有效性
6. **迭代和完善** 您的实验方案以备将来使用

**Socratic Question**：您觉得创建哪些类型的文档最具挑战性？文档创建过程中的哪些方面消耗的时间和精力最多？

---

## 1. 结构化文章协议

**何时使用此协议：**
需要创建一篇全面、结构良好的文章来有效地传达复杂的信息？该协议指导您撰写具有清晰组织、平衡深度和引人入胜内容的文章——非常适合博客文章、教育内容、思想领导力文章或技术解释。

```
/document.article{
    intent="Create a comprehensive, well-structured article on a specific topic",
    input={
        topic="[ARTICLE_TOPIC]",
        target_audience="[PRIMARY_READERS_AND_THEIR_KNOWLEDGE_LEVEL]",
        key_points=["[POINT_1]", "[POINT_2]", "[POINT_3]", "[ADD_AS_NEEDED]"],
        tone="[DESIRED_TONE: academic/conversational/persuasive/etc.]",
        length="[APPROXIMATE_WORD_COUNT]",
        special_elements="[ANY_SPECIFIC_INCLUSIONS: examples/case studies/data/etc.]"
    },
    process=[
        /outline{
            action="Create detailed hierarchical structure",
            format="Outline with sections and subsections"
        },
        /develop{
            action="Expand outline into full content",
            sections=[
                /introduction{
                    elements=["hook", "context", "thesis", "roadmap"],
                    purpose="Engage reader and establish framework"
                },
                /body{
                    approach="Logical progression of ideas",
                    section_pattern=[
                        "key point statement",
                        "supporting evidence/explanation",
                        "illustrative examples",
                        "implications or applications"
                    ]
                },
                /conclusion{
                    elements=["summary", "broader context", "call to action/future directions"],
                    purpose="Reinforce key messages and provide closure"
                }
            ]
        },
        /enhance{
            elements=[
                "transitional phrases between sections",
                "varied sentence structure",
                "precise and engaging vocabulary",
                "rhetorical devices appropriate to tone"
            ]
        },
        /finalize{
            action="Review and refine complete article",
            checks=["clarity", "flow", "tone consistency", "evidence strength"]
        }
    ],
    output={
        final_article="Complete article with clear structure and engaging content",
        key_messages="Summary of central points made in the article",
        suggested_title="Recommended title and potential alternatives",
        outline_reference="Final structure for future reference"
    }
}

I'd like to create an article following this protocol with the information I've provided. Please acknowledge and begin with an outline.
```

### 实施指南

1. **主题定义**：
   - 具体而非笼统
   - 框架作为重点问题或陈述
   - 考虑广度 （覆盖范围） 和深度 （细节级别）

2. **受众规格**：
   - 定义人口统计、知识水平和兴趣
   - 考虑他们阅读此内容的动机
   - 确定他们从文章中寻求的价值

3. **关键点选择**：
   - 确定 3-7 个核心信息或论点
   - 确保点在逻辑上相互构建
   - 平衡覆盖的广度和有意义的深度

4. **色调设置**：
   - 将语气与受众和目的相匹配
   - 考虑适当的词汇和句子结构
   - 保持整个文档的一致性

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 结构完整性 | 逻辑组织和流程 | 清晰的层次结构，平滑过渡 |
| 内容深度 | 点开发的彻底性 | 对每个关键点进行实质性探索 |
| 互动分值 | 读者兴趣和留存率 | 引人注目的钩子和不同的节奏 |
| 消息清晰度 | 关键点的可理解性 | 明确无误的中心信息 |

### 示例应用程序

```
/document.article{
    intent="Create a comprehensive, well-structured article on a specific topic",
    input={
        topic="The impact of generative AI on content creation workflows",
        target_audience="Marketing professionals with basic AI knowledge but limited technical expertise",
        key_points=[
            "AI fundamentally changes content creation economics",
            "Human-AI collaboration requires new workflows and skills",
            "Quality control becomes more important than initial creation",
            "Ethical considerations should be built into new processes"
        ],
        tone="Informative yet conversational, forward-looking but practical",
        length="1200-1500 words",
        special_elements="Include practical examples, mini case studies, and actionable takeaways"
    },
    process=[...],
    output={...}
}
```

---

## 2. 技术文档协议

**何时使用此协议：**
创建需要清晰、准确和全面的技术文档？该协议构建了技术指南、API 文档、产品手册或流程文档的开发，重点关注可用性、技术准确性和适当的细节级别。

```
/document.technical{
    intent="Create precise, usable technical documentation",
    input={
        subject="[SYSTEM/PRODUCT/PROCESS_TO_DOCUMENT]",
        documentation_type="[GUIDE/REFERENCE/API_DOCS/MANUAL/etc.]",
        target_users="[PRIMARY_USERS_AND_THEIR_EXPERTISE_LEVEL]",
        key_components=["[COMPONENT_1]", "[COMPONENT_2]", "[COMPONENT_3]", "[ADD_AS_NEEDED]"],
        technical_depth="[BASIC/INTERMEDIATE/ADVANCED]",
        usage_context="[HOW_AND_WHERE_DOCUMENTATION_WILL_BE_USED]"
    },
    process=[
        /structure{
            action="Create logical documentation architecture",
            elements=[
                "overview section",
                "prerequisite information",
                "component-by-component details",
                "cross-references and relationships",
                "troubleshooting or FAQ section"
            ]
        },
        /develop{
            action="Construct technical content with appropriate detail",
            sections=[
                /overview{
                    elements=["purpose", "scope", "architecture", "key concepts"],
                    purpose="Provide context and high-level understanding"
                },
                /component_details{
                    for_each="key_component",
                    structure=[
                        "component purpose and context",
                        "technical specifications",
                        "usage instructions or examples",
                        "limitations and considerations"
                    ]
                },
                /cross_references{
                    action="Establish connections between components",
                    elements=["dependencies", "interactions", "workflows"]
                },
                /troubleshooting{
                    structure=["common issues", "diagnostic steps", "solutions"],
                    purpose="Enable self-service problem resolution"
                }
            ]
        },
        /enhance{
            elements=[
                "clear diagrams or visual aids",
                "code samples or configuration examples",
                "callouts for important information",
                "consistent terminology and definitions"
            ]
        },
        /finalize{
            action="Review and validate technical accuracy",
            checks=["correctness", "completeness", "usability", "accessibility"]
        }
    ],
    output={
        final_documentation="Complete technical documentation with appropriate structure and detail",
        terminology_glossary="Definitions of key technical terms",
        usage_examples="Practical examples demonstrating application",
        improvement_areas="Suggestions for future documentation enhancements"
    }
}

I'd like to create technical documentation following this protocol with the information I've provided. Please acknowledge and begin with a documentation structure.
```

### 实施指南

1. **主题定义**：
   - 明确定义范围和边界
   - 确定要记录的特定版本或迭代
   - 考虑系统架构和组件关系

2. **文档类型选择**：
   - 指南：流程分步说明
   - 参考：用于查找的综合信息
   - API 文档：接口规范和用法
   - 手册：完整的产品或系统作

3. **用户规格**：
   - 定义主要用户的技术专业知识水平
   - 考虑具有不同需求的二级用户组
   - 确定常见的使用场景和用户目标

4. **组件优先级：**
   - 列出主要功能区域或系统组件
   - 根据重要性和使用频率确定优先级
   - 考虑逻辑分组和关系

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 技术精度 | 所有信息的正确性 | 100% 准确率 |
| 完整性 | 覆盖所有必要的组件 | 无功能差距 |
| 可用性 | 易于查找和应用信息 | 只需 2-3 次点击/步骤即可访问信息 |
| 质量示例 | 示例的实用性和清晰度 | 直接适用于常见场景 |

### 示例应用程序

```
/document.technical{
    intent="Create precise, usable technical documentation",
    input={
        subject="RESTful API for customer data management system v2.1",
        documentation_type="API reference with usage guides",
        target_users="Backend developers with intermediate REST experience, some new to our specific implementation",
        key_components=[
            "Authentication and authorization",
            "Customer record endpoints",
            "Transaction history endpoints",
            "Batch operations",
            "Rate limiting and quotas"
        ],
        technical_depth="Intermediate with advanced sections",
        usage_context="Used during development implementation and for troubleshooting"
    },
    process=[...],
    output={...}
}
```

---

## 3. 执行简报协议

**何时使用此协议：**
需要向忙碌的决策者简明扼要地提供复杂的信息？该协议创建重点突出的执行摘要、简报或备忘录，在保持影响力和可作性的同时有效地提供重要信息。

```
/document.executive_brief{
    intent="Create a concise, impactful brief for decision-makers",
    input={
        topic="[BRIEF_SUBJECT]",
        key_points=["[POINT_1]", "[POINT_2]", "[POINT_3]", "[ADD_AS_NEEDED]"],
        decision_context="[DECISIONS_OR_ACTIONS_THIS_BRIEF_SUPPORTS]",
        audience="[SPECIFIC_DECISION_MAKERS_AND_THEIR_PRIORITIES]",
        data_elements="[KEY_DATA_POINTS_TO_INCLUDE]",
        length_constraint="[MAXIMUM_LENGTH_OR_TIME_TO_READ]"
    },
    process=[
        /prioritize{
            action="Identify and rank information by decision relevance",
            criteria=["impact on decisions", "urgency", "strategic alignment"]
        },
        /structure{
            action="Create executive-appropriate format",
            elements=[
                "headline summary (key message)",
                "context (minimal necessary background)",
                "insights (key findings and implications)",
                "recommendations (clear, actionable next steps)",
                "supporting evidence (selected high-impact data)"
            ]
        },
        /develop{
            action="Craft concise, precise content",
            approach=[
                "use executive vocabulary and tone",
                "emphasize insights over process",
                "focus on business implications",
                "maintain brevity without sacrificing clarity"
            ]
        },
        /enhance{
            elements=[
                "visual data presentations",
                "executive framing of issues",
                "clear decision pathways",
                "risk and opportunity assessments"
            ]
        },
        /finalize{
            action="Optimize for immediate comprehension",
            checks=["clarity", "actionability", "strategic alignment", "conciseness"]
        }
    ],
    output={
        executive_brief="Concise document optimized for decision-maker consumption",
        key_takeaways="Single-sentence core messages",
        recommended_actions="Prioritized action items",
        supporting_data="Selected high-impact evidence points"
    }
}

I'd like to create an executive brief following this protocol with the information I've provided. Please acknowledge and begin by prioritizing the key information.
```

### 实施指南

1. **主题框架**：
   - 在业务影响或战略相关性方面进行表达
   - 关注结果而不是过程
   - 用决策者的语言，而不是技术术语来构建框架

2. **决策上下文说明**：
   - 指定此简报将告知的确切决定
   - 注意决策的时间表
   - 确定影响决策的约束或注意事项

3. **受众分析**：
   - 定义特定角色和职责
   - 记下每个决策者的具体关注点或优先事项
   - 考虑预先存在的知识和偏好

4. **数据选择**：
   - 仅选择最具影响力的指标或调查结果
   - 关注前瞻性影响，而不是历史细节
   - 以业务术语（收入、成本、增长、风险）呈现数据

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 简洁 | 沟通效率 | 在目标时间内可读（通常为 3-5 分钟） |
| 执行官相关性 | 与决策者的优先事项保持一致 | 与战略关注点直接联系 |
| 可作性 | 明确后续步骤 | 明确的建议 |
| Impact Clarity | 重要性的显而易见性 | 明确的业务影响 |

### 示例应用程序

```
/document.executive_brief{
    intent="Create a concise, impactful brief for decision-makers",
    input={
        topic="Proposed expansion into Southeast Asian markets: Opportunity analysis and entry strategy",
        key_points=[
            "Thailand and Vietnam offer highest immediate ROI with 28% projected margins",
            "Phased entry strategy reduces capital requirements by 40% versus simultaneous launch",
            "Strategic partnership with LocalTech Inc. mitigates regulatory risks and accelerates market access",
            "Competitive landscape shows 12-18 month window before major competitors enter"
        ],
        decision_context="Board needs to approve $15M initial investment and partnership agreement at next meeting",
        audience="Board members with varied international experience, particularly concerned with risk management and capital efficiency",
        data_elements="Market size projections, competitor analysis, capital requirements by phase, risk assessment matrix",
        length_constraint="5-minute read maximum, one-page executive summary"
    },
    process=[...],
    output={...}
}
```

---

## 4. 教学内容协议

**何时使用此协议：**
创建旨在教授技能或程序的内容？该协议开发教育材料，重点是学习进展、知识保留和实际应用，非常适合教程、作指南、培训材料或教育内容。

```
/document.instructional{
    intent="Create effective learning-focused content",
    input={
        subject="[SKILL_OR_KNOWLEDGE_TO_TEACH]",
        learner_profile="[TARGET_LEARNERS_AND_THEIR_STARTING_POINT]",
        learning_objectives=["[OBJECTIVE_1]", "[OBJECTIVE_2]", "[OBJECTIVE_3]", "[ADD_AS_NEEDED]"],
        prerequisite_knowledge="[WHAT_LEARNERS_SHOULD_ALREADY_KNOW]",
        format="[TUTORIAL/GUIDE/COURSE/etc.]",
        engagement_approach="[HOW_TO_MAINTAIN_LEARNER_INTEREST]"
    },
    process=[
        /structure{
            action="Design learning progression",
            approach=[
                "sequence concepts from foundational to advanced",
                "chunk information into manageable sections",
                "incorporate scaffolding for complex concepts",
                "build in knowledge validation points"
            ]
        },
        /develop{
            action="Create instructional content with pedagogical focus",
            sections=[
                /introduction{
                    elements=["learning goals", "relevance to learner", "overview of progression"],
                    purpose="Establish motivation and context for learning"
                },
                /core_content{
                    for_each="learning_objective",
                    structure=[
                        "concept explanation",
                        "demonstration or example",
                        "guided practice opportunity",
                        "common pitfalls and solutions"
                    ]
                },
                /reinforcement{
                    elements=["summary", "practice exercises", "real-world applications"],
                    purpose="Consolidate and apply new knowledge"
                }
            ]
        },
        /enhance{
            elements=[
                "visual learning aids (diagrams, charts, etc.)",
                "varied examples for different learning styles",
                "analogies and metaphors for complex concepts",
                "checkpoints for knowledge validation"
            ]
        },
        /finalize{
            action="Optimize for learning effectiveness",
            checks=["clarity", "engagement", "knowledge building", "practical application"]
        }
    ],
    output={
        instructional_content="Complete learning-focused content with effective progression",
        quick_reference="Summary of key concepts for later review",
        practice_materials="Exercises or activities for skill development",
        instructor_notes="Guidance for teaching or facilitating (if applicable)"
    }
}

I'd like to create instructional content following this protocol with the information I've provided. Please acknowledge and begin by designing the learning progression.
```

### 实施指南

1. **主题定义**：
   - 定义要教授的特定技能或知识
   - 建立包含/排除内容的明确界限
   - 将复杂的主题分解为可教的组件

2. **学习者档案开发**：
   - 定义先前的知识和经验水平
   - 确定学习此主题的动机
   - 考虑潜在的挑战或误解

3. **学习目标表述**：
   - 编写具体、可衡量的目标
   - 使用表示掌握程度的动作动词
   - 确保逐步建立目标

4. **格式选择**：
   - 教程：特定任务的分步指南
   - 指南：应用程序的全面概述
   - 课程：结构化、多模块的学习体验
   - 参考：持续使用的井然有序的信息

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 概念清晰 | 解释的可理解性 | 可访问 Target 学习者个人资料 |
| 学习进度 | 知识的逻辑构建 | 从基础到精通的清晰路径 |
| 参与级别 | 保持学习者的兴趣 | 保持注意力的多种方法 |
| 应用程序支持 | 知识的实际应用 | 多种应用学习的机会 |

### 示例应用程序

```
/document.instructional{
    intent="Create effective learning-focused content",
    input={
        subject="Data visualization fundamentals with Tableau",
        learner_profile="Marketing professionals with basic data literacy but no visualization tool experience",
        learning_objectives=[
            "Connect to and prepare data sources for visualization",
            "Create five fundamental chart types for different analytical purposes",
            "Design interactive dashboards combining multiple visualizations",
            "Apply best practices for clarity and visual communication"
        ],
        prerequisite_knowledge="Basic understanding of data concepts (metrics, dimensions), comfort with spreadsheets",
        format="Hands-on tutorial with progressive exercises",
        engagement_approach="Real-world marketing data examples, progressive challenges, visual before/after comparisons"
    },
    process=[...],
    output={...}
}
```

---

## 5. 说服性文件协议

**何时使用此协议：**
需要影响决策、改变观点或激发行动？该协议开发有说服力的内容，以最大限度地提高影响并推动预期结果，非常适合提案、销售材料、宣传内容或变更管理沟通。

```
Prompt: I need to create a compelling business proposal to secure funding for our new SaaS platform. My audience is a panel of venture capitalists with technology backgrounds who are looking for innovative solutions with clear market potential. I need to persuade them to invest $2M in our first funding round. Please structure this as a persuasive document that addresses their likely concerns about market size, competition, and our execution capability.

Protocol:
/document.persuasive{
    intent="Create content designed to influence and drive action",
    input={
        proposition="Invest $2M in our SaaS platform's initial funding round",
        target_audience="Technology-focused venture capitalists seeking innovative solutions with market potential",
        desired_outcome="Secure $2M in funding with favorable terms",
        key_motivators=[
            "Potential for significant ROI (10x within 5 years)",
            "Unique technological advantage over competitors",
            "Clear path to market with established customer interest",
            "Experienced team with domain expertise"
        ],
        potential_objections=[
            "Market may be too niche or competitive",
            "Technology remains unproven at scale",
            "Execution team lacks previous exits"
        ],
        evidence_available="Market analysis, working prototype, LOIs from potential customers, team credentials, financial projections"
    },
    process=[
        /analyze{
            action="Assess audience and persuasion context",
            elements=[
                "current position analysis",
                "motivation and value mapping",
                "objection anticipation",
                "influence path planning"
            ]
        },
        /structure{
            action="Design persuasion architecture",
            approach=[
                "attention-grabbing opening",
                "establish relevance and credibility",
                "build logical and emotional case",
                "address objections proactively",
                "clear call to action"
            ]
        },
        /develop{
            action="Craft persuasive content with strategic intent",
            sections=[
                /opening{
                    elements=["hook", "relevance establishment", "thesis"],
                    purpose="Capture attention and interest"
                },
                /case_building{
                    structure=[
                        "logical argument progression",
                        "emotional appeal alignment",
                        "evidence presentation",
                        "benefit articulation"
                    ]
                },
                /objection_handling{
                    approach="Acknowledge, address, and reframe",
                    purpose="Neutralize resistance points"
                },
                /call_to_action{
                    elements=["specific request", "urgency creation", "next steps"],
                    purpose="Drive desired outcome"
                }
            ]
        },
        /enhance{
            elements=[
                "persuasive language patterns",
                "social proof integration",
                "visual persuasion elements",
                "risk mitigation framing"
            ]
        },
        /finalize{
            action="Optimize for persuasive impact",
            checks=["argument coherence", "emotional resonance", "objection coverage", "action clarity"]
        }
    ],
    output={
        persuasive_document="Complete persuasive content designed to drive action",
        key_arguments="Summary of most compelling points",
        objection_responses="Prepared answers to anticipated resistance",
        presentation_guidance="Recommendations for effective delivery"
    }
}
```

### 实施指南

1. **命题表述**：
   - 具体说明您的要求
   - 根据观众利益，而不仅仅是您的需求来构建框架
   - 使其具体且可作

2. **受众分析**：
   - 确定您主张的当前位置
   - 了解决策标准和优先级
   - 映射关系和影响动态

3. **动机识别**：
   - 研究驱动这些特定受众的因素
   - 根据相对重要性确定优先级
   - 尽可能从收益的角度出发，而不是避免损失

4. **异议预期**：
   - 列出所有可能的阻力点
   - 按潜在影响确定优先级
   - 准备循证回复

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 说服力 | 改变视角的有效性 | 明显转向预期结果 |
| 异议处理 | 彻底解决疑虑 | 消除所有主要反对意见 |
| 动机对齐 | 与受众驱动因素的连接 | 直接吸引关键激励因素 |
| 号召性用语清晰度 | 请求的作的特异性 | 明确的后续步骤 |

## 6. 政策和程序协议

**何时使用此协议：**
创建需要全面、一致和可作的组织治理文档？该协议以清晰和完整的方式制定政策、程序和标准，非常适合用于作指南、合规性文档或标准作程序。

```
Prompt: I need to create a comprehensive remote work policy for our organization following recent changes to our hybrid work model. This policy needs to clarify eligibility, expectations, security requirements, and performance measurement for remote employees. It should balance flexibility with accountability and ensure consistent application across departments.

Protocol:
/document.policy{
    intent="Create clear, comprehensive governance documents",
    input={
        policy_purpose="Define a comprehensive remote work policy for the organization",
        scope="All employees eligible for remote work arrangements",
        stakeholders=["Executive leadership", "Department managers", "HR", "IT", "Employees"],
        key_components=[
            "Eligibility criteria and approval process",
            "Schedule and availability requirements",
            "Equipment and workspace standards",
            "Security and confidentiality protocols",
            "Performance measurement and accountability",
            "Communication expectations"
        ],
        compliance_requirements="Data protection regulations, employment law, industry standards",
        organizational_context="Transitioning from office-first to hybrid work model"
    },
    process=[
        /structure{
            action="Establish policy architecture",
            elements=[
                "purpose and scope statement",
                "definitions of key terms",
                "policy statements by component",
                "roles and responsibilities",
                "procedures and workflows",
                "compliance and exceptions",
                "related documents and references"
            ]
        },
        /develop{
            action="Craft policy content with precision and clarity",
            sections=[
                /purpose_scope{
                    elements=["policy intent", "applicability", "authority"],
                    purpose="Establish boundaries and foundation"
                },
                /policy_statements{
                    for_each="key_component",
                    structure=[
                        "clear directive statements",
                        "rationale or context",
                        "guidelines for application",
                        "examples or clarifications"
                    ]
                },
                /procedures{
                    elements=["step-by-step processes", "decision workflows", "templates"],
                    purpose="Enable consistent implementation"
                },
                /roles_responsibilities{
                    approach="Map accountabilities to roles",
                    purpose="Establish ownership and authority"
                },
                /governance{
                    elements=["review cycle", "exception handling", "compliance monitoring"],
                    purpose="Ensure ongoing policy effectiveness"
                }
            ]
        },
        /validate{
            action="Ensure policy effectiveness and compliance",
            checks=[
                "stakeholder alignment",
                "legal/regulatory compliance",
                "implementation feasibility",
                "clarity and accessibility",
                "edge case coverage"
            ]
        },
        /finalize{
            action="Optimize for usability and compliance",
            elements=[
                "consistent formatting and terminology",
                "navigational aids (TOC, indices)",
                "version control and approvals",
                "implementation guidance"
            ]
        }
    ],
    output={
        complete_policy="Comprehensive policy document with all components",
        implementation_guide="Guidance for rolling out the policy",
        compliance_checklist="Key requirements for monitoring adherence",
        communication_materials="Content for explaining policy to stakeholders"
    }
}
```

### 实施指南

1. **策略目的定义**：
   - 明确说明需要解决的问题或需要
   - 阐明预期的组织成果
   - 建立范围和边界

2. **利益相关者识别**：
   - 包括受政策影响或实施政策的所有各方
   - 考虑每个群体的观点和需求
   - 识别潜在的阻力点

3. **组件定义**：
   - 将策略分解为合乎逻辑、可管理的部分
   - 确保全面覆盖，无重叠
   - 根据重要性和影响确定优先级

4. **合规性映射**：
   - 确定所有相关法规和标准
   - 注意影响策略的特定要求
   - 考虑行业最佳实践

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 清晰 | 政策声明的可理解性 | 所有利益相关者均可访问 |
| 完整性 | 必要组件的覆盖范围 | 无明显差距 |
| 可实施性 | 易于将策略付诸实践 | 清晰可行的程序 |
| 合规 | 符合要求 | 完全遵守法规 |

## 7. 战略计划协议

**何时使用此协议：**
制定定义方向和方法的前瞻性文件？该协议创建战略计划、路线图或愿景文档，以有效地传达方向、优先事项和实施路径，非常适合组织战略、产品路线图或部门计划。

```
Prompt: I need to develop a three-year strategic plan for our marketing department that aligns with the company's global expansion goals. The plan should address our transition to digital-first marketing, build our capabilities in new markets, and establish measurement frameworks to demonstrate ROI. It needs to be ambitious yet achievable with our current team size and budget constraints.

Protocol:
/document.strategic_plan{
    intent="Create forward-looking strategic direction documents",
    input={
        planning_horizon="Three-year marketing department strategic plan",
        organizational_context="Company pursuing global expansion with digital-first approach",
        strategic_objectives=[
            "Transition to digital-first marketing approach",
            "Build marketing capabilities in new geographic markets",
            "Establish comprehensive measurement framework to demonstrate ROI",
            "Align marketing activities with global expansion goals"
        ],
        current_state="Traditional marketing mix with limited digital capabilities and primarily domestic focus",
        resource_constraints="Current team size and existing budget with moderate annual increases",
        success_measures="Market penetration in new regions, digital engagement metrics, marketing-attributed revenue"
    },
    process=[
        /analyze{
            action="Assess strategic context and requirements",
            elements=[
                "environmental analysis (market, competitors, trends)",
                "capability assessment (strengths, gaps, opportunities)",
                "stakeholder needs and expectations",
                "alignment with broader organizational strategy"
            ]
        },
        /structure{
            action="Design strategic framework",
            elements=[
                "vision and mission statements",
                "strategic pillars or themes",
                "objectives and key results (OKRs)",
                "phased implementation approach",
                "resource allocation framework"
            ]
        },
        /develop{
            action="Craft strategic content with appropriate detail",
            sections=[
                /executive_summary{
                    elements=["strategic direction", "key priorities", "expected outcomes"],
                    purpose="Provide quick understanding of strategic intent"
                },
                /strategic_framework{
                    elements=["vision", "mission", "values", "strategic pillars"],
                    purpose="Establish foundation and boundaries"
                },
                /objectives_strategies{
                    for_each="strategic_objective",
                    structure=[
                        "specific objective statement",
                        "rationale and alignment",
                        "key strategies and approaches",
                        "success metrics and targets"
                    ]
                },
                /implementation_roadmap{
                    elements=["phased approach", "key initiatives", "dependencies", "milestones"],
                    purpose="Provide actionable path forward"
                },
                /resource_plan{
                    elements=["budget requirements", "staffing needs", "capability development"],
                    purpose="Define required investments and allocations"
                },
                /governance_measurement{
                    elements=["review cadence", "key metrics", "adjustment mechanisms"],
                    purpose="Enable progress tracking and adaptation"
                }
            ]
        },
        /validate{
            action="Test strategic soundness and feasibility",
            checks=[
                "alignment with organizational strategy",
                "resource feasibility",
                "risk assessment",
                "stakeholder buy-in",
                "measurement validity"
            ]
        },
        /finalize{
            action="Optimize for inspiration and execution",
            elements=[
                "compelling narrative and vision",
                "clear accountability assignments",
                "visual strategy representations",
                "executive presentation materials"
            ]
        }
    ],
    output={
        strategic_plan="Comprehensive strategy document with execution roadmap",
        executive_presentation="Materials for leadership communication",
        implementation_framework="Detailed execution guidance",
        measurement_dashboard="Key metrics and tracking approach"
    }
}
```

### 实施指南

1. **规划范围定义**：
   - 为战略类型选择合适的时间框架
   - 考虑行业步伐和组织环境
   - 雄心壮志和可预测性之间的平衡

2. **组织环境评估**：
   - 记录当前的战略方向和优先事项
   - 注意相关的市场和竞争因素
   - 确定影响策略的主要趋势

3. **战略目标制定**：
   - 定义推动成功的 3-5 个主要目标
   - 确保目标具体但足够广泛
   - 验证与组织方向的一致性

4. **现状分析**：
   - 诚实地评估目前的能力和地位
   - 确定要利用的优势和要解决的差距
   - 建立明确的基线来衡量进度

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 战略清晰度 | 方向的可理解性 | 在各个层面上都有明确的前进道路 |
| 实施可行性 | 执行的实用性 | 现实的资源要求 |
| 测量框架 | 能够跟踪进度 | 具有目标的有意义的指标 |
| 鼓舞人心的品质 | 激励行动的能力 | 引人注目的愿景和叙述 |

## 8. 综合评估协议

**何时使用此协议：**
进行需要平衡考虑多个因素的全面分析？该协议创建全面客观的评估文件、评估或审查，非常适合绩效评估、情况分析、项目评估或产品评估。

```
Prompt: I need to conduct a comprehensive assessment of our recently completed software implementation project. We need to evaluate what went well, what challenges we faced, the final quality of the deliverables, and extract key lessons for future projects. This should be balanced and objective, acknowledging both successes and areas for improvement.

Protocol:
/document.assessment{
    intent="Create balanced, thorough evaluation documents",
    input={
        assessment_subject="Recently completed software implementation project",
        evaluation_dimensions=[
            "Project management effectiveness",
            "Deliverable quality and completeness",
            "Budget and timeline performance",
            "Stakeholder satisfaction",
            "Team performance and collaboration",
            "Risk management effectiveness"
        ],
        assessment_purpose="Post-project review to extract lessons and improve future implementations",
        data_sources="Project documentation, stakeholder interviews, quality metrics, budget reports",
        intended_audience="Project leadership, executive sponsors, implementation team",
        balance_requirement="Equal focus on successes and improvement opportunities"
    },
    process=[
        /structure{
            action="Design comprehensive assessment framework",
            elements=[
                "executive summary with balanced highlights",
                "assessment methodology and approach",
                "dimensional evaluations",
                "integrated findings and patterns",
                "recommendations and action items",
                "supporting evidence and data"
            ]
        },
        /gather{
            action="Collect and organize assessment inputs",
            approach=[
                "triangulate multiple data sources",
                "apply consistent evaluation criteria",
                "identify patterns and outliers",
                "maintain objectivity and evidence basis"
            ]
        },
        /analyze{
            action="Evaluate assessment dimensions with depth and balance",
            for_each="evaluation_dimension",
            structure=[
                /dimension_assessment{
                    elements=[
                        "objective description of findings",
                        "strengths identification",
                        "challenge or gap analysis",
                        "contributing factors exploration",
                        "evidence and examples"
                    ]
                },
                /rating_and_context{
                    elements=["quantitative/qualitative rating", "comparison to standards or expectations"],
                    purpose="Provide clear performance indication"
                }
            ]
        },
        /synthesize{
            action="Develop integrated insights and recommendations",
            elements=[
                "cross-dimensional patterns",
                "root cause identification",
                "specific, actionable recommendations",
                "prioritization framework",
                "implementation guidance"
            ]
        },
        /finalize{
            action="Optimize for objectivity and utility",
            checks=[
                "evidence strength",
                "balance and fairness",
                "actionability of recommendations",
                "clarity of presentation",
                "alignment with assessment purpose"
            ]
        }
    ],
    output={
        assessment_report="Comprehensive evaluation with balanced findings",
        executive_summary="Concise overview of key findings and recommendations",
        recommendation_roadmap="Prioritized improvement actions",
        lessons_learned="Key insights for future application"
    }
}
```

### 实施指南

1. **评估科目定义**：
   - 明确定义范围和边界
   - 指定要评估的时间段或版本
   - 请注意任何特殊的上下文因素

2. **尺寸选择**：
   - 选择 4-7 个重点方面进行评估
   - 确保尺寸涵盖所有关键因素
   - 平衡过程和结果维度

3. **目的澄清**：
   - 定义此评估将告知的具体决策
   - 确定如何使用调查结果
   - 考虑可作性的时间需求

4. **数据源识别**：
   - 列出所有可用的信息源
   - 包括定量和定性数据
   - 请注意任何重要的数据限制

### 性能指标

| 度量 | 描述 | 目标 |
|--------|-------------|--------|
| 客观性 | 平衡和循证分析 | 不受未经证实的判断 |
| 全面性 | 覆盖所有关键维度 | 无明显的盲点 |
| Insight 质量 | 研究结果的深度和有用性 | 揭示不明显的模式 |
| 可作性 | 建议的实用性 | 具体可行的改进路径 |

## 高级协议集成

### 为复杂项目组合文档协议

对于复杂的文档需求，协议可以组合或嵌套：

```
Prompt: I need to create a comprehensive business case for a major digital transformation initiative that includes both persuasive elements to secure executive approval and detailed strategic planning for implementation. It needs to convince our leadership team to approve a $5M investment while also providing a clear roadmap for executing the three-year program.

Protocol:
/document.integrated{
    components=[
        /document.persuasive{
            intent="Secure executive approval for digital transformation investment",
            input={
                proposition="Approve $5M investment for comprehensive digital transformation",
                target_audience="C-suite executives focused on growth and operational efficiency",
                desired_outcome="Full funding approval with executive sponsorship",
                key_motivators=[
                    "30% increase in operational efficiency",
                    "New digital revenue streams (15% growth projection)",
                    "Competitive differentiation in rapidly evolving market",
                    "Risk mitigation for digital disruption threats"
                ],
                potential_objections=[
                    "ROI timeline exceeds typical investment criteria",
                    "Significant change management challenges",
                    "Previous technology investments underperformed"
                ],
                evidence_available="Market analysis, competitor benchmarking, pilot project results, customer feedback"
            },
            // Process and output details
        },
        /document.strategic_plan{
            intent="Provide implementation roadmap for transformation program",
            input={
                planning_horizon="Three-year digital transformation program",
                organizational_context="Traditional company facing digital disruption pressures",
                strategic_objectives=[
                    "Modernize core technology infrastructure",
                    "Digitize customer-facing processes and touchpoints",
                    "Build data analytics capabilities and culture",
                    "Develop digital product innovation pipeline"
                ],
                current_state="Legacy systems, siloed data, traditional processes",
                resource_constraints="Limited digital talent, competing priorities",
                success_measures="Efficiency metrics, digital revenue, customer satisfaction"
            },
            // Process and output details
        }
    ],
    integration_framework={
        structure="Persuasive executive summary with strategic implementation details",
        alignment="Ensure consistent messaging and data across components",
        progression="Lead with persuasive case, transition to strategic execution"
    }
}
```

### 协议适配指南

1. **添加专门的流程步骤**：
   ```
   /document.technical{
       ...
       process=[
           ...,
           /specialized{action="Domain-specific technical validation"}
       ]
   }
   ```

2. **扩展输入参数**：
   ```
   /document.strategic_plan{
       ...
       input={
           ...,
           competitive_landscape="[DETAILED_COMPETITOR_ANALYSIS]"
       }
   }
   ```

3. **增强输出规格**：
   ```
   /document.assessment{
       ...
       output={
           ...,
           maturity_model="[CAPABILITY_MATURITY_FRAMEWORK]"
       }
   }
   ```

## 性能优化提示

### Token 效率

1. **内容优先级**：
   - 专注于影响最大的文档元素
   - 使用渐进式披露来获取详细信息
   - 在所有领域都倾向于关键领域的深度而不是广度

2. **流程简化**：
   - 对于更简单的文档，降低流程复杂性
   - 组合相关的开发步骤
   - 删除易于理解的格式的验证步骤

3. **输出焦点**：
   - 仅请求所需的文档组件
   - 将详细程度与实际使用要求相匹配
   - 使用结构化格式实现高效的信息呈现

### 文档协议的现场动力学

对于高级文档开发，请合并字段动态：

```
Prompt: I need to create a strategic vision document that will inspire our organization to embrace a significant transformation in how we approach customer experience. This document should establish powerful attractors around customer-centricity while allowing for adaptation as we implement the vision.

Protocol:
/document.strategic_plan{
    ...
    field_dynamics={
        attractors: [
            "customer-centric mindset",
            "continuous improvement culture",
            "data-driven decision making"
        ],
        boundaries: {
            firm: ["short-term financial focus", "departmental silos"],
            permeable: ["implementation approaches", "technology choices"]
        },
        resonance: ["empathy for customer needs", "innovation mindset"],
        residue: {
            target: "customer experience as everyone's responsibility",
            persistence: "HIGH"
        }
    },
    ...
}
```

## 文档协议库管理

随着文档协议集合的增长，组织它们对于重用和改进变得至关重要。

### 组织架构

创建个人文档协议库：

```markdown
# Document Protocol Library

## By Document Type
- [Strategic Plan v2.1](#strategic-plan)
- [Persuasive Proposal v1.3](#persuasive-proposal)
- [Technical Documentation v3.0](#technical-documentation)

## By Use Context
- [Executive Communication](#executive-communication)
- [Team Documentation](#team-documentation)
- [External Publishing](#external-publishing)

## Protocol Definitions

### Strategic Plan
```
/document.strategic_plan.v2.1{
    完整的协议定义
}
```

### Persuasive Proposal
```
/document.persuasive.v1.3{
    完整的协议定义
}
```
```

## 文档协议开发过程

创建自己的文档协议遵循以下开发路径：

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│         DOCUMENT PROTOCOL DEVELOPMENT CYCLE         │
│                                                     │
│  1. IDENTIFY NEED                                   │
│     • Recognize recurring document type             │
│     • Identify pain points in creation process      │
│     • Define quality standards and success criteria │
│                                                     │
│  2. DESIGN STRUCTURE                                │
│     • Define document components and architecture   │
│     • Outline development process steps             │
│     • Determine required input parameters           │
│                                                     │
│  3. PROTOTYPE & TEST                                │
│     • Create minimal viable protocol                │
│     • Test with realistic document needs            │
│     • Document performance and challenges           │
│                                                     │
│  4. REFINE & OPTIMIZE                               │
│     • Enhance based on test results                 │
│     • Optimize for efficiency and quality           │
│     • Improve usability and flexibility             │
│                                                     │
│  5. STANDARDIZE & SHARE                             │
│     • Create usage guidelines                       │
│     • Define performance metrics                    │
│     • Add to organizational protocol library        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 结论：文档创建的演变

文档协议代表了传统内容创建方法的范式转变。通过为文档开发提供明确的架构和流程，他们将不可预测的、费力的写作转变为结构化、可靠的内容制作。

在构建文档协议库时，请记住以下原则：

1. **从高价值文档开始**：专注于频繁创建或关键文档类型
2. **根据结果进行迭代**：根据实际使用结果优化协议
3. **共享和标准化**：创建组织标准以实现一致的质量
4. **系统思考**：考虑文档如何在更大的通信生态系统中协同工作
5. **平衡结构和创造力**：提供足够的结构以实现一致性，同时允许适当的灵活性

借助本指南中的这些原则和文档协议，您可以很好地将内容创建从不可预测的工作量密集型工作转变为可靠、高效地制作高质量文档。

**反思性问题**：这些文档协议如何改变您在组织内进行知识捕获和沟通的方法？

---

> *“写作的过程就是思考的过程。清晰的文件反映了清晰的思路，而清晰的协议创造了清晰的文件。*

---

## 附录：快速参考

### 协议基本结构

```
/document.type{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```

### 常见流程作

- `/structure`：定义文档架构
- `/develop`：按照结构创建内容
- `/analyze`：检查信息或上下文
- `/validate`：验证质量或准确性
- `/enhance`：添加可提高影响的元素
- `/finalize`：针对最终交付进行优化

### 文档实验方案选择指南

| 需要 | 推荐方案 |
|------|----------------------|
| 创建综合文章 | `/document.article` |
| 开发技术文档 | `/document.technical` |
| 撰写执行简报 | `/document.executive_brief` |
| 创建以学习为中心的内容 | `/document.instructional` |
| 制定有说服力的文档 | `/document.persuasive` |
| 创建策略或过程 | `/document.policy` |
| 制定战略计划 | `/document.strategic_plan` |
| 进行全面评估 | `/document.assessment` |
