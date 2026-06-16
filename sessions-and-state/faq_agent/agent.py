from google.adk.agents import Agent

faq_agent = Agent(
  name="faq_agent",
  model="gemini-2.5-flash",
  description = "Answer questions based on provided user details",
  instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preference}
    """,
)