# Jenkins CI Server Setup (Docker-Native)

This guide will help you set up a Jenkins CI server using Docker on a Linux machine. This approach is portable, easy to maintain, and works well for most modern CI/CD workflows.

---
ansible -h

## 1. Prerequisites
- A Linux server (Ubuntu, Debian, CentOS, etc.)
- Docker installed ([Install Docker](https://docs.docker.com/engine/install/))
- (Optional) Docker Compose installed ([Install Docker Compose](https://docs.docker.com/compose/install/))
- Ports 8080 (Jenkins UI) and 50000 (agent connections) open

---

## 2. Prepare Jenkins Data Directory
Create a directory on your server to persist Jenkins data:

```sh
mkdir -p ~/jenkins/jenkins_home
cd ~/jenkins
```

---

## 3. Create `docker-compose.yml`
Create a file named `docker-compose.yml` in your Jenkins directory with the following content:

```yaml
version: '3.8'
services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - ./jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    restart: unless-stopped
```

---

## 4. Start Jenkins
Run Jenkins in the background:

```sh
docker compose up -d
```

- Jenkins will be available at: `http://your-server-ip:8080`
- The first-time admin password is in `jenkins_home/secrets/initialAdminPassword`

---

## 5. Initial Setup
1. Open Jenkins in your browser.
2. Enter the admin password from the file above.
3. Install recommended plugins.
4. Create your admin user.

---

## 6. Configure Jenkins for Docker Builds
- Install the **Docker** and **Docker Pipeline** plugins.
- You can now run build jobs inside Docker containers for isolation and reproducibility.
- Example: Use `agent { docker { image 'python:3.11' } }` in your Jenkinsfile for Python builds.

---

## 7. Security & Maintenance
- Set up HTTPS (reverse proxy or Jenkins config).
- Regularly update Jenkins and plugins.
- Back up `jenkins_home`.

---

## 8. Example Jenkinsfile (Python Project)
```groovy
pipeline {
  agent {
    docker { image 'python:3.11' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
  }
}
```

---

## References
- [Jenkins Docker Docs](https://www.jenkins.io/doc/book/installing/docker/)
- [Jenkins Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Jenkins Docker Pipeline Plugin](https://plugins.jenkins.io/docker-workflow/)

---

**You now have a robust, Docker-native Jenkins CI server!**
