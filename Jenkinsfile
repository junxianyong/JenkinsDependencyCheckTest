pipeline {
    agent any
    
    tools {
        dependencyCheck 'OWASP_Dependency-Check_Vulnerabilities'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/0xprime/JenkinsDependencyCheckTest'
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
                dependencyCheck additionalArguments: '--format HTML'
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