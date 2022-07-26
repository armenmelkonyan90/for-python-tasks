pipeline {
  agent any
  triggers {
    GenericTrigger(
        causeString: 'Triggered from release/prerelease', 
        genericVariables: [
            [defaultValue: '', key: 'ref', regexpFilter: '', value: '$.ref']
            ],
             )
  }
  
  stages {
      stage('Release') {
        when {
             expression { ref == 'main' }
         }
         steps {
             sh "echo 'hello world main branch1'"  
         }
      }
   }
}
  
