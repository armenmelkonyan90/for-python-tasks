pipeline {
  agent any
  triggers {
    GenericTrigger(
        causeString: 'Triggered from release/prerelease', 
        genericVariables: [
            [defaultValue: '', key: 'branch', regexpFilter: '', value: '$.ref']
            ],
             )
  }
  
  stages {
      stage('Release') {
        when {
             expression {branch == 'refs/heads/main' }
         }
         steps {
             sh "echo 'hello world main branch'"  
         }
      }
   }
}
  
