pipeline {
    agent any

    environment {
        PATH = "/home/ubuntu/.local/bin:$PATH"
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    export PATH=$PATH:/home/ubuntu/.local/bin
                    echo "PATH is: $PATH"
                    which pipenv || echo "Pipenv not found!"
                    pipenv --python python3 sync
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    export PATH=$PATH:/home/ubuntu/.local/bin
                    pipenv run pytest
                '''
            }
        }
        stage('Package') {
            when {
                anyOf { branch "master"; branch "release" }
            }
            steps {
                sh 'zip -r sbdl.zip lib'
            }
        }
        stage('Release') {
            when {
                branch 'release'
            }
            steps {
                sh """
                scp -i /var/lib/jenkins/cred/Sandy.pem \
                    -o 'StrictHostKeyChecking no' \
                    -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf \
                    ubuntu@13.221.209.31:/home/ubuntu/sbdl-qa
                """
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh """
                scp -i /var/lib/jenkins/cred/Sandy.pem \
                    -o 'StrictHostKeyChecking no' \
                    -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf \
                    ubuntu@13.221.209.31:/home/ubuntu/sbdl-prod
                """
            }
        }
    }
}


