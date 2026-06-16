from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
  name="tool_agent",
  model="gemini-2.5-flash",
  description="You are a helpful assistant that uses tools to answer user queries",
  instruction="""
  Your are a helpful assistant that uses tools to answer user queries.
  If you need to search the web, use the google_search tool.
  """,
  tools=[google_search],
)