pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage started...'
                sh 'ls -la'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 test_calculator.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage completed (dummy deploy for now)'
            }
        }
    }
}
