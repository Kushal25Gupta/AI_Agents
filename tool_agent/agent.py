from datetime import datetime

from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
  """
  Get the current time in the format YYYY-MM-DD HH:MM:SS
  """

  return {
    "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }

root_agent = Agent(
  name="tool_agent",
  model="gemini-2.5-flash",
  description="You are a helpful assistant that uses tools to answer user queries",
  instruction="""
  Your are a helpful assistant that uses tools to answer user queries.
  -get_current_time
  """,
  tools=[get_current_time]
  # tools=[google_search],
)