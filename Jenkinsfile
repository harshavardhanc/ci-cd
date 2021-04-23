pipeline {
  options {
    buildDiscarder(
        logRotator(
            // number of build logs to keep
            numToKeepStr:'1',
            // number of builds have their artifacts kept
            artifactNumToKeepStr: '1'
        )
    )
  }

   parameters {
      string(name: 'image_name', defaultValue: 'harshac/python_webapp', description: 'Bulid Image Name', )
   }

    agent any 
    stages {
        stage('CleanWorkspace') {
            steps {
              cleanWs()
            }

        }

        stage('Build') {
            steps {
                sh'''
                  tag=$(git rev-parse --short HEAD)
                  docker build -t ${image_name}:${tag} .
                  echo "${image_name}:${tag}" > artifact_metadata
                  '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'artifact_metadata', onlyIfSuccessful: true
        }
    }
}
