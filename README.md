lright. I’m going to fix this cleanly and decisively.
Below is a FULL README.md that WILL render images on GitHub if (and only if) your folder structure is exactly:

aproposdrive-aws-devops-assignment/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── templates/
│       ├── index.html
│       └── success.html
├── screenshots/
│   ├── ss1.png
│   ├── ss2.png
│   ├── ss3.png
│   └── ...
│   └── ss22.png
└── README.md


If images still don’t open after this, the problem is NOT markdown — it’s either:

wrong folder name (Screenshots vs screenshots)

wrong file name (ss1.PNG vs ss1.png)

or images not pushed

No excuses. Now paste THIS EXACT FILE as README.md.

Aproposdrive AWS & DevOps Assignment
Overview

This repository contains my submission for the AWS & DevOps Intern assignment by Aproposdrive Technologies.
The goal was to build a simple application, containerize it using Docker, deploy it on AWS EC2, and configure load balancing and auto scaling with cost optimization.

All steps were executed manually and documented with screenshots.

Task 1: Application (Frontend + Backend + Database)

I created a simple Flask-based user registration application with a MySQL database.
The application accepts user input (name and email) and stores it in the database.

Project structure on local system

User registration page

Form submission success page

Data successfully stored in MySQL database

Task 2: Dockerization

The application and database were containerized using Docker and Docker Compose.
Ports were exposed correctly, and containers were verified to be running.

Docker image created

Running containers using docker ps

Docker Compose configuration

Task 3: AWS EC2 Deployment

A cost-optimized EC2 instance was launched and Docker was installed.
The application containers were then run on the EC2 instance.

EC2 instance running

SSH access to EC2 instance

Docker and Docker Compose installed on EC2

Application directory structure on EC2

Docker containers running on EC2

Task 4: Application Access

The application was accessed using the EC2 public IP address.

Application accessible via EC2 public IP

Task 5: Load Balancer & Auto Scaling

An Application Load Balancer (ALB) and Auto Scaling Group (ASG) were configured to distribute traffic and ensure high availability.

GitHub repository pushed

Application Load Balancer created

Load Balancer listener configuration

Auto Scaling Group created

Auto Scaling instance running

Target group configuration

Free-tier eligible instance type (t2.micro)

Desired capacity set to 1

Task 6: Cost Optimization

Free-tier eligible EC2 instance type used (t2.micro)

Desired capacity kept at 1

Auto Scaling enabled to avoid over-provisioning

Docker used to minimize resource usage

Task 7: Troubleshooting

When the application was not accessible, I verified EC2 security groups and ensured port 5000 was allowed.

When the container was running but the port was unreachable, I checked Docker port mappings using docker ps.

When the target group showed unhealthy, I SSHed into the instance and verified the application response using curl localhost:5000.

Deliverables

Complete working setup

Source code

Screenshots for every major step

Step-by-step execution documentation

Final Notes

This assignment was completed manually to understand real-world AWS and DevOps workflows, including deployment issues and troubleshooting steps.