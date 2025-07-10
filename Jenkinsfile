pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               bat 'pipenv --python python3 sync'
            }
        }
        stage('Test') {
            steps {
               bat 'pipenv run pytest'
            }
        }
        stage('Package') {
            steps {
               bat 'powershell Compress-Archive -Path lib -DestinationPath sbdl.zip'
            }
        }
    }
}

