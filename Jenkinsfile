pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "bash test.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifaces:"htmlcov/*"
        }
    }
}