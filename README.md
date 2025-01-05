# AirBnB Console v2

This is the command-line interpreter for the AirBnB Clone project. It is the foundational step towards creating a full web application, allowing the management of various objects, including `User`, `State`, `City`, `Place`, and more. This console will evolve to support HTML/CSS templating, database storage, APIs, and front-end integration in future phases of the project.

---

## Features

- **Initialization**: Create a BaseModel class to manage object creation, serialization, and deserialization.
- **Serialization & Deserialization**: Manage instances to and from JSON and files.
- **Models**: Create the essential models, including `User`, `State`, `City`, and `Place`, each inheriting from `BaseModel`.
- **Storage**: Implement a file storage engine for persisting data.
- **Testing**: Comprehensive unittests to validate all models and storage engine functionalities.

---

## Command Interpreter

The command interpreter, `console.py`, allows users to interact with the objects created for the AirBnB clone. Commands are available in both **interactive** and **non-interactive** modes.

### How to Start

To start the console in **interactive mode**, run:
```bash
$ ./console.py
