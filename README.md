# Decoding the Capabilities of Large Language Models: A Multidimensional Comparison of LLM Tools for Algorithmic Code Generation

## Introduction

This repository contains the code and resources for the Comparison of LLM Tools for Algorithmic Code Generation.

File naming convention: LLM tools were prompted to fill in the methods. For instance, `directions.py` is the original template file and `directions_chat_gpt4.py` is the solution provided by Chat GPT 4, and so on.

## Virtual Environment Setup

### Unix-like Systems (macOS, Linux)

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. Run the setup script:
   ```bash
   bash setup.sh
   ```
3. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```

### For Windows

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. Run the setup script:

   - For Command Prompt:

     ```cmd
     setup.bat
     ```

   - For Git Bash:

     ```bash
     cmd.exe /c setup.bat
     ```

3. Activate the virtual environment:

   - For Git Bash and Command Prompt:

     ```cmd
     myenv\Scripts\activate.bat
     ```

   - For PowerShell:

     ```powershell
     myenv\Scripts\Activate.ps1
     ```

## Running Tests

### Unix-like Systems (macOS, Linux)

1. Ensure the script has execution permissions:
   ```bash
   chmod +x run_tests.sh
   ```
2. Run the script:
   ```bash
   ./run_tests.sh
   ```

### For Windows

1. Run the script:

   - For Command Prompt:

     ```cmd
     run_tests.bat
     ```

   - For Git Bash:

     ```bash
     cmd.exe /c run_tests.bat
     ```

## Pytest Command

To run the test for each coding challenge, navigate (`cd`) to its directory first (e.g., `Directions` or `Roman Numerals`, etc.) and then use the following commands.

### Unix-like Systems (macOS, Linux)

1. Apply execution rights:
   ```bash
   chmod +x run_tests.sh
   ```
2. Run the script:
   ```bash
   ./run_tests.sh
   ```

### Windows

1. Run the script:

   - For Command Prompt:

     ```cmd
     run_tests.bat
     ```

   - For Git Bash:

     ```bash
     cmd.exe /c run_tests.bat
     ```

## Prompts given to LLMs:

This guide is only for reapplication purposes. If you are an assessor, please disregard this step.

1. Copy and paste the assignment instructions (`rational_instructions.txt` or `roman_instructions.txt`) from Canvas. Note that there are no instructions for `Directions` and `Long Toss` challenges.
2. Copy and paste the template code associated with the project you are trying to run (`directions.py` or `long_toss.py` or `rational.py` or `roman.py`) from Canvas.
3. Send the following prompt to the LLM: "Implement the solution to template methods based on given instructions".

## License

This project is licensed under the MIT License - see the LICENSE file for details.
