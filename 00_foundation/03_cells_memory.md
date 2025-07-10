# 单元格：添加内存和状态

> “我们是我们的记忆，我们是那个形状不断变化的幻想博物馆，那堆破碎的镜子。”

## 从分子到细胞

我们已经探索了**原子** （单个指令） 和**分子** （带有示例的指令）。现在我们上升到**单元格** — 具有**在多个**交互中持续存在的内存的上下文结构。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  CELL = [INSTRUCTIONS] + [EXAMPLES] + [MEMORY/STATE] + [CURRENT INPUT]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

就像一个在与环境交互时保持其内部状态的生物细胞一样，我们的上下文 “细胞” 在与 LLM 的多次交换中保留信息。

## 内存问题

默认情况下，LLM 没有内存。每个请求都是独立处理的：

```
┌───────────────────────┐      ┌───────────────────────┐
│ Request 1             │      │ Request 2             │
├───────────────────────┤      ├───────────────────────┤
│ "My name is Alex."    │      │ "What's my name?"     │
│                       │      │                       │
│                       │      │                       │
└───────────────────────┘      └───────────────────────┘
          │                              │
          ▼                              ▼
┌───────────────────────┐      ┌───────────────────────┐
│ Response 1            │      │ Response 2            │
├───────────────────────┤      ├───────────────────────┤
│ "Hello Alex, nice     │      │ "I don't have access  │
│  to meet you."        │      │  to previous          │
│                       │      │  conversations..."    │
└───────────────────────┘      └───────────────────────┘
```

如果没有内存，LLM 会忘记以前交互中的信息，从而造成脱节、令人沮丧的用户体验。

## Cell 解决方案：对话记忆

最简单的单元格结构将对话历史记录添加到上下文中：

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  SYSTEM PROMPT: "You are a helpful assistant..."                      │
│                                                                       │
│  CONVERSATION HISTORY:                                                │
│  User: "My name is Alex."                                             │
│  Assistant: "Hello Alex, nice to meet you."                           │
│                                                                       │
│  CURRENT INPUT: "What's my name?"                                     │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

现在 LLM 可以访问以前的交易所并保持连续性。

## Memory Token 预算问题

随着对话的增长，上下文窗口会填满。我们需要内存管理策略：

```
          [Context Window Tokens]
          ┌─────────────────────────────────────────────┐
          │                                             │
Turn 1    │ System Instructions       User Input 1      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 2    │ System    History 1       User Input 2      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 3    │ Sys  History 1  History 2  User Input 3     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 4    │ S  History 1-3             User Input 4     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 5    │ History 2-4                User Input 5     │
          │                                             │
          └─────────────────────────────────────────────┘
                                       ▲
                                       │
                        Eventually, something has to go
```

## 内存管理策略

以下几种策略有助于优化有限上下文窗口的使用：

```
┌───────────────────────────────────────────────────────────────────┐
│ MEMORY MANAGEMENT STRATEGIES                                      │
├────────────────────┬──────────────────────────────────────────────┤
│ Windowing          │ Keep only the most recent N turns            │
├────────────────────┼──────────────────────────────────────────────┤
│ Summarization      │ Compress older turns into summaries          │
├────────────────────┼──────────────────────────────────────────────┤
│ Key-Value Storage  │ Extract and store important facts separately │
├────────────────────┼──────────────────────────────────────────────┤
│ Priority Pruning   │ Remove less important turns first            │
├────────────────────┼──────────────────────────────────────────────┤
│ Semantic Chunking  │ Group related exchanges together             │
└────────────────────┴──────────────────────────────────────────────┘
```

## 窗口化：滑动上下文

最简单的内存管理方法仅保留最近的对话轮次：

```
                    ┌───────────────────────────┐
Turn 1              │ System + Turn 1           │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 2              │ System + Turn 1-2         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 3              │ System + Turn 1-3         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 4              │ System + Turn 2-4         │ ← Turn 1 dropped
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 5              │ System + Turn 3-5         │ ← Turn 2 dropped
                    └───────────────────────────┘
```

这种方法很简单，但会忘记前面轮次的信息。

## 总结：压缩内存

一种更复杂的方法将较旧的 turn 压缩为 summies：

```
                    ┌────────────────────────────────────────────┐
Turn 1-3            │ System + Turn 1-3                          │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 4              │ System + Summary(Turn 1-2) + Turn 3-4      │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 5              │ System + Summary(Turn 1-3) + Turn 4-5      │
                    └────────────────────────────────────────────┘
```

