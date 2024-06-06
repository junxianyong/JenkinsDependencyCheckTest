pipeline {
    agent any
    
    tools {
        // Install the OWASP Dependency Check tool
        dependencyCheck 'OWASP_Dependency-Check_Vulnerabilities'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git 'https://github.com/0xprime/JenkinsDependencyCheckTest'
            }
        }
        
        stage('Dependency Check') {
            steps {
                // Run OWASP Dependency Check
                dependencyCheckAnalyzer datadir: '', hintsFile: '', outdir: '', scanpath: '**/*.jar,**/*.war,**/*.zip'
            }
        }
    }
    
    post {
        always {
            // Archive the dependency-check report
            archiveArtifacts artifacts: '**/dependency-check-report.html', allowEmptyArchive: true
            // Publish the dependency-check report
            dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        }
    }
}