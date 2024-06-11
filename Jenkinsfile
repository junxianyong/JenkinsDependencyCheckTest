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
        
        stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
		}
	}	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}