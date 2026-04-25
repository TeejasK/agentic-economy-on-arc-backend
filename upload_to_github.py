import os
import subprocess

def run(cmd):
    print(f"> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        exit(1)

def main():
    print("===================================")
    print("   GitHub Auto Upload Script 🚀")
    print("===================================")

    repo_url = input("https://github.com/TeejasK/agentic-economy-on-arc-backend").strip()

    # Step 1: Initialize git (if not exists)
    if not os.path.exists(".git"):
        print("Initializing Git repository...")
        run("git init")

    # Step 2: Add all files
    print("Adding files...")
    run("git add .")

    # Step 3: Commit
    print("Committing...")
    # Check if commit exists
    result = subprocess.run("git rev-parse --verify HEAD", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if result.returncode != 0:
        run('git commit -m "Initial commit"')
    else:
        run('git commit -m "Update project"')

    # Step 4: Set branch to main
    print("Setting branch to main...")
    run("git branch -M main")

    # Step 5: Add remote origin
    print("Setting remote origin...")
    result = subprocess.run("git remote", shell=True, capture_output=True, text=True)
    
    if "origin" not in result.stdout:
        run(f"git remote add origin {repo_url}")
    else:
        print("Remote origin already exists")

    # Step 6: Push to GitHub
    print("Pushing to GitHub...")
    run("git push -u origin main")

    print("===================================")
    print("✅ DONE! Your project is live on GitHub")
    print("===================================")

if __name__ == "__main__":
    main()