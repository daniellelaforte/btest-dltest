pipeline {
   agent any
   stages {   
      stage('test PythonEnv') {
         withPythonEnv('python3') {
               sh 'pip install requirements.txt'
         }
      } 
      stage('setup') {
         steps {
            browserstack(credentialsId: 'b894af2b-2e70-4686-ae0e-1f927fd13928') {
               sh 'browserstack-sdk python3 ./python-selenium-browserstack/tests/test.py'
            }
            browserStackReportPublisher 'automate'
         }
      }
    }
  }
