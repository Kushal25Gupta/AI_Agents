import asyncio
import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from faq_agent.agent import faq_agent

load_dotenv()

#will create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
  "user_name": "Kushal Gutpa",
  "user_preference": """
  I like to play badminton, basketball.
  My favorite food is Idli.
  My favorite TV show is Tenali Rama.
  Loves it when I am alone sometimes people would leave me alone.
  """,
}

APP_NAME = "Kushal Bot"
USER_ID = "kushal_gupta"
SESSION_ID = str(uuid.uuid4())
stateful_session = asyncio.run(
  session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
  )
)

print("CREATED NEW SESSION:")
print(f"\tSession Id: {SESSION_ID}")

runner = Runner(
  agent=faq_agent,
  app_name=APP_NAME,
  session_service=session_service_stateful,
)

new_message = types.Content(
  role="user",
  parts=[types.Part(text="What is Kushal's favorite TV show?")]
)

for event in runner.run(
  user_id=USER_ID,
  session_id=SESSION_ID,
  new_message=new_message
):
  if event.is_final_response():
    if event.content and event.content.parts:
      print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = asyncio.run(
    session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
)

print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")