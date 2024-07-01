pipeline {
    agent any

    tools {
        git 'Default'
        'org.jenkinsci.plugins.DependencyCheck.tools.DependencyCheckInstallation' 'DP-Check'
    }

    environment {
        NVD_API_KEY = credentials('nvd')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/junxianyong/JenkinsDependencyCheckTest'
            }
        }

        stage('Verify Dependency Check Installation') {
            steps {
                // Verify the tool installation directory and permissions
                sh 'ls -l /var/jenkins_home/tools/org.jenkinsci.plugins.DependencyCheck.tools.DependencyCheckInstallation/dependency-check'
                sh 'which dependency-check.sh' // Verify the tool is in the PATH
            }
        }

        stage('OWASP DependencyCheck') {
            steps {
                // Add debug information to check environment variables and paths
                sh 'env'
                sh 'dependency-check.sh --version'

                dependencyCheck additionalArguments: '--scan . --project "Dependency Check Test Project" --format HTML --format XML --nvdApiKey $NVD_API_KEY --enableExperimental --disableOssIndex --out .', odcInstallation: 'DP-Check'
                archiveArtifacts artifacts: 'dependency-check-report.html, dependency-check-report.xml'
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
