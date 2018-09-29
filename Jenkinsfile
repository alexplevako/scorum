#!groovy
pipeline {
    agent {
        docker {
            image 'alexplevako/build_image:0.0.1'
            label "jenkins-agent-azure"
        }
    }
    stages {
        stage("Build") {
            parallel {
                stage('Debug') {
                    steps {
                        sh 'mkdir build-debug'
                        sh "cd build-debug && ../build.py run_cmake_debug"
                        sh 'cd build-debug && make -j$(nproc) all'
                    }
                }

                stage('Release default') {
                    steps {
                        sh 'mkdir build-default'
                        sh "cd build-default && ../build.py run_cmake_release_default"
                        sh 'cd build-default && make -j$(nproc) all'
                    }
                }

                stage('Release full') {
                    steps {
                        sh 'mkdir build-full'
                        sh "cd build-full && ../build.py run_cmake_release_full"
                        sh 'cd build-full && make -j$(nproc) all'
                    }
                }
            }
        }
    }
}