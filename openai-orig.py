from browser_use import Agent
from langchain_openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use' in the search bar, click on the first post and return the first comment.",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())