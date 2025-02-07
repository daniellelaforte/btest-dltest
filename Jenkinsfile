pipeline {
   agent {
        docker { image 'python:3' }
    }
   stages {
      stage('setup') {
         steps {
            browserstack(credentialsId: 'b894af2b-2e70-4686-ae0e-1f927fd13928') {
                     sh """
          				pip install -r requirements.txt
          				"""
          			   sh """
          			 	browserstack-sdk python3 ./python-selenium-browserstack/tests/test.py
          			 	"""
            }
            browserStackReportPublisher 'automate'
         }
      }
    }
  }
