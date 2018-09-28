#!groovy
pipeline {
    agent {
        label "jenkins-agent-azure"
    }
    stages {
        stage("Get submodules") {
            steps {
                sh 'git submodule update --init --recursive'
            }
        }
        stage('Build') {
            steps {
                sh 'ps -ef'
            }
        }
    }
}
