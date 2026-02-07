# Aproposdrive AWS & DevOps Assignment

This repository contains my submission for the **AWS & DevOps Intern assignment** provided by **Aproposdrive Technologies Pvt. Ltd.**

The assignment was completed step by step as per the given task flow, starting from application development to AWS deployment, load balancing, auto scaling, and basic cost optimization.

---

## Task 1: Application (Frontend + Backend + Database)

I created a simple Flask-based user registration application.  
The application collects user details and stores them in a MySQL database.

### Application project structure (local system)
![SS1](screenshots/ss1.png)

### User registration page
![SS2](screenshots/ss2.png)

### Form submission success page
![SS3](screenshots/ss3.png)

### Data stored successfully in MySQL database
![SS4](screenshots/ss4.png)

---

## Task 2: Docker

The application and database were containerized using Docker and Docker Compose.  
Required ports were exposed and containers were verified to be running.

### Docker image created
![SS5](screenshots/ss5.png)

### Running containers (`docker ps`)
![SS6](screenshots/ss6.png)

### Docker Compose configuration
![SS7](screenshots/ss7.png)

---

## Task 3: AWS EC2 Deployment

A cost-optimized EC2 instance was launched and Docker was installed.  
The Dockerized application was deployed on the EC2 instance.

### EC2 instance running
![SS8](screenshots/ss8.png)

### SSH into EC2 instance
![SS9](screenshots/ss9.png)

### Docker and Docker Compose installed on EC2
![SS10](screenshots/ss10.png)

### Application directory structure on EC2
![SS11](screenshots/ss11.png)

### Docker containers running on EC2
![SS13](screenshots/ss13.png)

---

## Task 4: Application Access

The application was accessed using the **EC2 public IP address**.

### Application accessible via public IP
![SS14](screenshots/ss14.png)

---

## Task 5: Load Balancer & Auto Scaling

An Application Load Balancer (ALB) and Auto Scaling Group (ASG) were configured to distribute traffic and maintain availability.

### Code pushed to GitHub repository
![SS15](screenshots/ss15.png)

### Application Load Balancer created
![SS16](screenshots/ss16.png)

### Load Balancer listener configuration
![SS17](screenshots/ss17.png)

### Auto Scaling Group created
![SS18](screenshots/ss18.png)

### Auto Scaling instance running
![SS19](screenshots/ss19.png)

### Target group configuration
![SS20](screenshots/ss20.png)

### Free-tier eligible instance type (t2.micro)
![SS21](screenshots/ss21.png)

### Desired capacity set to 1
![SS22](screenshots/ss22.png)

---

## Task 6: Cost Optimization

- Free-tier eligible instance type (t2.micro)
- Desired capacity kept at minimum (1)
- Auto Scaling enabled to avoid over-provisioning
- Docker used to reduce resource usage

---

## Task 7: Troubleshooting (Manual Explanation)

- When the application was not accessible, security group rules were verified to allow required ports.
- When containers were running but the port was unreachable, Docker port mappings were checked using `docker ps`.
- When the target group showed unhealthy status, the application was tested locally on the instance using `curl localhost:5000`.

---

## Conclusion

This assignment helped me gain hands-on experience with AWS EC2, Docker, Load Balancer, Auto Scaling, and real-world troubleshooting.  
All tasks were completed manually following the provided requirements.

---

**Repository submitted as per instructions.**
