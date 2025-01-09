# Timewarrior Task Automator

A Python script to automate [Timewarrior](https://timewarrior.net/) task tracking and schedule its termination using the `at` command. This script simplifies managing Timewarrior tasks with customizable project names, tags, and duration.

---

## Features

- **Automated Task Tracking**: Start a Timewarrior task with a project name and optional tags.
- **Scheduled Stop**: Automatically schedule the stop of the task after a specified duration using the `at` command.
- **Customizable**: Specify the project name, tags, and duration directly through command-line arguments.
- **Error Handling**: Ensures that required binaries (`timew` and `at`) are installed before execution.

---

## Requirements

- **Python 3.6+**
- **Timewarrior**: A time tracking tool. [Installation Guide](https://timewarrior.net/docs/)
- **at**: A command-line scheduling utility. Install it using your package manager:
  - On Debian/Ubuntu:
    ```bash
    sudo apt install at
    ```
  - On Fedora:
    ```bash
    sudo dnf install at
    ```
  - On Arch Linux:
    ```bash
    sudo pacman -S at
    ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/timewarrior-task-automator.git
   cd timewarrior-task-automator
   ```

2. Ensure required dependencies (`timew` and `at`) are installed and available in your system's `PATH`.

3. (Optional) Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

---

## Usage

Run the script with the following options:

```bash
python timew.py [--project PROJECT] [--tags TAG1 TAG2 ...] [--hours HOURS]
```

### Arguments

- `--project`: (Optional) Name of the project/task to track. Default: `"Brain Image Library"`.
- `--tags`: (Optional) Space-separated list of tags associated with the task.
- `--hours`: (Optional) Duration (in hours) the task will last. Default: `2`.

---

## Examples

### Example 1: Start a Task with Default Values
Start a task with the default project name `"Brain Image Library"` and duration of `2 hours`:
```bash
python timew.py
```

Expected behavior:
1. Starts the task:
   ```bash
   timew start "Brain Image Library"
   ```
2. Schedules the stop command:
   ```bash
   echo 'timew stop "Brain Image Library"' | at now + 2 hours
   ```

---

### Example 2: Customize the Task's Project Name and Duration
Start a task for a custom project (`"Research Project"`) that will last for 5 hours:
```bash
python timew.py --project "Research Project" --hours 5
```

Expected behavior:
1. Starts the task:
   ```bash
   timew start "Research Project"
   ```
2. Schedules the stop command:
   ```bash
   echo 'timew stop "Research Project"' | at now + 5 hours
   ```

---

### Example 3: Add Tags to a Task
Start a task for the default project name with the tags `development` and `testing`, and let it last for 3 hours:
```bash
python timew.py --tags development testing --hours 3
```

Expected behavior:
1. Starts the task:
   ```bash
   timew start "Brain Image Library" development testing
   ```
2. Schedules the stop command:
   ```bash
   echo 'timew stop "Brain Image Library" development testing' | at now + 3 hours
   ```

---

### Example 4: Fully Customized Task
Start a task with a custom project name, tags, and duration:
```bash
python timew.py --project "Open Source Contributions" --tags coding documentation --hours 6
```

Expected behavior:
1. Starts the task:
   ```bash
   timew start "Open Source Contributions" coding documentation
   ```
2. Schedules the stop command:
   ```bash
   echo 'timew stop "Open Source Contributions" coding documentation' | at now + 6 hours
   ```

---

### Example 5: Ensure Error Handling
If `timew` or `at` is not installed, the script will display an appropriate error message:
```bash
Error: 'timew' is not installed or not available on the system's PATH.
Error: 'at' is not installed or not available on the system's PATH.
```

---

## Error Handling

The script ensures that both `timew` and `at` are installed and accessible before execution. If either is missing, it will terminate with a clear error message.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

---
