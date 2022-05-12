
pipeline {
  agent any
  
  stages {
      stage('Release') {
          
         steps {
             
             dockerComposeUp("prod", "False")
         }
      }
      
   }
  
