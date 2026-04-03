# Installation Guide

This document provides a detailed installation guide for the Repowering Flexibility Optimization project. Follow the instructions according to your operating system.

## Prerequisites

Before you start installing the software, make sure you have the following prerequisites:
- **Python ≥ 3.8**
- **Node.js ≥ 14** (if applicable)
- **Git**

## Installation Instructions

### Windows
1. Download and install Python from the [official website](https://www.python.org/downloads/).
2. Open Command Prompt and verify the installation:
   ```bash
   python --version
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/farazaghajani-eng/repowering_flexibility_optimization.git
   cd repowering_flexibility_optimization
   ```
4. Install necessary packages:
   ```bash
   pip install -r requirements.txt
   ```
5. (Optional) Install Node.js from the [official website](https://nodejs.org/).
   If your project requires it and install npm packages:
   ```bash
   npm install
   ```


### macOS
1. Install Homebrew if you don't have it installed yet:
   ```bash
   /bin/bash -c "
   $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python and Node.js:
   ```bash
   brew install python node
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/farazaghajani-eng/repowering_flexibility_optimization.git
   cd repowering_flexibility_optimization
   ```
4. Install necessary packages:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

### Linux
1. Update your package list:
   ```bash
   sudo apt-get update
   ```
2. Install Python and Git:
   ```bash
   sudo apt-get install python3 python3-pip git
   ```
3. (Optional) For Node.js, use the following commands:
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```
4. Clone the repository:
   ```bash
   git clone https://github.com/farazaghajani-eng/repowering_flexibility_optimization.git
   cd repowering_flexibility_optimization
   ```
5. Install necessary packages:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

## Troubleshooting
- **Issue:** Command not found
  - **Solution:** Ensure that Python, Node.js, and Git are installed and added to your system's PATH.
- **Issue:** Package installation fails
  - **Solution:** Check if the requirements.txt file is correctly configured and if there are any compatibility issues with your OS.

## Optional Development Setup
1. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Install development packages:
   ```bash
   pip install -r dev_requirements.txt
   ```

3. Start the development server (if applicable):
   ```bash
   npm start
   ```

4. Happy coding!