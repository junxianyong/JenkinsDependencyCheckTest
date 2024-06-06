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
                // Assuming there is no build step needed, as there is no build tool specified
                echo 'No build step needed'
            }
        }
        
        stage('Dependency Check') {
            steps {
                dependencyCheckAnalyzer odcInstallation: 'DP-Check', additionalArguments: '--format HTML'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: '**/dependency-check-report.html', allowEmptyArchive: true
            dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        }
    }
}
