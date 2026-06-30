\# AgriGuardianAI Farmer Evaluation Scenarios



\## Weather Evaluation



\### Scenario 1

Farmer Location: Bidar

Question:

"What is the current weather in Bidar and should I irrigate today?"



Expected Agent:

weather\_agent



Success Criteria:

\- Retrieves weather information

\- Gives irrigation recommendation





\### Scenario 2

Farmer Location: Bengaluru

Question:

"Will rainfall affect my soybean crop today?"



Expected Agent:

weather\_agent



Success Criteria:

\- Retrieves weather data

\- Explains impact on soybean farming





\### Scenario 3

Farmer Location: Kalaburagi

Question:

"Is today suitable for pesticide spraying?"



Expected Agent:

weather\_agent



Success Criteria:

\- Checks weather conditions

\- Provides spraying advice





\---



\## Soil Analysis Evaluation



\### Scenario 4

Input:

pH=5.3

Nitrogen=low

Phosphorus=medium

Potassium=medium



Expected Agent:

soil\_agent



Success Criteria:

\- Detects acidic soil

\- Recommends lime application

\- Detects nitrogen deficiency





\### Scenario 5

Input:

pH=6.8

Nitrogen=low

Phosphorus=medium

Potassium=high



Expected Agent:

soil\_agent



Success Criteria:

\- Detects healthy pH

\- Recommends nitrogen improvement





\### Scenario 6

Input:

pH=8.2

Nitrogen=high

Phosphorus=low

Potassium=medium



Expected Agent:

soil\_agent



Success Criteria:

\- Detects alkaline soil

\- Recommends phosphorus improvement





\---



\## Market Evaluation



\### Scenario 7

Question:

"Suggest the most profitable crop for Kharif."



Expected Agent:

market\_agent



Success Criteria:

\- Returns Turmeric





\### Scenario 8

Question:

"Suggest the best crop for Kharif and Black soil."



Expected Agent:

market\_agent



Success Criteria:

\- Returns Tur





\### Scenario 9

Question:

"Suggest the best crop for Rabi and Sandy soil."



Expected Agent:

market\_agent



Success Criteria:

\- Returns Cumin





\### Scenario 10

Question:

"Suggest a low-water crop for Kharif."



Expected Agent:

market\_agent



Success Criteria:

\- Returns suitable low-water crops





\---



\## Advisory Evaluation



\### Scenario 11

Input:

Season=Kharif

Soil=Black

Water=Medium

pH=6.8

Nitrogen=low

Phosphorus=medium

Potassium=high



Expected Agent:

advisory\_agent



Success Criteria:

\- Recommends Tur

\- Explains reasoning





\### Scenario 12

Input:

Season=Rabi

Soil=Sandy

Water=Low

pH=7.0

Nitrogen=medium

Phosphorus=medium

Potassium=medium



Expected Agent:

advisory\_agent



Success Criteria:

\- Recommends Cumin





\### Scenario 13

Input:

Season=Kharif

Soil=Red

Water=High

pH=6.5

Nitrogen=medium

Phosphorus=medium

Potassium=high



Expected Agent:

advisory\_agent



Success Criteria:

\- Recommends Turmeric





\---



\## Multi-Agent Routing Evaluation



\### Scenario 14

Question:

"Which crop should I grow in Bidar this Kharif season?"



Expected Flow:

Coordinator → Weather → Soil → Market → Advisory



Success Criteria:

\- Correct routing sequence





\### Scenario 15

Question:

"My soil pH is 5.5 and nitrogen is low. What should I cultivate?"



Expected Flow:

Coordinator → Soil → Market → Advisory



Success Criteria:

\- Correct routing





\### Scenario 16

Question:

"Will today's weather affect my cotton crop?"



Expected Flow:

Coordinator → Weather → Advisory



Success Criteria:

\- Correct routing





\---



\## Edge Case Evaluation



\### Scenario 17

Invalid pH:

pH=15



Success Criteria:

\- Returns validation error





\### Scenario 18

Unknown Season:

Season=Summer



Success Criteria:

\- Handles unsupported season





\### Scenario 19

Unknown Soil:

Soil=Rocky



Success Criteria:

\- Returns fallback recommendation





\### Scenario 20

Empty Input



Success Criteria:

\- Requests additional information

