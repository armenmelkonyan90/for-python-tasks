pipeline {
    agent any
    
    stages {
        stage("Prod") {
            steps {
                sh "docker build -t my-app  -f Python/Homework1 ."
                sh "docker run -p 5050:5050 my-app"
            }
        }
    }
}
