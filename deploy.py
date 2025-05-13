import subprocess
import os

def notify(message):
    print(messgae)


def deploy():
    try:
        # Install dependencies from requirements.txt
        subprocess.run(['pip3', 'install', '-r', 'requirements.txt'], check=True)
        # Stop any existing Flask app process
        subprocess.run(['pkill', '-f', 'python3 app.py'], check=False)
        # Start the Flask app in the background
        subprocess.Popen(['python3', 'app.py'])
        notify("Deployment completed successfully!")
    except subprocess.CalledProcessError as e:
        notify(f"Deployment failed: {e}")


if __name__ == "__main__":
    deploy()

