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
                sh 'mkdir build'

                sh """
                    cd build &&
                    cmake    -DCMAKE_BUILD_TYPE=Debug
                             -DSCORUM_LIVE_TESTNET=OFF
                             -DSCORUM_LOW_MEMORY_NODE=OFF
                             -DSCORUM_CLEAR_VOTES=ON
                             -DSCORUM_SKIP_BY_TX_ID=ON
                             -DENABLE_COVERAGE_TESTING=ON
                             ..
                   """

                sh 'cd build && make -j$(nproc) all'
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