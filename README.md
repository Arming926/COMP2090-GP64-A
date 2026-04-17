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

<p align="center">
     <img src="/image/friends group.avif" width="300">

## 📖Table of Contents

- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [User Guide](#user-guide)
- [Trouble Shooting](#trouble-shooting)
- [Technical Architecture](#technical-architecture)
- [Demo Credentials](#demo-credentials)

## ✨Key Features

- **Role-Based Access Control (RBAC)**: Distinctive interfaces and permissions for "Leader" and "Member" roles, ensuring organized group hierarchy.

- **Dynamic Status Tracking**: Real-time updates for members regarding their application status, with instant system notifications if a group is disbanded or if a member is removed.

- **Defensive Programming**: Robust validation logic to prevent edge cases such as joining multiple groups simultaneously, exceeding member limits, or invalid user inputs.

## 📋Prerequisites     

Before running the program, ensure you have the following installed:

✅ Python 3.8 or higher.

## 📥Quick Start
 
1. Click into main profile of our Schooping system
2. Click the green 「 ![Code](https://img.shields.io/badge/--%3C%3E%20Code-brightgreen?style=for-the-badge)」 button
3. Click the download ZIP
4. Unzip the file you download
5. Double click the .py file to run the program
6. Enjoy your experience👍

## 📖User Guide

### 1.Initial Access
Upon launching, you will see the Welcome Menu:
<p align="center">
     <img src="/image/login and register.png" width="400">

- Register: Create a new account.
- Login: Enter your credentials to access the system.

### 2. Role Selection
Once logged in, the system determines your role based on your status:
<p align="center">
     <img src="/image/COJ.png" width="400">

- No Group: You will be asked to choose between (1) Create a Group [Leader] or (2) Join a Group [Member].
- In a Group: The system will automatically load your specific management or member menu.

### 3. Key Operations
- As a Leader: You can approve/reject pending applications and dissolve the group (which resets all members back to the initial state).
- As a Member: You can browse all available groups and check your application status.


## Trouble Shooting

- ModuleNotFoundError: This program uses the Python Standard Library only (`abc`, `math`, etc.), so no external pip install is required. If you encounter errors, ensure you are running Python 3.
- Input Errors: If you enter an invalid menu option, the system will prompt you with a "Warning" message and allow you to try again without crashing.

## 🛠Technical Architecture

This project strictly adheres to the **Four Pillars of Object-Oriented Programming (OOP)**:
- **Abstraction**: Utilizes abc.ABC to define a User base class, enforcing a structural contract for all subclasses.
- **Inheritance**: Establishes a clear hierarchy where Leader inherits from Member, and Member inherits from User.
- **Encapsulation**: Protects data integrity using private attributes `__MAX_SIZE` and object referencing `joined_group_obj` to manage internal states.
- **Polymorphism**: Implements method overriding for `show_menu()`, allowing a single interface call to execute role-specific behaviors.

## 👥Demo Credentials

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

<p align="center">
     <img src="/image/Nominor.png" width="100">


# We do not recommend minors use our system.
Users are responsible for their own actions, and we bear no responsibility whatsoever.
