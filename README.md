```
project-root
├── backend
│   ├── app
│   │   ├── models
│   │   │   ├── llama_fine_tuning
│   │   │   │   ├── config.json
│   │   │   │   ├── train.py
│   │   │   │   ├── utils.py
│   │   │   └── inference.py
│   │   ├── routers
│   │   │   ├── chat.py
│   │   │   ├── analytics.py
│   │   ├── services
│   │   │   ├── linking_methods.py
│   │   │   ├── analytics.py
│   │   ├── utils
│   │   │   ├── database.py
│   │   │   ├── settings.py
│   │   │   ├── logging_config.py
│   ├── tests
│   │   ├── test_endpoints.py
│   │   ├── test_services.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── Chatbot.jsx
│   │   │   ├── Dashboard.jsx
│   │   ├── hooks
│   │   ├── App.jsx
│   │   ├── index.js
│   ├── public
│   │   ├── index.html
│   ├── package.json
│   ├── webpack.config.js
│   ├── Dockerfile
├── data
│   ├── raw
│   ├── processed
│   ├── logs
├── analytics
│   ├── dashboards
│   │   ├── user_performance.pbix
│   │   ├── tableau_dashboard.twbx
├── ci_cd
│   ├── .github
│   │   ├── workflows
│   │   │   ├── backend.yml
│   │   │   ├── frontend.yml
├── deployment
│   ├── aws
│   │   ├── ec2_setup.sh
│   ├── terraform
├── docs
│   ├── project_overview.md
│   ├── api_docs.md
│   ├── architecture_diagram.png
├── README.md
```