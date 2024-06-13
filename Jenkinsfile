pipeline {
    agent any

    tools {
        git 'Default' // Ensure 'Default' is defined in Jenkins Global Tool Configuration
        'dependency-check' 'DP-Check' // Correct tool type for OWASP Dependency Check
    }

    environment {
        NVD_API_KEY = credentials('nvd') // Assuming you stored the API key in Jenkins Credentials
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/junxianyong/JenkinsDependencyCheckTest'
            }
        }

        stage('OWASP DependencyCheck') {
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML --nvdApiKey $NVD_API_KEY --enableExperimental', odcInstallation: 'DP-Check'
            }
        }

        stage('Safety Check') {
            steps {
                sh 'pip install safety'
                sh 'safety check -r requirements.txt --full-report > safety-report.txt'
                archiveArtifacts artifacts: 'safety-report.txt'
            }
        }
    }

    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
        always {
            archiveArtifacts artifacts: '**/dependency-check-report.html'
        }
    }
}
