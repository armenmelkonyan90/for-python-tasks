pipeline {
  agent any
     
  triggers{
      GenericTrigger(
         causeString: 'Generic Cause', 
         genericVariables: [
             [defaultValue: '', key: 'ref', regexpFilter: '', value: '$.ref']
              ], 
         regexpFilterExpression: '', 
         regexpFilterText: '', 
         token: '1234', 
         tokenCredentialId: '')
  }
  
    stages {
      when {
             expression { ref == 'refs/heads/main' }
         }
      stage('Release') {
        
         steps {
             sh "echo 'hello world main branch1'"  
         }
      }
      stage ("test") {
        steps {
          sh " echo 'test stage'"
        } 
      }
  }
}
  
