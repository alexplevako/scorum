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
                sh 'pwd'
                sh 'mkdir build && cd build'
                sh 'pwd'
                sh './build.py run_cmake_debug'
                sh 'make -j$(nproc) all'
            }
        }
        stage('Test') {
            steps {
                sh './build/libraries/chainbase/test/chainbase_test'
                sh './build/tests/utests/utests'
                sh './build/tests/chain_tests/chain_tests'
                sh './build/tests/wallet_tests/wallet_tests'
            }
        }
    }
}