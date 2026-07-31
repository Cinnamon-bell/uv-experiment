from datetime import datetime


def greeting() -> None:
    """Print a greeting."""
    print("Hello! Welcome to the automation project.")


def current_datetime() -> datetime:
    """Return the current date and time."""
    return datetime.now()


def write_log(now: datetime) -> None:
    """Write the current date and time to a log file."""
    with open("run_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Workflow ran at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")


def main() -> None:
    """Run the application."""
    greeting()
    now = current_datetime()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    write_log(now)


if __name__ == "__main__":
    main()


"""
mypy error example:
main.py:11: error: Incompatible return value type (got "datetime", expected "str")  [return-value]
main.py:18: error: "str" has no attribute "strftime"  [attr-defined]

-this pops up when def current_datetime() -> datetime: is changed to def current_datetime() -> str: because 
the return type is wrong, since it returns datetime.
"""