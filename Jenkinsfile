#!groovy
pipeline {
    agent {
        label "jenkins-agent-azure"
        docker { image 'node:7-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ps -ef'
            }
        }
    }
}
