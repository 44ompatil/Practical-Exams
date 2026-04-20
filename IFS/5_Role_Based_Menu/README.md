# Practical 5: Role-Based Menus

## Concept
Role-Based Access Control (RBAC) restricts system access to authorized users based on their assigned roles. Within an application, an administrator typically needs full access to the backend systems (e.g., adding/removing users, viewing logs), while a normal user only needs access to basic tasks (e.g., viewing their own profile). Providing specific menus based on roles adheres to the principle of least privilege.

## Objective
Write a program to demonstrate different menus for Admin and normal users after a successful login.

## Code Explanation (`5_role_menu.py`)
1.  **Extended Database**: The simple `user_db` is updated. Each user entry is no longer just a string mapping, but a dictionary containing both the `password` (hash) and their `role` ("admin" or "user").
2.  **Authentication**: Uses SHA-256 for secure hashing equivalent to previous practicals. It checks both the username and the credential matching.
3.  **Role Extraction & Routing**: If authentication is successful, the program retrieves `users[username]["role"]`. Using an `if-elif` structure, the code delegates control flow to either `display_admin_menu()` or `display_user_menu()`. 
4.  **Specialized Menus**: The admin menu acts as a mock display for privileged operations. The user menu offers basic self-service options.
