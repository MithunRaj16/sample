AMC Bank Login System
•	Introduction
•	Description
•	Functional Requirements
•	Non-functional Requirements
•	Flow of Code
•	Usage
•	Contributors
Introduction

AMC Bank Login System is a simple web application built using Flask, a lightweight Python web framework. This application provides a basic login functionality where users can enter their username and password to log in.
Description

This application consists of a single web page where users can enter their credentials. Upon submission of the form, the application checks the provided credentials against a predefined set of users and passwords. If the login is successful, the user is redirected to a page displaying "Login Successful"; otherwise, they are redirected to a page displaying "Login Failed".

Functional Requirements

1.	The system should allow users to enter their username and password.
2.	The system should validate the provided credentials against the predefined set of users and passwords.
3.	On successful login, the system should display a "Login Successful" message.
4.	On failed login, the system should display a "Login Failed" message.

Non-functional Requirements

1.	Usability: The application should have an intuitive and user-friendly interface.
2.	Performance: The application should respond quickly to user actions and provide a seamless experience.
3.	Security: User credentials should be handled securely to ensure the privacy and integrity of user data.

Flow of Code

1.	The main entry point of the application is app.py.
2.	The login() function in app.py handles the login logic.
3.	The HTML template login.html contains the login form.
4.	The HTML template login_result.html displays the login result based on the login attempt.
5.	The CSS file styles.css contains the styles for the HTML templates.
Usage

1.	Clone the repository.
2.	Run the application using python app.py.
3.	Access the application in a web browser at http://localhost:8000.
Contributors

•Mithun Raj S R
