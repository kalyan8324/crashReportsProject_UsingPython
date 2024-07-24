import subprocess

def run_fastapi():
    print("Fast api application running..")
    subprocess.run(["uvicorn", "server.app:app", "--reload", "--port", "8001"])

if __name__ == "__main__":
    run_fastapi()
