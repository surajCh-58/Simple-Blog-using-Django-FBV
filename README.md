# Simple Blog CRUD Application

This is a lightweight CRUD (Create, Read, Update, Delete) blog application built using Django.

## Project Overview
The core functionality of this application is powered by **Django Function-Based Views (FBVs)**. 

### Development Credits
* **Logic, Models, & Structure:** All backend Python logic, URL routing, and HTML structure were implemented by the project owner.
* **Styling & UI/UX:** The aesthetic appeal, responsive layout, and integration of **Bootstrap 5** were refined with the assistance of **Gemini**.

## Key Features
* **Function-Based Views:** Simple and direct view logic.
* **ModelForm Integration:** Efficient data handling using `ModelForm` with automated widget styling.
* **Bootstrap Styling:** Professional, responsive interface using Bootstrap 5 components such as Cards, Tables, and Buttons.
* **Form Automation:** The `form-control` CSS class is automatically injected into all form fields via the `__init__` method in `forms.py`, ensuring consistent design without manual HTML styling.

## Technical Details
* **Framework:** Django 6.0.6
* **Language:** Python 3.13.14
* **Styling Library:** Bootstrap 5 (via CDN)

## Acknowledgement
The backend development and initial implementation were completed independently. Gemini provided guidance on:
1. Debugging `get_object_or_404` implementation.
2. Integrating Bootstrap components for consistent UI/UX.
3. Automating CSS class injection in Django forms.
4. Refactoring HTML templates for better readability and structure.