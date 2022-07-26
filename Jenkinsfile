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
      
      stage('Release') {
        when {
             expression { ref == 'refs/heads/dev' }
         }
        
         steps {
             sh "echo 'hello world main branch1'"  
         }
      }
      stage ("test") {
        when {
             expression { ref == 'refs/heads/dev' }
         }
        steps {
          sh " echo 'test stage'"
        } 
      }
  }
}
  
