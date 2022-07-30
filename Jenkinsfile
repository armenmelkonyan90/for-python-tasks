pipeline {
  agent any
     
  triggers{
      GenericTrigger(
         causeString: 'Generic Cause', 
         genericVariables: [
             [defaultValue: '', key: 'base', regexpFilter: '', value: '$.pull_request.base.ref'],
              [defaultValue: '', key: 'ifmarged', regexpFilter: '', value: '$.pull_request.merged']
              ], 
         regexpFilterExpression: 'dev#true', 
         regexpFilterText: '$base#ifmarged', 
         token: '1234', 
         tokenCredentialId: '')
  }
  
    stages {
       when {
             expression { regexpFilterExpression == 'dev#true' }
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
  
