pipeline {
  agent any
     
    pipelineTriggers([
      GenericTrigger(
         causeString: 'Generic Cause', 
         genericVariables: [
             [defaultValue: '', key: 'ref', regexpFilter: '', value: '$.ref']
              ], 
         regexpFilterExpression: '', 
         regexpFilterText: '', 
         token: '1234', 
         tokenCredentialId: '')])])
  
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
  
