#!groovy
pipeline {
    agent {
        docker {
            image 'alexplevako/build_image:0.0.1'
            label "jenkins-agent-azure"
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'cmake .'
                sh 'make -j$(nproc) scorumd'
            }
        }
    }
}