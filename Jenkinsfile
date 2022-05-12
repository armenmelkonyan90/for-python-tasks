
pipeline {
  agent any
  
  stages {
      stage('Release') {
          
         steps {
             
             step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartService', scale: 1, service: 'server'], useCustomDockerComposeFile: true])
  
         }
      }
      
   }
  
