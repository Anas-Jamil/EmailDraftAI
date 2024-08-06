# Email Generator

## Made by Anas Jamil

This project is an email generator that uses OpenAI's GPT-3 to generate professional emails based on user input. It includes a GUI frontend built with `customtkinter` and integrates with Microsoft Outlook to send emails.

## Project Structure
- **`src/`**: Contains the main source code for the application.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`common/`**: Contains utility functions and helpers.
    - **`__init__.py`**: Marks the directory as a Python package.
    - **`utils.py`**: Utility functions used across the project.
  - **`models/`**: Contains data models.
    - **`__init__.py`**: Marks the directory as a Python package.
    - **`email_data.py`**: Data model for email information.
  - **`services/`**: Contains core service functions for the application.
    - **`__init__.py`**: Marks the directory as a Python package.
    - **`email_service.py`**: Functions to generate email content and send emails.
  - **`main.py`**: Main script for email generation and sending.
  - **`frontend.py`**: GUI frontend built with customtkinter.
- **`tests/`**: Contains unit tests for the application.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`test_main.py`**: Tests for `main.py`.
  - **`test_frontend.py`**: Tests for `frontend.py`.
- **`README.md`**: Project documentation.
- **`requirements.txt`**: Lists project dependencies.
