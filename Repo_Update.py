from github import Github
import os
import shutil

username = "AIUBInnoLab"
repo_name = "bscl_deploy"
access_token = "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"
local_directory = "/home/pi/Desktop/aiub_trp_ip_v1/bscl_deploy"
log_file = "/home/pi/Desktop/Repo_Update/update.log"
g = Github(access_token)
repo = g.get_user(username).get_repo(repo_name)
last_commit = repo.get_commits()[0]
last_modified_date = last_commit.last_modified

try:
    def create_updateLog():
        f = open(log_file, "w")
        f.write(last_modified_date)

    def create_localDirectory():
        print("Local Repository Does not Exist! \nAttempting To Download Repository...")
        try:
            create_updateLog()
            os.makedirs(local_directory)
            git_url = repo.clone_url.replace("https://", f"https://{access_token}@")
            os.system(f"git clone {git_url} {local_directory}")
            print("Repository Created Successfully!")
        except:
            print("ERROR! Failed to Create Repository!")

    def update_localDirectory():
        f = open("update.log", "w")
        f.write(last_modified_date)
        shutil.rmtree(local_directory)
        os.makedirs(local_directory)
        git_url = repo.clone_url.replace("https://", f"https://{access_token}@")
        os.system(f"git clone {git_url} {local_directory}")
        print("Repository Successfully Updated!")

    def checkUpdate():
        print("Checking for System Updates....")
        if not os.path.isfile(log_file):
            create_updateLog()
        f = open("update.log", "r")
        if not last_modified_date == f.read():
            print("Updates Available!\nUpdating System...")
            update_localDirectory()
        else:
            print("System is Up To Date!")

    def main():
        print("Repo Name: ",repo.name)
        print("Last Modified: ",last_modified_date)
        if not os.path.exists(local_directory):
            create_localDirectory()
        else:
            checkUpdate()

    if __name__ == "__main__":
        main()

except:
    print("System Error!\nExiting Update System...")
