# 1. Create EC2 Instance 
Go to AWS → EC2 → Launch Instance

Select:

- AMI: Ubuntu (latest)
- Instance Type: t2.large (recommended)
- Create a key pair (.pem file)
- Enable auto-assign public IP
- Configure security group:
- Allow SSH (port 22)
- Storage: Minimum 30 GB

Launch the instance.

# 2. Connect to EC2 Instance

Use the following command from your local machine:

`ssh -i /path/to/key.pem ubuntu@<public-ip>`


If you get a permission error:

`chmod 400 /path/to/key.pem`

- On first connection, type yes when prompted.

# 3. Update System Packages 
`sudo apt update`

- This updates the package list so that you install the latest and secure versions of software.

# 4. Install Docker 

Follow the official documentation:

https://docs.docker.com/engine/install/

- Use the APT repository method.

This ensures:

- Installation of the latest stable version
- Proper dependency management
- Easier updates

# 5. Verify Docker Installation
`docker ps`

If you see a permission error:

- permission denied while trying to connect to the docker daemon

Run:

`sudo usermod -aG docker ubuntu`

Then log out and reconnect:

exit

Reconnect and run again:

`docker ps`

This step allows you to run Docker without using sudo.

# 6. Install kubectl 

Follow the official documentation:
https://kubernetes.io/docs/tasks/tools/

Use the curl installation method.

kubectl is required to interact with Kubernetes clusters for deploying and managing applications.

# 7. Install Terraform 

Follow the official documentation:

https://developer.hashicorp.com/terraform/install

Terraform is used to provision infrastructure such as VPC, EC2, and EKS using code.

# 8. Clone the Repository 
`git clone <your-repo-url>`

`cd <project-folder>`

# 9. Run the Application  
`docker compose up -d`

- This command starts all services defined in the docker-compose file in detached mode.

# 10. Update Security Group

- Go to AWS Console → EC2 → Security Groups → Edit Inbound Rules

Add the following rule:

- Type: Custom TCP
- Port: 8080
- Source: Anywhere (0.0.0.0/0)

This allows access to the application from a browser.

Security note:

Allowing all traffic from anywhere is not recommended for production
You can restrict access using “My IP” for better security

# 11. Access the Application

Open your browser and navigate to:

`http://<public-ip>:8080`
