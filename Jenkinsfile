pipeline {
    agent any
    
    stages {
        stage("Prod") {
            steps {
                sh "docker build -t my-app  -f Python/Homework1/Dockerfile ."
                sh "docker run -p 5050:5050 --name flaskapp -v /var/run/docker.sock:/var/run/docker.sock my-app"
            }
        }
    }
    post {
        failure {
            steps {
                sh "docker container rm -f flaskapp"   
            }
        }
    }
}
