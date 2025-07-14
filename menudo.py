import os

def show_menu():
    print("""
    ------------------------
    Docker Menu Project
    ------------------------
    1. Launch new container
    2. Stop container
    3. Remove the container
    4. Start the container
    5. List images
    6. List all containers
    7. Exit
    """)

def runcont():
    image_name = input("Enter image name to run: ")
    container_name = input("Enter container name (optional): ")
    port_map = input("Enter port mapping (e.g. 8080:80) or leave blank: ")

    cmd = "docker run -d"
    if port_map:
        cmd += f" -p {port_map}"
    if container_name:
        cmd += f" --name {container_name}"
    cmd += f" {image_name}"
    os.system(cmd)

def stopcont():
    container_id = input("Enter container ID or name to stop: ")
    os.system(f"docker stop {container_id}")

def removecont():
    container_id = input("Enter container ID or name to remove: ")
    os.system(f"docker rm {container_id}")

def startcont():
    container_id = input("Enter container ID or name to start: ")
    os.system(f"docker start {container_id}")

def listimages():
    os.system("docker images")

def listallcontainers():
    os.system("docker ps -a")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            runcont()
        elif choice == "2":
            stopcont()
        elif choice == "3":
            removecont()
        elif choice == "4":
            startcont()
        elif choice == "5":
            listimages()
        elif choice == "6":
            listallcontainers()
        elif choice == "7":
            print("Exiting Docker automation menu. Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()