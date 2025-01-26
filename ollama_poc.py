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
    # agent = Agent(
    #     task="Go to https://sports.ladbrokes.com/in-play/football and analyze the page structure. For each element:\n"
    #         "1. Extract and show the raw HTML\n"
    #         "2. Identify Playwright-compatible selectors\n"
    #         "3. Map elements to: match time, score, team names, event IDs\n"
    #         "4. Continue until all relevant elements are analyzed",
    #     llm=ChatOpenAI(
    #         model="gpt-4-turbo-preview",  # More capable at HTML analysis
    #         temperature=0.2  # Lower temperature for more consistent parsing
    #     ),
    #     include_attributes=[
    #         'title', 'type', 'name', 'role', 'id', 'class',
    #         'data-*', 'aria-*', 'href', 'src', 'value',
    #         'placeholder', 'for', 'text'
    #     ],
    #     max_failures=5,  # Increase retry attempts
    #     retry_delay=5,  # Shorter delay between retries
    #     max_input_tokens=32000,  # Reduced token limit for faster processing
    #     validate_output=True,  # Enable output validation
    #     tool_calling_method='function_calling',  # Explicit function calling
    #     max_actions_per_step=5  # Allow more actions per step
    # )
    agent = Agent(
        # task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
        # llm=ChatOllama(
        #     model="deepseek-r1:latest",#"qwen2.5:32b-instruct-q4_K_M",
        #     num_ctx=32000,
        # ),
        # llm=ChatOllama(model=os.getenv('OLLAMA_MODEL'), base_url=os.getenv('OLLAMA_BASE_URL'), temperature=0),
        # task="""
        # Analyze the login form at https://members.brsgolf.com/gsaayr/login with these specific steps:
        # 1. Navigate to the login page
        # 2. For each input field and button:
        #     - Extract and display the complete HTML markup
        #     - Identify all possible Playwright selectors (id, name, role, placeholder, aria-*)
        #     - Determine the field's purpose (username, password, submit)
        #     - List the most reliable selector strategy for each element
        # 3. Create a structured summary of:
        #     - Username field selectors
        #     - Password field selectors
        #     - Login button selectors
        # 4. Verify each selector's uniqueness on the page
        # 5. Continue analysis until all form elements are documented
        
        # Format findings as:
        # Element: [purpose]
        # HTML: [raw html]
        # Recommended Selector: [most reliable selector]
        # Alternative Selectors: [other valid selectors]
        # """,
        # include_attributes=[
        #     'id', 'name', 'type', 'role', 'class',
        #     'placeholder', 'aria-label', 'aria-describedby',
        #     'data-*', 'value', 'for', 'autocomplete', 'username', 'password', 'login'
        # ],
        # task='https://members.brsgolf.com/gsaayr/login, locate all fields needed for logging in to the website and print out the html per field, search for the locator tags suitable for playwright library to use. Do the analysis until you exhaust all steps.',
        # task="Go to https://sports.ladbrokes.com/in-play/football and analyze the page structure. For each element:\n"
        #     "1. Extract and show the raw HTML\n"
        #     "2. Identify Playwright-compatible selectors\n"
        #     "3. Map elements to: match time, score, team names, event IDs\n"
        #     "4. Continue until all relevant elements are analyzed",
        # task='Go to https://sports.ladbrokes.com/in-play/football, analyse the football matches listed on the page, search for the locator tags suitable for playwright library to extract match time, score, team name, and event id. For each screen element you identified, print the html snippet first, then match the element to match time, score, team name, and event id. If you found a match, say it. No matter if you find a match, pass on the next identified page element to the next step. Do the analysis until you exhaust all steps.',
        task='Go to https://www.amazon.co.uk/, search for laptop, sort by best rating, and give me the price of the first result',
        # task="""
        # Extract laptop price from Amazon UK with these precise steps:
        # 1. Navigate to https://www.amazon.co.uk/
        # 2. Search phase:
        #     - Locate the search input field
        #     - Enter "laptop"
        #     - Submit the search
        # 3. Sorting phase:
        #     - Find the sorting dropdown/button
        #     - Select "Avg. Customer Review" option
        # 4. Price extraction phase:
        #     - Identify the first product listing
        #     - Extract its price
        #     - Capture full product name
        #     - Note any special offers/discounts
        # 5. Return structured data:
        #     Product: [name]
        #     Price: [amount]
        #     Rating: [stars]
            
        # Expected elements to interact with:
        # - Search: input[id="twotabsearchtextbox"]
        # - Sort: span[data-action="a-dropdown-button"]
        # - Price: span[class*="price"]
        # """,
        # task="Find flights on https://www.kayak.co.uk/ from Zurich to Beijing from 25.12.2024 to 02.02.2025.",
        # task='Go to https://identitysso.betfair.com/view/login, Locate the tag to hit that should close the cookies popup',
        llm=ChatOllama(model="qwen2.5:14b", base_url="http://127.0.0.1:11434", temperature=0),
        max_failures=5,  # Increase retry attempts
        retry_delay=30,  # Longer delay between retries
        max_actions_per_step=5  # Allow more actions per step
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())
