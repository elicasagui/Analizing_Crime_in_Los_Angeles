# setup_replit.py

import subprocess
import os

REPO_URL = "https://github.com/elicasagui/Analizing_Crime_in_Los_Angeles.git"
REPO_DIR = "Analizing_Crime_in_Los_Angeles"


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


def main():
    # 1. Clone repository (if not already present)
    if not os.path.isdir(REPO_DIR):
        run(f"git clone {REPO_URL}")
    os.chdir(REPO_DIR)

    # 2. Install dependencies using the default Python 3 in Replit
    run("pip install --upgrade pip")
    run("pip install -r requirements.txt")

    # 3. Download the CSV via our download script
    run("python src/download_data.py")

    print("\nSetup complete. Inside Replit you can now run:\n"
          "  • python main.py\n"
          "  • streamlit run src/dashboard.py\n")


if __name__ == "__main__":
    main()
