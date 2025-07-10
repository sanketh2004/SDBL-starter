pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               echo "🔨 Building the project..."
               sh 'pipenv --python python3 sync'
            }
        }
        stage('Test') {
            steps {
               echo "🧪 Running tests..."
               sh 'pipenv run pytest'
            }
        }
        stage('Package') {
            steps {
               echo "📦 Packaging files..."
               sh 'zip -r sbdl.zip lib'
            }
        }
    }
}

