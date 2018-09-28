#!groovy
pipeline {
    agent {
        label "jenkins-agent-azure"
        docker { image 'node:7-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'node --version'
            }
        }
    }
    // post {
    //     success {
    //         sh 'ciscripts/buildsuccess.sh'
    //     }
    //     failure {
    //         sh 'ciscripts/buildfailure.sh'
    //         slackSend (color: '#ff0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    //     }
    // }
}
