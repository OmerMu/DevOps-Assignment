pipeline {
    agent any

    parameters {
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Environment: dev/test/prod')
    }

    stages {
        stage('Validate ENV') {
            steps {
                script {
                    // Validate the ENVIRONMENT parameter
                    if (!['dev','test','prod'].contains(params.ENVIRONMENT)) {
                        error "Invalid ENVIRONMENT value: ${params.ENVIRONMENT}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building for environment: ${params.ENVIRONMENT}"
            }
        }

        stage('Generate HTML Report') {
            steps {
                script {
                    bat '''
                      echo "<html><head><title>Build Report</title></head><body>" > build_report.html
                      echo "<h1>Build Results</h1>" >> build_report.html
                      echo "<p>params.Environment chosen: ${params.ENVIRONMENT}</p>" >> build_report.html
                      echo "<p>View the link to results here: <a href='http://example.com'>Check results</a></p>" >> build_report.html
                      echo "</body></html>" >> build_report.html
                    '''
                }
                archiveArtifacts artifacts: 'build_report.html', fingerprint: true
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'build_report.html',
                    reportName: 'Build Report'
                ])
            }
        }
    }

    post {
        success {
            echo "Build succeeded! Check the HTML report."
        }
        failure {
            echo "Build failed. Check logs and report (if generated)."
        }
    }
}
