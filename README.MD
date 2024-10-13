
# Creation Tests Environment

Execute ``docker compose -f docker-compose.core.yaml up -d --build``
It will deploy:

## 1. Database Service
- **Container Name:** `db`
- **Image:** Custom PostgreSQL image built from `db.Dockerfile`
- **Environment Variables:** Loaded from `pgsql.env`
- **Volume:** Persistent data stored in `postgres-db-volume`
- **Network:** Connected to `cicd-demo`

## 2. Gitea Server
- **Container Name:** `gitea-server`
- **Image:** `gitea/gitea`
- **Environment Variables:** Loaded from `gitea.env`
- **Volumes:**
  - Gitea data stored in `./gitea`
  - Timezone configuration from `/etc/timezone`
  - Local time configuration from `/etc/localtime`
- **Ports:**
  - HTTP: `3000`
  - SSH: `22`
- **Network:** Connected to `cicd-demo`
- **Depends on:** `db`

## 3. SonarQube
- **Container Name:** `sonarqube`
- **Image:** `sonarqube:community`
- **Environment Variables:** Loaded from `sonar.env`
- **Volumes:**
  - Extensions: `sonarqube_extensions`
  - Logs: `sonarqube_logs`
  - Temporary files: `sonarqube_temp`
  - Data: `/opt/sonarqube/data`
- **Port:** `9000`
- **Network:** Connected to `cicd-demo`
- **Depends on:** `db`
- **Resource Limits:** 
  - CPUs: `0.5`
  - Memory Limit: `4096M`
  - Memory Reservation: `4096M`

## 4. SSH Server
- **Container Name:** `ssh-server`
- **Image:** `lscr.io/linuxserver/openssh-server:latest`
- **Environment Variables:**
  - `PUID=1000`
  - `PGID=1000`
  - `TZ=Etc/UTC`
  - `PASSWORD_ACCESS=true`
  - `USER_PASSWORD=sshpass`
  - `USER_NAME=sshuser`
- **Volumes:**
  - Configuration: `./ssh-server/config`
  - Web content: `./web_content`
- **Port:** `2222`
- **Network:** Connected to `cicd-demo`

## 5. Web Beta
- **Container Name:** `web-beta`
- **Image:** `nginx`
- **Volume:** Web content stored in `./web_content/web_beta`
- **Network:** Connected to `cicd-demo`

## 6. Web Production
- **Container Name:** `web-prod`
- **Image:** `nginx`
- **Volume:** Web content stored in `./web_content/web_prod`
- **Network:** Connected to `cicd-demo`

## 7. Reverse Proxy
- **Container Name:** `r_proxy`
- **Image:** `nginx`
- **Volume:** Nginx configuration stored in `./r_proxy`
- **Port:** `80`
- **Network:** Connected to `cicd-demo`

---

### Volumes
- `postgres-db-volume`
- `sonarqube_extensions`
- `sonarqube_logs`
- `sonarqube_temp`

### Network
- `cicd-demo`

# Set up Gitea (main CICD tool)

1. According to [Gitea - modern lightweight self-hosted git service](https://site.extadmin.space/posts/how-to/gitea-modern-lightweight-self-hosted-git-service/), set up Gitea and add a act_runner (runtime). OAuth is not required. 