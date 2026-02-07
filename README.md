Aproposdrive AWS & DevOps Assignment

Candidate: Samyak Londhe


Repository structure:
aproposdrive-aws-devops-assignment/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── templates/
│
├── screenshots/
│   ├── ss1.png
│   ├── ss2.png
│   ├── ss3.png
│   └── ...
│
└── README.md


Task 1 – Application


I first created the project folder and opened it in VS Code to start working on the application.
Screenshot:
screenshots/ss1.png – Project files opened in VS Code

I built a simple user registration page using Flask where a user can enter name and email.
Screenshot:
screenshots/ss2.png – User registration page in browser

After submitting the form, a success page is shown.
Screenshot:
screenshots/ss3.png – Form submitted successfully

Then I checked the database to confirm the data is actually stored.
Screenshot:
screenshots/ss4.png – User data visible in MySQL table


Task 2 – Docker

After confirming the app works locally, I containerized it.
Created a Dockerfile for the Flask app and built the image.
Screenshot:
screenshots/ss5.png – Docker image created

Created docker-compose.yml to run Flask app and MySQL together.
Screenshot:
screenshots/ss7.png – docker-compose.yml file

Started the containers and verified both app and database are running.
Screenshot:
screenshots/ss6.png – Containers running using docker ps


Task 3 – AWS EC2 Deployment

Launched a free-tier eligible EC2 instance.
Screenshot:
screenshots/ss8.png – EC2 instance running

Connected to the instance using SSH.
Screenshot:
screenshots/ss9.png – SSH connected to EC2

Checked Docker and Docker Compose versions on EC2.
Screenshot:
screenshots/ss10.png – Docker and Docker Compose version

Copied application files from local machine to EC2 using SCP.
Screenshot:
screenshots/ss11.png – SCP file transfer

Verified the application folder structure on EC2.
Screenshot:
screenshots/ss12.png – Tree structure on EC2

Started containers on EC2.
Screenshot:
screenshots/ss13.png – Docker containers running on EC2


Task 4 – Application Access

Accessed the application using EC2 public IP.
Screenshot:
screenshots/ss14.png – User registration page via public IP

Task 5 – Load Balancer & Auto Scaling
Pushed complete project code to GitHub repository.
Screenshot:
screenshots/ss15.png – Git push confirmation

Created an Application Load Balancer.
Screenshot:
screenshots/ss16.png – ALB created

Configured listener for the load balancer.
Screenshot:
screenshots/ss17.png – ALB listener configuration

Created Auto Scaling Group using launch template.
Screenshot:
screenshots/ss18.png – Auto Scaling Group created

Verified instance launched by ASG.
Screenshot:
screenshots/ss19.png – ASG instance running

Created and attached target group.
Screenshot:
screenshots/ss20.png – Target group attached

Confirmed instance type is free-tier eligible.
Screenshot:
screenshots/ss21.png – t2.micro instance

Set desired capacity to 1 to avoid extra cost.
Screenshot:
screenshots/ss22.png – Desired capacity set to 1


Task 6 – Cost Optimization

Used only free-tier eligible instance types.
Kept desired capacity at minimum.
Used Docker containers to reduce resource usage.


Task 7 – Troubleshooting (Manual Explanation)

App not accessible:
Initially failed due to security group rules. Fixed by allowing required ports.


Container running but port not reachable:
Issue was incorrect port mapping. Verified using docker ps and fixed mapping.


ALB health check failures:
Health check failed because the app took time to start. After startup completed, target became healthy automatically.


Final Result

Application is running on EC2 using Docker.
Database is connected and storing data.
ALB and Auto Scaling are configured.
All steps are documented with screenshots.