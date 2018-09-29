#!groovy
pipeline {
    agent {
        docker {
            image 'alexplevako/build_image:0.0.1'
            label "jenkins-agent-azure"
        }
    }
    stages {
        parallel {
            stage('Build Debug') {
                steps {
                    sh 'mkdir build-debug'
                    sh "cd build-debug && ../build.py run_cmake_debug"
                    sh 'cd build-debug && make -j$(nproc) all'
                }
            }

            stage('Build default') {
                steps {
                    sh 'mkdir build-default'
                    sh "cd build-default && ../build.py run_cmake_release_default"
                    sh 'cd build-default && make -j$(nproc) all'
                }
            }

            stage('Build full') {
                steps {
                    sh 'mkdir build-full'
                    sh "cd build-full && ../build.py run_cmake_release_full"
                    sh 'cd build-full && make -j$(nproc) all'
                }
            }
        }

        // stage('Test') {
        //     steps {
        //         sh './build/libraries/chainbase/test/chainbase_test'
        //         sh './build/tests/utests/utests'
        //         sh './build/tests/chain_tests/chain_tests'
        //         sh './build/tests/wallet_tests/wallet_tests'
        //     }
        // }
    }
}