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




## <a name="Statement"></a>:underage:Statement

# We do not recommend minors use our system.
Users are responsible for their own actions, and we bear no responsibility whatsoever.
