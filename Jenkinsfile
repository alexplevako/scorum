#!groovy
pipeline {
    agent {
        docker {
            image 'phusion/baseimage:0.9.19'
            label "jenkins-agent-azure"
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ps -ef'
                sh 'ls -la'
            }
        }
    }
}
