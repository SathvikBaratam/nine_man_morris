## 🔹 Nine Men's Morris – Project Preview

This project is a complete terminal-based implementation of **Nine Men’s Morris**, a classic two-player strategy board game.  
It features a clean ASCII board, colored highlights, saving/loading, cross-platform exit support, and a smooth gameplay flow covering both **placement** and **movement** phases.

## 🔹 Project Preview

- Fully playable **Nine Men’s Morris** in the terminal  
- ASCII-based game board with position indicators `(0–23)`  
- Player names, turn display, mill notifications, and win detection  
- Save/Load support (`nine_morris.sav`)  
- Cross-platform exit commands (`exit`, `quit`, `e`, `q`)  
- Clean separation of logic:
  - `board.c/.h` → board & rendering  
  - `game.c/.h` → turn logic, placing & moving  
  - `mill.c/.h` → mill detection & removal rules  
  - `main.c` → initialization, rules, player setup  
  - `Makefile` → build automation (Windows/Linux/Mac)

## Folder structure
project/
├── src/
│   ├── main.c
│   ├── game.c
│   ├── board.c
│   ├── mill.c
│
├── include/
│   ├── game.h
│   ├── board.h
│   ├── mill.h
│
├── Makefile
└── README.md

### Prerequisites

Before running:

1)Install GCC

2)Install Make (Linux/Mac; Windows needs MinGW/MSYS2)

3)OS requirements

## 🔹 Key Game Functionalities

### ✔ 1. **Board Rendering**
- ASCII board with index markers  
- `.`, `O`, `X` symbols for empty/white/black  
- Highlights last move  
- Auto-clear between turns (platform safe)

### ✔ 2. **Placement Phase**
- Players alternate placing 9 tokens  
- Validates empty position  
- Detects mill formation immediately after placement  
- Allows opponent piece removal after forming a mill  

### ✔ 3. **Movement Phase**
- Normal movement restricted to adjacent positions  
- Flying rules enabled when a player has only 3 pieces  
- Automatic win detection:
  - Opponent has <3 pieces  
  - Opponent cannot move  

### ✔ 4. **Mill Detection & Rules**
- Uses predefined triple combinations  
- Checks if move/placement forms a mill  
- Removal rules:
  - Cannot remove pieces in opponent's mill  
  - Unless all opponent pieces are inside mills  

### ✔ 5. **Saving & Loading the Game**
- Saves board + last move to `nine_morris.sav`  
- Load support integrated via input commands  
- Compatible on Windows, Linux, macOS  
### ✔ 6. **SAVE AND EXIT FEATURE**
Players can save or exit the game at any time using quick commands. Press ‘s’ to save the current game state, ‘e’ to exit immediately without saving, and ‘es’ to save and exit together. These commands work during both placing and moving phases, allowing players to leave the game at any point and resume later using the Load Game option.

### ✔ 7. **Input Safety**
- Trims whitespace  
- Rejects invalid numbers  
- Provides informative error messages  

## 🔹 Build and Run Instructions

## Windows (MinGW)

#### **Build**

      mingw32-make

#### **Run**

    nine_morris.exe

### 🐧 Linux / macOS

#### **Build**

    make


#### **Run**

    ./nine_morris

###  If Makefile is missing or not working

Manually compile with:
          gcc main.c board.c game.c mill.c -o nine_morris
Windows:
      gcc main.c board.c game.c mill.c -o nine_morris.exe
#### Cleaning Up
To remove all generated object files (.o) and the executable (nine_morris), use the clean target:
make clean