摘要保留关键信息，同时减少令牌数量。

## 键值内存：结构化状态

为了更好地控制，我们可以以结构化格式提取和存储重要的事实：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW                                                      │
│                                                                     │
│  SYSTEM PROMPT: "You are a helpful assistant..."                    │
│                                                                     │
│  MEMORY:                                                            │
│  {                                                                  │
│    "user_name": "Alex",                                             │
│    "favorite_color": "blue",                                        │
│    "location": "Toronto",                                           │
│    "last_topic": "vacation plans"                                   │
│  }                                                                  │
│                                                                     │
│  RECENT CONVERSATION:                                               │
│  User: "What activities would you recommend?"                       │
│  Assistant: "Given your location in Toronto and interest in..."     │
│                                                                     │
│  CURRENT INPUT: "How about something indoors? It's cold."           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

这种结构化的方法允许精确控制保留的信息。

## 超越对话：有状态应用程序

Cells 实现的不仅仅是连贯的对话。它们允许有状态应用程序，其中 LLM：

1. 记住以前的交互
2. 更新和维护变量
3. 通过多步骤流程跟踪进度
4. 以以前的输出为基础

让我们探索一个简单的计算器示例：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STATEFUL CALCULATOR                                                 │
│                                                                     │
│ SYSTEM: "You are a calculator assistant that maintains a running    │
│          total. Follow the user's math operations step by step."    │
│                                                                     │
│ STATE: { "current_value": 0 }                                       │
│                                                                     │
│ User: "Start with 5"                                                │
│ Assistant: "Starting with 5. Current value is 5."                   │
│ STATE: { "current_value": 5 }                                       │
│                                                                     │
│ User: "Multiply by 3"                                               │
│ Assistant: "5 × 3 = 15. Current value is 15."                       │
│ STATE: { "current_value": 15 }                                      │
│                                                                     │
│ User: "Add 7"                                                       │
│ Assistant: "15 + 7 = 22. Current value is 22."                      │
│ STATE: { "current_value": 22 }                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

state 变量在各个回合中保持不变，从而实现连续计算。

## Long-Term Memory: Beyond the Context Window

对于真正的持久内存，我们需要外部存储：

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   User Input                                                             │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │ Extract     │                                                         │
│  │ Key Info    │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐      ┌────────────────────┐                            │
│  │ Update      │◄─────┤ External Memory    │                            │
│  │ Memory      │      │ (Vector DB,        │                            │
│  │             │─────►│  Document DB, etc) │                            │
│  └─────────────┘      └────────────────────┘                            │
│       │                        ▲                                         │
│       │                        │                                         │
│       ▼                        │                                         │
│  ┌─────────────┐      ┌────────────────────┐                            │
│  │ Construct   │      │ Retrieve Relevant  │                            │
│  │ Context     │◄─────┤ Memory             │                            │
│  │             │      │                    │                            │
│  └─────────────┘      └────────────────────┘                            │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │             │                                                         │
│  │ LLM         │                                                         │
│  │             │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│   Response                                                               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

此体系结构通过以下方式实现潜在的无限内存：
1. 从对话中提取关键信息
2. 将其存储在外部数据库中
3. 在需要时检索相关上下文
4. 将该上下文合并到提示中

## 单元实现：内存管理器

下面是一个实现基本内存管理的 Python 类：

