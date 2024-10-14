
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

1. Follow to http://localhost:3000

2. In the **Initial Configuration** page find out **Optional settings -> Administrator Account Settings** section and expand it. Fill up the gaps
    > E.g.  
    >   Administrator Username:  *gitea-admin*  
    >   Email Address:  *gitea-admin@example.com*  
    >   Password:  *Pa55w0rD!!*  
    >   Confirm Password:  *Pa55w0rD!!*

And Press **Install**

3. At the right top corner, press on the *account* button and sellect **Site Administration*

4. In the *Admin Settings* menu choose **Actions -> Runners** section; and press the **Create new Runner** button. Copy a **Registration token**. Then bring back to codes folder, find ``act_runner.env`` and insert the token as value ``GITEA_RUNNER_REGISTRATION_TOKEN="ReplaceOnRgistrationToken"``

5. Execute ``docker compose -f docker-compose.act_runner.yaml up -d`` in the repo's root for act-runner deploy.

6. On the http://localhost:3000/admin/actions/runners you have to see the added runner in **Idle** status.

# Set up SonarQube

1. Follow to http://localhost:9000 and sign-in with credentials *admin* *admin*, then change pssword e.g. ``Pa55w0rD!!sonar``.

2. Create a new local project

    > Project display name: *DemoProject*  
    > Project key: *DemoProject*  
    > Main branch name: *main*  

Then press **Next**, select **Use the global setting** and click on **Create Project**

3. In the *Analys method* select **With GitHub Ations**. Generate token and save it for future. Follow the instructions.

    > For example  
    > sqp_917258c6705f366b62b5ab521a199a1c4011e9cb  
    > 

# Create a local repository and first action

1. Go back to http://http://localhost:3000/ and create a new one 
  > E.g. **Repository Name** *DemoProject*  

2. Clone the repo to the local maschine and create ``./.gitea/workflows/main.yaml``; insert content ``/actions/main.yaml`` file into it. Additional create ``sonar-project.properties`` file in root folder of your repo with ``sonar.projectKey=DemoProject`` content.

3. Go into the ropsitory settings [**Actions -> Secrets**](http://localhost:3000/gitea-admin/DemoProject/settings/actions/secrets) and create following 
  
  > SONAR_TOKEN=sqp_917258c6705f366b62b5ab521a199a1c4011e9cb  
  > SONAR_HOST_URL=http://localhost:9000  
  > SONAR_PROJECT_KEY=DemoProject  
  > SSH_PASSWORD=sshpass  
  > SSH_USER=sshuser

4. Push repo changes to the gitea. Check actions.


