pipeline {
  agent any
     
  triggers{
      GenericTrigger(
         causeString: 'Generic Cause', 
         genericVariables: [
             [defaultValue: '', key: 'base', regexpFilter: '', value: '$.pull_request.base.ref'],
              [defaultValue: '', key: 'ifmarged', regexpFilter: '', value: '$.pull_request.merged']
              ], 
         regexpFilterExpression: '', 
         regexpFilterText: '', 
         token: '1234', 
         tokenCredentialId: '')
  }
  
    stages {
      
      
      stage('Release') {
          when {
             expression { base == 'dev' && ifmerged == true }
         }
        
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
  
