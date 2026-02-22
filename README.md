![CI](https://github.com/codewithmazi/OA-devops-intern-final/actions/workflows/ci.yml/badge.svg)
# OA-devops-intern-final  DevOps Intern Final Assessment

Name: Oluwanifemi Awopetu
Date: 22 Feb 2026

This repository implements a simple DevOps workflow involving Git/GitHub, Linux scripting, Docker, CI/CD with GitHub Actions, Nomad, and basic Loki monitoring notes.


## Docker

Build:
```bash
docker build -t devops-hello .

docker run --rm devops-hello


## Nomad Deployment

1. Ensure `devops-hello:latest` Docker image is available on Nomad server.
2. Run: `nomad job run nomad/hello.nomad`
3. Check status: `nomad job status hello-devops`


## Loki Monitoring

See monitoring/loki_setup.txt for local Docker setup.
screenshot: 
![alt text](image-1.png)


## MLflow experiment
screenshot:
![alt text](<Screenshot 2026-02-22 220735.png>)


##other screenshots
![alt text](<Screenshot 2026-02-22 205126.png>)

![alt text](<Screenshot 2026-02-22 205217.png>)

![alt text](<Screenshot 2026-02-22 211141.png>)