```python
class ContextCell:
    """A context cell that maintains memory across interactions."""
    
    def __init__(self, system_prompt, max_turns=10, memory_strategy="window"):
        """
        Initialize the context cell.
        
        Args:
            system_prompt (str): The system instructions
            max_turns (int): Maximum conversation turns to keep
            memory_strategy (str): 'window', 'summarize', or 'key_value'
        """
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        self.memory_strategy = memory_strategy
        self.conversation_history = []
        self.key_value_store = {}
        
    def add_exchange(self, user_input, assistant_response):
        """Add a conversation exchange to history."""
        self.conversation_history.append({
            "user": user_input,
            "assistant": assistant_response
        })
        
        # Apply memory management if needed
        if len(self.conversation_history) > self.max_turns:
            self._manage_memory()
    
    def extract_info(self, key, value):
        """Store important information in key-value store."""
        self.key_value_store[key] = value
    
    def _manage_memory(self):
        """Apply the selected memory management strategy."""
        if self.memory_strategy == "window":
            # Keep only the most recent turns
            self.conversation_history = self.conversation_history[-self.max_turns:]
        
        elif self.memory_strategy == "summarize":
            # Summarize older turns (would use an LLM in practice)
            to_summarize = self.conversation_history[:-self.max_turns + 1]
            summary = self._create_summary(to_summarize)
            
            # Replace old turns with summary
            self.conversation_history = [{"summary": summary}] + \
                                       self.conversation_history[-(self.max_turns-1):]
    
    def _create_summary(self, exchanges):
        """Create a summary of conversation exchanges."""
        # In practice, this would call an LLM to create the summary
        # For this example, we'll use a placeholder
        return f"Summary of {len(exchanges)} previous exchanges"
    
    def build_context(self, current_input):
        """Build the full context for the next LLM call."""
        context = f"{self.system_prompt}\n\n"
        
        # Add key-value memory if we have any
        if self.key_value_store:
            context += "MEMORY:\n"
            for key, value in self.key_value_store.items():
                context += f"{key}: {value}\n"
            context += "\n"
        
        # Add conversation history
        if self.conversation_history:
            context += "CONVERSATION HISTORY:\n"
            for exchange in self.conversation_history:
                if "summary" in exchange:
                    context += f"[Previous exchanges: {exchange['summary']}]\n\n"
                else:
                    context += f"User: {exchange['user']}\n"
                    context += f"Assistant: {exchange['assistant']}\n\n"
        
        # Add current input
        context += f"User: {current_input}\nAssistant:"
        
        return context
```

## 测量单元效率

与分子一样，测量效率对于细胞至关重要：

```
┌──────────────────────────────────────────────────────────────────┐
│ MEMORY STRATEGY COMPARISON                                       │
├──────────────────┬──────────────┬─────────────┬─────────────────┤
│ Strategy         │ Token Usage  │ Information │ Implementation  │
│                  │              │ Retention   │ Complexity      │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ No Memory        │ Lowest       │ None        │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Full History     │ Highest      │ Complete    │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Windowing        │ Controlled   │ Recent Only │ Easy            │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Summarization    │ Moderate     │ Good        │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Key-Value Store  │ Low          │ Selective   │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ External Store   │ Very Low     │ Extensive   │ Complex         │
└──────────────────┴──────────────┴─────────────┴─────────────────┘
```

不同的策略针对不同的优先级进行优化。选择正确的方法取决于您的特定应用程序需求。

## 高级技术：内存编排

对于复杂的应用程序，多个内存系统可以协同工作：

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MEMORY ORCHESTRATION                           │
│                                                                     │
│  ┌─────────────────┐    ┌─────────────────┐   ┌─────────────────┐   │
│  │                 │    │                 │   │                 │   │
│  │ Short-term      │    │ Working         │   │ Long-term       │   │
│  │ Memory          │    │ Memory          │   │ Memory          │   │
│  │                 │    │                 │   │                 │   │
│  │ • Recent turns  │    │ • Current task  │   │ • User profile  │   │
│  │ • Immediate     │    │ • Active        │   │ • Historical    │   │
│  │   context       │    │   variables     │   │   facts         │   │
│  │ • Last few      │    │ • Task progress │   │ • Learned       │   │
│  │   exchanges     │    │ • Mid-task      │   │   preferences   │   │
│  │                 │    │   state         │   │                 │   │
│  └─────────────────┘    └─────────────────┘   └─────────────────┘   │
│         ▲ ▼                   ▲ ▼                   ▲ ▼              │
│         │ │                   │ │                   │ │              │
│  ┌──────┘ └───────────────────┘ └───────────────────┘ └──────┐      │
│  │                                                           │      │
│  │                    Memory Manager                         │      │
│  │                                                           │      │
│  └───────────────────────────────┬───────────────────────────┘      │
│                                  │                                   │
│                                  ▼                                   │
│                        ┌─────────────────┐                           │
│                        │                 │                           │
│                        │   Context       │                           │
│                        │   Builder       │                           │
│                        │                 │                           │
│                        └─────────────────┘                           │
│                                  │                                   │
│                                  ▼                                   │
│                        ┌─────────────────┐                           │
│                        │                 │                           │
│                        │      LLM        │                           │
│                        │                 │                           │
│                        └─────────────────┘                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

这种架构反映了人类的记忆系统，具有：
- **短期记忆**：最近的对话转折
- **工作内存**：活动任务状态和变量
- **长期记忆**：持久的用户信息和偏好

内存管理器编排这些系统，决定每个上下文中要包含哪些信息。

