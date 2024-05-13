import subprocess

def run_code_in_repo(repo_path):
    subprocess.run(['python', 'cli_tool/cli_script.py'], check=True)

if __name__ == "__main__":
    run_code_in_repo('cli_tool')