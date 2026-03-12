# Terminal Hacking Sim — Full Game Plan

## Overview
You play as a freelance hacker. Each session you hack into servers of increasing difficulty, steal files, avoid detection, and build your reputation. It's endless — the game gets harder the better you do.

---

## Feature 1: Project Setup & Terminal Shell
The foundation. A loop that reads player input, parses commands, and prints responses.

- **Step 1.1** — Create the project folder structure (`main.py`, and empty files for future modules)
- **Step 1.2** — Build the main game loop (infinite loop, input prompt, exit command)
- **Step 1.3** — Build a command parser (splits input into command + arguments)
- **Step 1.4** — Add a `help` command that lists available commands
- **Step 1.5** — Style the shell (custom prompt like `[GHOST@darknet]>`, clear screen on start, ASCII banner)

---

## Feature 2: Player & Session State
Track who the player is and what's happening in the current session.

- **Step 2.1** — Create a `Player` class (name, reputation score, hacker rank)
- **Step 2.2** — Create a `Session` class (current target, connection status, trace level)
- **Step 2.3** — Add a `status` command that prints player info and current session state

---

## Feature 3: Network & Server System
The world the player hacks into. A collection of servers with different security levels.

- **Step 3.1** — Create a `Server` class (IP, name, security level, firewall on/off, files list)
- **Step 3.2** — Generate a random network of servers on game start
- **Step 3.3** — Add a `scan` command that lists nearby servers (IPs only, no details yet)
- **Step 3.4** — Add a `probe <IP>` command that reveals server details (security level, firewall, OS)

---

## Feature 4: Connection System
Let the player connect and disconnect from servers.

- **Step 4.1** — Add a `connect <IP>` command that attempts to connect (fails if firewall is active)
- **Step 4.2** — Add a `disconnect` command that ends the session
- **Step 4.3** — Update the shell prompt to show the connected server's IP when connected

---

## Feature 5: File System Simulation
Each server has a fake file system with directories and files to steal.

- **Step 5.1** — Design a simple file tree structure (nested dict or objects)
- **Step 5.2** — Add an `ls` command to list files/folders in the current directory
- **Step 5.3** — Add a `cd <dir>` command to navigate directories
- **Step 5.4** — Add a `read <file>` command to display file contents
- **Step 5.5** — Add a `download <file>` command to steal a file (adds to player's loot)

---

## Feature 6: Password Cracking Minigame
When a server requires a password, the player must crack it through a minigame.

- **Step 6.1** — Trigger the minigame when `connect`ing to a password-protected server
- **Step 6.2** — Build minigame: player sees a scrambled sequence and must type it correctly within a time limit
- **Step 6.3** — Difficulty scales with server security level (longer sequence, less time)
- **Step 6.4** — On failure, increment trace level; on success, grant access

---

## Feature 7: Firewall Bypass Minigame
Some servers have a firewall that must be disabled before connecting.

- **Step 7.1** — Add a `bypass <IP>` command that triggers the minigame
- **Step 7.2** — Build minigame: player is shown a pattern of numbers/symbols and must identify the odd one out or complete the sequence
- **Step 7.3** — Difficulty scales with security level
- **Step 7.4** — On success, firewall is disabled; on failure, trace level increases

---

## Feature 8: Trace System
A countdown that represents how close authorities are to catching the player.

- **Step 8.1** — Add a `trace` value to the Session (0–100%)
- **Step 8.2** — Trace increases over time while connected (background ticker), and on failed minigames
- **Step 8.3** — Show a trace warning when it crosses thresholds (50%, 75%, 90%)
- **Step 8.4** — At 100%, trigger a "TRACED" game over screen and end the session
- **Step 8.5** — Add a `trace --status` command so the player can check current trace level

---

## Feature 9: Social Engineering / Dialogue
Sometimes the player can manipulate NPCs instead of brute-forcing security.

- **Step 9.1** — Some servers have an NPC "sysadmin" that can be contacted
- **Step 9.2** — Add a `message <IP>` command to open a dialogue with the sysadmin
- **Step 9.3** — Build a dialogue system with 2–3 choices (bribe, bluff, threaten)
- **Step 9.4** — Outcome is based on player reputation and randomness — success lowers trace or disables firewall, failure raises trace

---

## Feature 10: Score & Reputation System
Reward the player for successful hacks.

- **Step 10.1** — Assign a bounty value to each file on a server
- **Step 10.2** — Add score when a file is successfully downloaded
- **Step 10.3** — Add reputation XP when a server is fully looted and disconnected cleanly
- **Step 10.4** — Build a rank system (e.g. Script Kiddie → Grey Hat → Ghost) based on reputation
- **Step 10.5** — Show a mission complete summary screen after each clean disconnect

---

## Feature 11: Difficulty Scaling & Progression
Make the game harder as the player improves.

- **Step 11.1** — Track a global difficulty level that increases with reputation
- **Step 11.2** — Higher difficulty = more security layers, faster trace, harder minigames
- **Step 11.3** — Unlock new server types at higher difficulties (government, military, megacorp)
- **Step 11.4** — Add a high score screen at game over

---

## Suggested Build Order
1 → 2 → 3 → 4 → 5 → 8 → 6 → 7 → 10 → 9 → 11
