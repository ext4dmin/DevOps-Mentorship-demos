
## Creation Tests Environment

Execute ``docker compose -f docker-compose.core.yaml up -d --build``
It deploys:
- DB: postgresql
- Git: gitea
- Source check: sonarqube (execute before deploying ``sudo su;echo "vm.max_map_count=262144" >> /etc/sysctl.conf;sudo sysctl -p``)
- Webservers: nginx [-prod; -beta]
- Reverse Proxy: nginx 

## Set up Gitea

As CICD tool we uss Gitea actions

1. According to [Gitea - modern lightweight self-hosted git service](https://site.extadmin.space/posts/how-to/gitea-modern-lightweight-self-hosted-git-service/), set up Gitea and add a act_runner (runtime). OAuth is not required. 