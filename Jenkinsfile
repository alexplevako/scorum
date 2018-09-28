#!groovy
pipeline {
    agent {
        docker {
            image 'node:7-alpine'
            label "jenkins-agent-azure"
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ps -ef'
            }
        }
    }
}
