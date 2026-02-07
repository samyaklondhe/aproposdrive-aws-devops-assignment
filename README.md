Aproposdrive AWS & DevOps Assignment

This repository contains my submission for the AWS & DevOps Intern assignment provided by Aproposdrive Technologies Pvt. Ltd.
The goal of this assignment was to design, containerize, deploy, and scale a simple application on AWS using best practices while keeping the setup cost-optimized.

Task 1 – Application Setup (Frontend + Backend + Database)

I created a simple Flask-based web application with a user registration form.
The application stores submitted user data in a MySQL database.

The project includes:

Flask backend

HTML frontend

MySQL database connection

Project structure on local machine:

Screenshot:


Task 2 – Dockerization

Docker was used to containerize both the Flask application and the MySQL database.

Steps performed:

Created a Dockerfile for the Flask app

Created a docker-compose.yml to run app and database together

Exposed required ports

Verified containers restart automatically

Docker image creation:

Screenshot:


Running containers check:

Screenshot:


Task 3 – AWS EC2 Deployment

An EC2 instance was launched using a free-tier eligible instance type.

The following actions were performed:

Launched EC2 instance

Connected using SSH

Installed Docker and Docker Compose

Copied application files to EC2

Ran containers using Docker Compose

EC2 instance running:

Screenshot:


SSH connection into EC2:

Screenshot:


Docker & Docker Compose versions on EC2:

Screenshot:


Project directory structure on EC2:

Screenshot:


Task 4 – Application Access

The application was successfully accessed using the EC2 public IP address.

Application landing page:

Screenshot:


The MySQL database runs inside a Docker container, and data submitted through the UI is stored inside the database container.

Task 5 – Load Balancer & Auto Scaling

To make the setup scalable and production-like, the following AWS services were configured:

Application Load Balancer (ALB)

Target Group

Launch Template

Auto Scaling Group (ASG)

The application listens on port 5000, and the ALB routes traffic to healthy instances.

Application Load Balancer created:

Screenshot:


ALB Listener configuration:

Screenshot:


Auto Scaling Group created:

Screenshot:


Auto Scaling EC2 instance running:

Screenshot:


Target Group health check status:

Screenshot:


Free-tier instance type used (t2.micro):

Screenshot:


Desired capacity set to 1 to avoid over-provisioning:

Screenshot:


Task 6 – Cost Optimization

Cost optimization was ensured by:

Using free-tier eligible instance types

Keeping desired capacity to 1

Using Auto Scaling to scale only when required

Avoiding unnecessary AWS resources

Task 7 – Troubleshooting (Explanation)

During the setup, the following issues were encountered and resolved:

1. Application not accessible
This happened when security groups did not allow inbound traffic on port 5000.
Fix: Updated security group rules to allow traffic from ALB and public access where required.

2. Container running but port not reachable
Containers were running, but the application was not accessible externally.
Fix: Ensured correct port mapping (5000:5000) and verified container logs.

3. ALB health check failures
Initial health check failures occurred because the application took time to start.
Fix: Adjusted health check path and allowed sufficient warm-up time.

Git Repository

All application code, Docker configuration files, and screenshots are stored in this repository for verification.

Git push confirmation:

Screenshot:


Conclusion

This assignment demonstrates:

Application containerization using Docker

Deployment on AWS EC2

Load balancing and auto scaling using AWS services

Cost optimization and troubleshooting skills

The setup follows a clean, practical approach suitable for real-world DevOps workflows.