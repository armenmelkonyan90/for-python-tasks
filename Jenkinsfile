pipeline {
  agent any
  triggers {
    GenericTrigger(causeString: 'Generic Cause', 
                   genericVariables: [[key: 'COMMIT_HASH', value: '$.head_commit.id']])
  } 
  stages {
    stage("Store commit hash") { 
      steps {
        script {
          try {
            sh """docker exec redis_server redis-cli "set" "BEFORE_TEST" "${COMMIT_HASH}" """
            sh """docker exec redis_server redis-cli "save" """
          }
          catch(Exception err) {
            error("Unable to store commit hash")
          }
        }
      }
    }
    stage('Checkout "Tasks" Repo')  {
      steps {
        script {
          try {
            dir('TasksRepo') {
              git branch: 'main', url: "https://github.com/armenmelkonyan90/for-python-tasks.git"
            }
          }
          catch(Exception err) {
            error("Unable to clone developer's repo")
          }
        }  
      }
    }
    stage("Build & Run Testing Container") { 
      steps {
        sh "docker build -t temp_test_img ."
        sh """docker run --rm --name temp_container temp_test_img > answers.txt""" 
      }  
    }
  }
}
