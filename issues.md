# Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|
| Shell command execution using `os.system()` | Security — High | 61 | Concatenating a path into a shell command can allow command injection. | Replace shell-based execution with a safer argument-based subprocess call, or remove the unused helper if it is not required. |
| Hardcoded temporary directory | Security — Medium | 8 | The report directory is hardcoded to `/tmp/expense_reports`, which may not exist or be appropriate on every platform. | Use Python's temporary-directory facilities or a safely managed application-specific directory. |
| Insecure temporary filename | Security — Medium | 55 | `tempfile.mktemp()` generates a filename without safely creating the file. | Use a secure temporary-file API, such as `tempfile.NamedTemporaryFile`, with appropriate file handling. |
| Hardcoded password | Security — Low | 5 | The bank-sync password is stored directly in the source code. | Read the secret from a suitable configuration or environment variable rather than hardcoding it. |
| Missing module docstring | Code quality | 1 | The module has no descriptive docstring. | Add a short module-level docstring. |
| Non-standard naming conventions | Code quality | Multiple | Several functions and variables do not follow Python naming conventions. | Rename functions and variables to use `snake_case` and constants to use `UPPER_CASE`, updating all references. |
| Broad exception handling | Code quality | 41 | Catching `Exception` may conceal unexpected errors. | Catch the specific exception types that the code is expected to handle. |
| Missing function docstrings | Code quality | Multiple | Functions do not explain their purpose. | Add concise docstrings describing each function's behaviour. |

## Verification

Initial Pylint score: 5.27/10

Initial Bandit findings: 1 High, 2 Medium, 1 Low

Final scores and findings: To be recorded after applying fixes and rerunning the tools.