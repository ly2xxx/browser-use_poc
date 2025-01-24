import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"

import asyncio
from browser_use import Agent
from langchain_ollama import ChatOllama
# from langchain.chat_models import ChatOllama
# from langchain_community.chat_models import ChatOllama



async def run_search() -> str:
    agent = Agent(
        # task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
        # llm=ChatOllama(
        #     model="deepseek-r1:latest",#"qwen2.5:32b-instruct-q4_K_M",
        #     num_ctx=32000,
        # ),
        # llm=ChatOllama(model=os.getenv('OLLAMA_MODEL'), base_url=os.getenv('OLLAMA_BASE_URL'), temperature=0),
        task='Go to https://www.amazon.co.uk/, search for laptop, sort by best rating, and give me the price of the first result',
        # task="Find flights on https://www.kayak.co.uk/ from Zurich to Beijing from 25.12.2024 to 02.02.2025.",
        llm=ChatOllama(model="qwen2.5:14b", base_url="http://127.0.0.1:11434", temperature=0),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())
