import os
import subprocess

username = "SERPENT47"
email = "khaliduzzaman.mredul@gmail.com"
repo = "https://github.com/SERPENT47/GitPushTest.git"

def git_init():
    try:
        subprocess.call(["git", "init"])
    except:
        print("Git Initialization failed!")
    '''try:
        subprocess.call(["git", "--version"])
    except:
        print("Git is not installed. Please install Git and try again.")
        
    try:
        subprocess.check_output(["git", "rev-parse", "--is-inside-work-tree"])
    except:
        print("Initializing git...")
        subprocess.call(["git", "init"])'''
        
def git_config():
    try:
        subprocess.call(["git", "config", "--global", "user.name", username])
        subprocess.call(["git", "config", "--global", "user.email", email])
    except:
        print("Error Configuring git!")

def git_add():
    print("1. Push Entire Folder\n2. Push Specific File")
    sel_opt = input("Select Option:")
    if sel_opt=='1':
        subprocess.call(["git", "add", "."])
    elif sel_opt=='2':
        file_name = input("Enter file name: ")
        subprocess.call(["git", "add", file_name])
        
def git_push():
    try:
        subprocess.call(["git", "commit", "-m", "Update"])
        subprocess.call(["git", "branch", "-M", "main"])
        subprocess.call(["git", "remote", "add", repo])
        subprocess.call(["git", "push", "-u", "origin", "main"])
    except:
        print("Error pushing into git!")
        
def main():
    git_init()
    git_config()
    git_add()
    git_push()

if __name__ == "__main__":
    main()

'''
SERPENT47
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
'''
