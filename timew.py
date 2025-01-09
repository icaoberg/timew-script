import argparse
import subprocess
import shutil
import sys

def check_binary(binary_name):
    """
    Check if a binary is available on the system's PATH.

    Args:
        binary_name (str): The name of the binary to check (e.g., 'timew', 'at').

    Raises:
        SystemExit: If the binary is not found in the system's PATH.
    """
    if not shutil.which(binary_name):
        print(f"Error: '{binary_name}' is not installed or not available on the system's PATH.", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Automates Timewarrior task creation and scheduling a stop using the 'at' command.

    This script:
    1. Checks if the required binaries ('timew' and 'at') are available.
    2. Starts a Timewarrior task with the provided project name and tags.
    3. Schedules the stop of the task after a specified duration using the 'at' command.

    Args:
        --project: The name of the project/task (default: "Brain Image Library").
        --tags: A list of tags to associate with the task.
        --hours: Duration (in hours) the task will last (default: 2 hours).
    """
    # Check if required binaries are available
    check_binary("timew")
    check_binary("at")

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Automate Timewarrior task with tags and scheduled stop.")
    parser.add_argument(
        "--project",
        default="Brain Image Library",
        help='The project name for the task (default: "Brain Image Library").'
    )
    parser.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="List of tags for the task."
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=2,
        help="Duration (in hours) the task will last (default: 2 hours)."
    )

    # Parse command-line arguments
    args = parser.parse_args()
    project = args.project
    tags = args.tags
    hours = args.hours

    # Construct the timew start command
    tags_str = " ".join(tags)  # Join all tags into a single space-separated string
    start_command = f'timew start "{project}" {tags_str}'  # Create the start command
    print(f"Running command: {start_command}")  # Inform the user of the command being run
    subprocess.run(start_command, shell=True)  # Execute the start command

    # Construct the timew stop command and schedule it using 'at'
    stop_command = f'timew stop "{project}" {tags_str}'  # Create the stop command
    schedule_command = f'echo "{stop_command}" | at now + {hours} hours'  # Schedule the stop command
    print(f"Scheduling stop command: {schedule_command}")  # Inform the user of the scheduled command
    subprocess.run(schedule_command, shell=True)  # Execute the scheduling command

if __name__ == "__main__":
    main()
