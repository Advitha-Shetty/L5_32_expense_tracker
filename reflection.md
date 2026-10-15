 Lab 5: Static Code Analysis — Reflection_note

 1. What is static code analysis?

Static code analysis examines source code without executing the program. Tools such as Pylint, Bandit, and Flake8 help identify code-quality problems, potential security vulnerabilities, and style violations.

 2. What issues were identified?

The initial analysis identified security concerns, including a hardcoded password, unsafe temporary-file creation, a hardcoded temporary directory, and the use of a shell command to open a file. Pylint also identified documentation, naming, and code-quality issues, while Flake8 reported formatting violations.

 3. How were the issues resolved?

The password check was changed to read the expected password from an environment variable and compare it securely. Unsafe temporary-file creation was replaced with `NamedTemporaryFile`, and shell-based file opening was replaced with Python's `webbrowser` module. I also improved documentation, naming, and code style to satisfy the analysis tools.

 4. What did I learn?

I learned that a program can produce the expected output and still contain security risks or maintainability problems. Using multiple static analysis tools helps identify different categories of issues. Re-running the tools after making changes helps verify that the findings have been addressed.
