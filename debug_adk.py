import os

print("BEFORE IMPORT")
print("VERTEX =", os.environ.get("GOOGLE_GENAI_USE_VERTEXAI"))
print("PROJECT =", os.environ.get("GOOGLE_CLOUD_PROJECT"))

from app.agri_guardian.agent import root_agent

print("\nAFTER IMPORT")
print("VERTEX =", os.environ.get("GOOGLE_GENAI_USE_VERTEXAI"))
print("PROJECT =", os.environ.get("GOOGLE_CLOUD_PROJECT"))
print("LOCATION =", os.environ.get("GOOGLE_CLOUD_LOCATION"))