# Solo Leveling Productivity System
#### Video Demo:  https://youtu.be/uv7AIybMXGc
#### Description:
Inspired by the anime Solo Leveling, where the main character Sung Jin-Woo possesses a game-like system in his mind, this program transforms that concept into a fun and motivating productivity tool. In the world of Solo Leveling, characters gain experience (EXP), level up, and rise through ranks by completing quests. This project brings that idea into the real world—allowing you to become stronger and more productive by completing your own real-life tasks in a gamified way.

🌟 Features
This program provides the following core features:

- View Your Stats: Check your current level, rank, EXP, active quests, and completed quest count.
- Show Quests: Display all currently active quests (tasks) that you've added.
- Add Quests: Add a new quest and specify how much EXP it is worth.
- Complete Quests: Mark an active quest as completed to gain EXP and possibly level up.
- Save and Load Data: All progress is saved in a JSON file so you can continue where you left off.

🚀 How It Works
When launched, the program reads data from player_data.json. If this is your first time, a new profile will be created with default stats (Level 1, Rank E, 0 EXP). You’ll be asked to input your name (ID). If your ID already exists in the data, it will load your previous progress. The user is given five options:

- View Stats
- Show Active Quests
- Add New Quest
- Complete Quest
- Exit

Quest Management:
You can add tasks as quests and assign a custom EXP value. Completing a quest increases your EXP and might result in a level-up.

Leveling and Ranking System:
The required EXP to level up is 100 * current_level. Ranks are upgraded based on level milestones:

- Level 1–4: Rank E
- Level 5–9: Rank D
- Level 10–14: Rank C
- Level 15–19: Rank B
- Level 20–24: Rank A
- Level 25+: Rank S

💾 Data Storage
Player data is stored persistently in a JSON file named player_data.json. Each player is stored as a dictionary entry under "id", with their own stats and quest logs.

✅ Error Handling
All user inputs are handled gracefully. Invalid numeric entries, empty inputs, or out-of-range selections are caught with proper error messages to prevent program crashes.

🧠 Motivation
This program was created as a final project after completing Harvard’s CS50P (Introduction to Programming with Python). The idea is to gamify productivity by drawing from anime mechanics and RPG systems. Instead of treating to-do lists as chores, this system turns them into a path toward character growth.

🙏 Acknowledgements
Huge thanks to CS50P for providing such an amazing course. This project would not have been possible without the foundational knowledge and inspiration it gave.

— Dylan Moreno
