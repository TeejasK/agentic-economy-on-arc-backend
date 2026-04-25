import os
import subprocess

# 🔹 CHANGE THIS PATH if needed
PROJECT_PATH = r"D:\agentic-economy-on-arc-backend-main"

# 🔹 Your working repo
REPO_URL = "https://github.com/TeejasK/agentic-economy-on-arc-backend.git"


def run(cmd):
    print(f"> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed: {cmd}")
        exit(1)


def main():
    print("===================================")
    print("  GitHub Auto Push (TEEJAS K) 🚀")
    print("===================================")

    os.chdir(PROJECT_PATH)

    # Step 1: Init git if not exists
    if not os.path.exists(".git"):
        print("Initializing Git repo...")
        run("git init")

    # Step 2: Add files
    run("git add .")

    # Step 3: Commit
    result = subprocess.run(
        "git rev-parse --verify HEAD",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode != 0:
        run('git commit -m "Initial commit"')
    else:
        run('git commit -m "Update project files"')

    # Step 4: Set branch
    run("git branch -M main")

    # Step 5: Set remote
    remotes = subprocess.run("git remote", shell=True, capture_output=True, text=True)

    if "origin" not in remotes.stdout:
        run(f"git remote add origin {REPO_URL}")
    else:
        run(f"git remote set-url origin {REPO_URL}")

    # Step 6: Push
    run("git push -u origin main")

    print("===================================")
    print("✅ SUCCESS: Code uploaded to GitHub")
    print("===================================")


if __name__ == "__main__":
    main()