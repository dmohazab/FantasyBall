# FantasyBall
Back-end Basketball API being created

To Run:
- 
- Run `docker-compose up`, injecting required environment variables at runtime 
(build-time will compile but endpoints will fail) <br>

- If manual docker set-up is desired, run: <br>
`docker build -t waitress_server:latest .` <br>
`$ docker run -d -p 5000:5000 waitress_server:latest`


![Back-end Architecture](readme_util/architecture.png)
- Deploy on AWS using RDS to set up live MySQL DB instance
- Use Amazon EKS for deployment (TODO: Set up charts and jobs)

Microservice Connection Ideas (TODO)
- 
- Sell API access with API keys (on rapidapi)
- Fantasy point prediction, including ML layer and front-end
- Actual NBA Fantasy Application
