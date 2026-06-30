# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import google.auth
from google.adk.apps import App
from app.agri_guardian.agent import root_agent
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

# Set up GCP project environment variables safely
try:
	pass
#    _, project_id = google.auth.default()
#    if project_id:
#        os.environ["GOOGLE_CLOUD_PROJECT"] = project_id

except Exception:
    pass

# Ensure fallbacks if project_id is not set
if not os.environ.get("GOOGLE_CLOUD_PROJECT"):
    os.environ["GOOGLE_CLOUD_PROJECT"] = ""  #personal-projects-368516"

os.environ["GOOGLE_CLOUD_LOCATION"] = ""  #global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"  #"True"

app = App(
    root_agent=root_agent,
    name="app",
)
