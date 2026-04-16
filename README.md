<p align="center">
     <img src="/image/logo.png" width="400">

## Schooping-system: Application for students to find their groupmates

[MA Haochen](https://github.com/mhczxg-commits)
[LUO Kong Fai](https://github.com/robu-dga)
[Kelvin Cheng](https://github.com/Arming926)

Schooping-system is a system which provides a platform to find teammates for any activities.

For those who are fear to social with others in reality, it is recommended to try Schooping-system

Whatever you are finding friends or study partners

You can try Schooping-system ! 
## Interface Simulation
<p align="center">     
<img src="/image/interface simulation.png" width="800">

## 📚 Contents

- [Project Overview](#project-overview)
- [Core Features](#core-features)
- [Algorithm Explanation](#algorithm-explanation)
- [Class Structure](#class-structure)
- [Program Workflow](#program-workflow)
- [Key Advantages](#key-advantages)
- [Schooping1 User Guide](#schooping1-user-guide)
- [Schooping2 User Guide](#schooping2-user-guide)

---

## 📌Project Overview

This project is an automated group management and assignment program designed for course group allocation scenarios.
The system uses a Max-Heap to maintain group member counts and Heap Sort to sort groups from the smallest to largest size in real time. This ensures every new student is assigned to the least crowded, most available group, achieving fair and balanced member distribution.

## 🎯Core Features

1. Create groups with customizable maximum size limits
2. Add students to groups
3. Automatically check if a group is full
4. Maintain group size dynamically using Max-Heap
5. Sort groups by member count (ascending) using Heap Sort
6. Automatic allocation: New students join the group with the fewest members
7. Re-sort automatically after each assignment to maintain balance

## 🧠Algorithm Explanation

### Max-Heap
- Uses group member count as the sorting key
- Root node always represents the largest group
- Supports insertion, max extraction, heapify up, and heapify down

### Heap Sort
- Insert all groups into a Max-Heap
- Extract max elements repeatedly to build a sorted list
- Reverse the result to get smallest → largest order
- Guarantees efficient selection of the most available group

## 📁Class Structure

### Group Class
Manages individual group information and members
- `group_id`: Unique group ID
- `members`: List of group members
- `max_size`: Maximum member limit
- `get_member_count()`: Returns current number of members
- `is_full()`: Checks if group has reached capacity
- `add_member()`: Adds a new student to the group

### MaxHeap Class
Implements a max-heap to efficiently manage group sizes
- `insert()`: Inserts a group into the heap
- `extract_max()`: Removes and returns the largest group
- `_heapify_up()`: Maintains heap structure upward
- `_heapify_down()`: Maintains heap structure downward

### heap_sort_groups Function
Performs heap sort and returns groups sorted from fewest to most members


## 🚀Program Workflow

1. Initialize 4 groups with a maximum size of 5
2. Prepopulate some students into groups
3. Use heap sort to display groups from least to most crowded
4. Automatically assign 4 new students
5. Re-sort after each assignment
6. Display final group sizes


## 💡Key Advantages

✅ Fair and automatic student allocation

✅ Efficient heap‑based data structure

✅ Balanced group member distribution

✅ Clean, readable, and maintainable code

✅ Ideal for coursework and academic projects

<p align="center">     
<img src="/image/team.jpg" width="400">

<p align="center">Working together never feel alone 
together makes us home！！！




## 🚀Schooping1 User Guide

Welcome to Schooping! This guide will help you set up and run the Group Management System on your local machine.

## 📋 Prerequisites     

Before running the program, ensure you have the following installed:

✅ Python 3.8 or higher.

## 📥 Installation & Setup

1. Click into main profile of our Schooping system
2. Click the green 「<> Code」 button
3. Click the download ZIP
4. Unzip the file you download
5. Double click the .py file to run the program
6. Enjoy your experience

## 📖 Quick Start Instructions

### 1.Initial Access
Upon launching, you will see the Welcome Menu:
- Register: Create a new account.
- Login: Enter your credentials to access the system.

### 2. Role Selection
Once logged in, the system determines your role based on your status:
- No Group: You will be asked to choose between (1) Create a Group [Leader] or (2) Join a Group [Member].
- In a Group: The system will automatically load your specific management or member menu.

### 3. Key Operations
- As a Leader: You can approve/reject pending applications and dissolve the group (which resets all members back to the initial state).
- As a Member: You can browse all available groups and check your application status.

## 🛠️ Troubleshooting

- ModuleNotFoundError: This program uses the Python Standard Library only (abc, math, etc.), so no external pip install is required. If you encounter errors, ensure you are running Python 3.
- Input Errors: If you enter an invalid menu option, the system will prompt you with a "Warning" message and allow you to try again without crashing.

## 👥 Demo Credentials

For the convenience of grading, you may use the following pre-registered account:

<div align="center">
<h3>🔐 System Login Interface</h3>
<pre style="font-family: monospace; font-size: 14px; color: #58a6ff;">
┌─────────────────────────────┐
│  _______________________    │
│ │ Username     boss     │    │
│  _______________________    │
│                             │
│  _______________________    │
│ │ Password      123     │    │
│  _______________________    │
│                             │
│   [ Sign In ]               │
└─────────────────────────────┘
</pre>
</div>


## Simulation
<p align="center">     
<img src="/image/login and register.png" width="200">

## 🚀Schooping2 User Guide


<p align="center">
     <img src="/image/friends group.avif" width="300">

## <a name="Statement"></a>:underage:Statement

# We do not recommend minors use our system.
Users are responsible for their own actions, and we bear no responsibility whatsoever.
