import os, subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))
        is_valid_directory = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if not is_valid_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not file_path or not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        commands = ["python", target_dir]

        if args and args != []:
            commands.extend(args)

        run_result = subprocess.run(
            commands,
            cwd=working_directory_abs,
            capture_output=True,
            text=True, 
            timeout=30
        )

        result = []

        if run_result.returncode != 0:
            result.append(f"Process exited with code {run_result.returncode}")

        if run_result.stdout == "" and run_result.stderr == "":
            result.append("No output produced")
        else:
            if run_result.stdout:
                result.append(f"STDOUT: {run_result.stdout}")

            if run_result.stderr:
                result.append(f"STDERR: {run_result.stderr}")

        return "\n".join(result)

    except Exception as e: 
        return f"Error: executing Python file: {e}"