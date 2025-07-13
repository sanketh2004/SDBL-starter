pipeline {
    agent any

    environment {
        // Use pipenv installed for the Jenkins user
        PATH = "/var/lib/jenkins/.local/bin:$PATH"
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    echo "PATH is: $PATH"
                    which pipenv || echo "Pipenv not found!"
                    pipenv --python python3 sync
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
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
                sh '''
                ssh -i /var/lib/jenkins/cred/Sandy.pem \
                    -o "StrictHostKeyChecking no" \
                    ubuntu@13.221.209.31 "mkdir -p /home/ubuntu/sbdl-qa"

                scp -i /var/lib/jenkins/cred/Sandy.pem \
                    -o "StrictHostKeyChecking no" \
                    -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf \
                    ubuntu@13.221.209.31:/home/ubuntu/sbdl-qa
                '''
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh '''
                ssh -i /var/lib/jenkins/cred/Sandy.pem \
                    -o "StrictHostKeyChecking no" \
                    ubuntu@13.221.209.31 "mkdir -p /home/ubuntu/sbdl-prod"

                scp -i /var/lib/jenkins/cred/Sandy.pem \
                    -o "StrictHostKeyChecking no" \
                    -r sbdl.zip log4j.properties sbdl_main.py sbdl_submit.sh conf \
                    ubuntu@13.221.209.31:/home/ubuntu/sbdl-prod
                '''
            }
        }
    }
}