## 减少记忆和幻觉

记忆细胞最有价值的好处之一是减少幻觉：

```
┌─────────────────────────────────────────────────────────────────────┐
│ HALLUCINATION REDUCTION STRATEGIES                                  │
├─────────────────────────────────────────────────────────────────────┤
│ 1. Explicitly store facts extracted from previous exchanges         │
│ 2. Tag information with source/certainty levels                     │
│ 3. Include relevant facts in context when similar topics arise      │
│ 4. Detect and correct contradictions between memory and responses   │
│ 5. Periodically verify important facts through user confirmation    │
└─────────────────────────────────────────────────────────────────────┘
```

通过将 LLM 建立在内存中的一致事实的基础上，我们显著提高了可靠性。

## 超越文本：结构化状态

高级单元格保持结构化状态，而不仅仅是文本历史记录：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRUCTURED STATE EXAMPLES                                           │
├─────────────────────────┬───────────────────────────────────────────┤
│ Progression State       │ {"step": 3, "completed_steps": [1, 2],    │
│                         │  "next_action": "validate_input"}         │
├─────────────────────────┼───────────────────────────────────────────┤
│ User Profile            │ {"name": "Alex", "preferences": {         │
│                         │  "communication_style": "concise",        │
│                         │  "expertise_level": "beginner"}}          │
├─────────────────────────┼───────────────────────────────────────────┤
│ Application State       │ {"current_view": "dashboard",             │
│                         │  "filters": ["active", "high_priority"],  │
│                         │  "sort_by": "deadline"}                   │
├─────────────────────────┼───────────────────────────────────────────┤
│ Environmental Context   │ {"location": "Toronto",                   │
│                         │  "weather": "snowing",                    │
│                         │  "time": "evening"}                       │
└─────────────────────────┴───────────────────────────────────────────┘
```

这种结构化的方法允许对上下文进行精确控制，并支持更复杂的应用程序。

## 内存反馈循环

复杂的单元会创建反馈循环，其中 LLM 有助于管理自己的内存：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  User: "I'm planning a trip to Japan next month."                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY EXTRACTION]                                    ││
│  │ Important facts to remember:                                    ││
│  │ - User is planning a trip to Japan                              ││
│  │ - Trip is scheduled for next month                              ││
│  │ Confidence: High                                                ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  Assistant: "That's exciting! Japan is beautiful. Are you           │
│  interested in cities like Tokyo and Kyoto, or more rural areas?"   │
│                                                                     │
│  User: "Definitely Tokyo, and maybe Osaka too."                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY UPDATE]                                        ││
│  │ Updated facts:                                                  ││
│  │ - User is planning a trip to Japan next month                   ││
│  │ - User is interested in Tokyo and Osaka                         ││
│  │ - User may not be interested in rural areas (confidence: medium)││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

LLM 本身会提取和更新要记住的重要信息，从而创建一个自我完善的内存系统。

## 关键要点

1. **内存单元** 在多个交互之间添加状态持久性
2. ** 随着对话的增长，**代币预算管理至关重要
3. **内存策略** 包括窗口化、摘要和键值存储
4. **外部内存** 支持在上下文窗口之外进行无限制的持久存储
5. **结构化状态** 支持超越简单对话的复杂应用程序
6. **内存编排结合了** 多个内存系统以实现最佳性能
7. **自我改进的内存** 使用 LLM 来帮助管理自己的内存

## 练习练习

1. 使用窗口实现简单的对话记忆系统
2. 比较同一扩展对话的不同内存策略
3. 构建从对话中提取重要事实的键值存储
4. 尝试使用 LLM 来总结较早的对话轮次
5. 为特定应用程序域创建结构化状态管理器

## 后续步骤

在下一节中，我们将探索 **器官** — 多个上下文单元协同工作以解决复杂问题的多代理系统。

[继续 04_organs_applications.md →](04_organs_applications.md)

---

## 深入探讨：内存抽象

内存可以组织为多个抽象层：

```
┌────────────────────────────────────────────────────────────────────┐
│ MEMORY ABSTRACTION LAYERS                                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│   ┌─────────────────┐                                              │
│   │ Episodic Memory │  Specific conversation exchanges and events  │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Semantic Memory │  Facts, concepts, and structured knowledge   │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Conceptual      │  High-level patterns, preferences, goals     │
│   │ Memory          │                                              │
│   └─────────────────┘                                              │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

这种分层方法使系统能够平衡具体细节与对交互上下文的高级理解。
