pipeline {
  agent any
  triggers {
    GenericTrigger(
        causeString: 'Triggered from release/prerelease', 
        genericVariables: [
            [defaultValue: '', key: 'ref', regexpFilter: '', value: '$ref']
            ],
        token: '1234', 
        tokenCredentialId: ''
             )
  }
  
  stages {
      stage('Release') {
        when {
             expression { ref == 'refs/heads/main' }
         }
         steps {
             sh "echo 'hello world main branch1'"  
         }
      }
   }
}
  
