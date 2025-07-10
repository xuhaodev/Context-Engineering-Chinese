# Few-shot 学习模板

## 总结
一个模板，用于通过示例教授 AI 系统，使它们能够学习模式并将其应用于新案例，而无需明确说明。

## 背景和应用
当您希望 AI 从示例中学习，而不是从明确的规则或指令中学习时，请使用此模板。小样本学习功能强大，因为它显示而不是讲述，使 AI 能够推断模式并将其应用于新情况。

此模板非常适合：
- 难以解释但易于演示的任务
- 基于模式的任务，其中示例比规则更好地传达模式
- 需要一致的格式或样式的情况
- 教授细微的判断或分类

## 模板结构

```
# Task: {{task_description}}

## Examples

### Example 1
Input: {{input_1}}
Output: {{output_1}}

### Example 2
Input: {{input_2}}
Output: {{output_2}}

### Example 3
Input: {{input_3}}
Output: {{output_3}}

## Your Turn
Input: {{new_input}}
Output:
```

## 参数

- `{{task_description}}`：要执行的任务的简要描述（例如，“对这些评论的情绪进行分类”）
- `{{input_X}}`：演示模式的示例输入（推荐 3-5 个示例）
- `{{output_X}}`：显示每个输入的预期响应的相应输出
- `{{new_input}}`：您希望 AI 使用它学习的模式处理的新案例

## 例子

### 示例 1：情绪分类

```
# Task: Classify the sentiment of customer feedback as positive, negative, or neutral

## Examples

### Example 1
Input: "The product arrived on time and works perfectly. Couldn't be happier with my purchase!"
Output: Positive

### Example 2
Input: "Delivery was quick but the product has several scratches on the surface."
Output: Neutral

### Example 3
Input: "Terrible customer service. Had to call three times and still haven't resolved my issue."
Output: Negative

## Your Turn
Input: "Package was delivered two days late, but the quality of the item exceeded my expectations."
Output:
```

### 示例 2：数据转换

```
# Task: Convert the given product information into a standardized JSON format

## Examples

### Example 1
Input: 
Product: Wireless Headphones
Brand: SoundCore
Price: $79.99
Features: Noise cancellation, 30-hour battery, Bluetooth 5.0

Output:
```json
{
  "product_name": "Wireless Headphones",
  "manufacturer": "SoundCore",
  "price_usd": 79.99,
  "specifications": [
    "Noise cancellation",
    "30-hour battery",
    "Bluetooth 5.0"
  ]
}
```

### 示例 2
输入：
产品名称：Smart Watch Pro
品牌： TechFit
会员价 $129.95
特点： 心率监测器， GPS追踪， 防水

输出：
```json
{
  "product_name": "Smart Watch Pro",
  "manufacturer": "TechFit",
  "price_usd": 129.95,
  "specifications": [
    "Heart rate monitor",
    "GPS tracking",
    "Water resistant"
  ]
}
```

## 该你了
输入：
产品： 便携式蓝牙音箱
厂商： AudioMax
会员价 $45.50
特点： 防水， 12 小时播放， 内置麦克风

输出：
```

## Variations

### Zero-Shot Extension
For when you have no examples but can describe the pattern:

```
# 任务：{{task_description}}

## 模式
{{detailed_pattern_description}}

## 格式
{{output_format_specification}}

## 该你了
输入： {{new_input}}
输出：
```

### One-Shot Learning
For simple patterns that can be communicated with a single example:

```
# 任务：{{task_description}}

## 例
输入：{{input_example}}
输出：{{output_example}}

## 该你了
输入： {{new_input}}
输出：
```

### Many-Shot Learning
For complex patterns requiring many examples:

```
# 任务：{{task_description}}

## 例子
[示例 1-10 格式为输入/输出对]

## 测试用例
[验证理解的其他示例]

## 该你了
输入： {{new_input}}
输出：
```

## Best Practices

- **Use diverse examples** that cover different cases and edge conditions
- **Order examples strategically** from simple to complex to build understanding
- **Include 3-5 examples** for most tasks (fewer for simple patterns, more for complex ones)
- **Ensure consistency** in formatting across all examples
- **Choose representative examples** that clearly demonstrate the pattern
- **Make examples distinct enough** to highlight the pattern rather than superficial similarities
- **For classification tasks**, include examples of all possible categories
- **For generative tasks**, show range in style, length, and content as appropriate
- **Test the pattern** by trying different inputs to ensure the AI has properly learned it

## Related Templates

- **Minimal Context Template**: When examples aren't necessary and direct instructions suffice
- **Chain of Thought Template**: When you need to demonstrate reasoning processes step-by-step
- **Pattern and Anti-Pattern Template**: When showing both good and bad examples helps clarify expectations
