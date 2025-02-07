pipeline {
   agent any
   stages {
      stage('version') {
         steps {
          	sh 'python3 --version'
            sh 'virtualenv venv --distribute'
            sh '. venv/bin/activate'
            sh 'pip install -r requirements.txt'
         }
      }      
      stage('setup') {
         steps {
            browserstack(credentialsId: 'b894af2b-2e70-4686-ae0e-1f927fd13928') {
               sh 'python3 ./python-selenium-browserstack/tests/test.py'
            }
            browserStackReportPublisher 'automate'
         }
      }
    }
  }
