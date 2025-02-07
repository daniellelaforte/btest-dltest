pipeline {
   agent any
   stages {   
      stage('test PythonEnv') {
         steps {
            withPythonEnv('python3') {
               sh 'pip install -r requirements.txt'
            }
         }
      } 
      stage('setup') {
         steps {
            withPythonEnv('python3') {
               browserstack(credentialsId: 'b894af2b-2e70-4686-ae0e-1f927fd13928') {
                  sh 'python3 ./python-selenium-browserstack/tests/test.py'
               }
               browserStackReportPublisher 'automate'
            }
         }
      }
    }
  }
