from google.adk.agents import Agent

root_agent = Agent(
  name="greeting_agent",
  model="gemini-2.5-flash",
  description="You are a friendly agent who greets users",
  instruction="""
  Your are a helpful assistant that greets the user.
  Ask for the user's name and greet them.
  Then give the user's name meaning to user's.
  """,
)