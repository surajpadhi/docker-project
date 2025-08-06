Dockerized Python Service with Nginx
This project deploys a simple Python Flask app using Docker Compose, with Nginx for load balancing, rate limiting, and basic authentication.

Features
Two Python service instances

Nginx reverse proxy (port 8080)

Round-robin load balancing

10 req/sec rate limit

Basic authentication

Prerequisites
Docker, Docker Compose, and httpd-tools on your Red Hat EC2 instance.

Project Structure
.
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/
│   ├── nginx.conf
│   └── .htpasswd
├── docker-compose.yml
└── README.md

Deployment Steps
Follow these steps on your EC2 instance:

1. Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Generate .htpasswd
Create this file in nginx/ for Nginx auth (e.g., admin:your_password).

cd nginx/
sudo yum install -y httpd-tools
htpasswd -c .htpasswd admin # Enter password
cd ..

3. Build & Run
docker-compose up --build -d

4. Verify Status
docker-compose ps

Testing
Replace <YOUR_EC2_PUBLIC_IP> with your EC2 instance's IP.

1. Basic Authentication
curl -u admin:your_password http://<YOUR_EC2_PUBLIC_IP>:8080/

Expected: Hello from Python service instance: <container_id>!

2. Load Balancing
for i in {1..10}; do curl -u admin:your_password http://<YOUR_EC2_PUBLIC_IP>:8080/; sleep 0.5; done

Expected: Alternating container IDs.

3. Rate Limiting
for i in {1..15}; do curl -s -o /dev/null -w "%{http_code}\n" -u admin:your_password http://<YOUR_EC2_PUBLIC_IP>:8080/; done

Expected: Mix of 200 and 429 status codes.

Stop & Remove
docker-compose down
docker-compose down --rmi all

Troubleshooting
docker-compose up fails: Check Docker status, user permissions, YAML syntax.

Cannot access: Check EC2 Security Group (port 8080), Nginx container status, Nginx logs.

Auth/Rate Limit issues: Verify nginx.conf, .htpasswd.

Python not responding: Check Python service logs.

Future Enhancements
HTTPS, health checks, advanced load balancing, logging, monitoring, secrets management, CI/CD.