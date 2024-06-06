pipeline {
    agent any
    
    tools {
        'dependency-check' 'DP-Check'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/junxianyong/JenkinsDependencyCheckTest'
            }
        }
        
        stage('Build') {
            steps {
                echo 'No build step needed'
            }
        }
        
        stage('Dependency Check') {
            steps {
                sh '''
                    mkdir -p dependency-check-report
                    dependency-check.sh --project "JenkinsDependencyCheckTest" --scan . --format "ALL" --out dependency-check-report
                '''
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'dependency-check-report/*', allowEmptyArchive: true
            dependencyCheckPublisher pattern: 'dependency-check-report/dependency-check-report.xml'
        }
    }
}
