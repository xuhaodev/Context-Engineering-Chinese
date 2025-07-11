import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

def chat_completion(messages, temperature=1.0, top_p=1.0, model="openai/gpt-4.1-mini"):
    endpoint = "https://models.github.ai/inference"
    token = os.getenv("GITHUB_TOKEN")
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )
    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant."),
            UserMessage(messages),
        ],
        temperature=temperature,
        top_p=top_p,
        model=model
    )
    return response.choices[0].message.content

# 示例调用
if __name__ == "__main__":
    messages = "What is the capital of France?"
    result = chat_completion(messages)
    print(result)
