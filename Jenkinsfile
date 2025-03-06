pipeline {
    agent any

    parameters {
        string(name: 'NUMBER', defaultValue: '12321', description: 'Enter a number to check if it is a palindrome')
    }

    stages {
        stage('Copy .env to Jenkins Workspace') {
            steps {
                bat 'copy "C:\\omer\\year3\\Devops\\DevOps-Assignment\\.env" "%WORKSPACE%\\.env" /Y'
            }
        }

        stage('Check .env file') {
            steps {
                bat 'if exist .env (echo ✅ .env file found) else (echo ❌ ERROR: .env file NOT found & exit /b 1)'
            }
        }

        stage('Load Environment Variables') {
            steps {
                bat '''
                setlocal EnableDelayedExpansion
                for /F "tokens=1,2 delims==" %%A in (.env) do (
                    set "%%A=%%B"
                    echo Loaded: %%A=%%B
                )
                '''
            }
        }

        stage('Validate Environment Variables') {
            steps {
                bat '''
                echo JENKINS_USER=!JENKINS_USER!
                echo JENKINS_TOKEN=!JENKINS_TOKEN!
                echo JENKINS_URL=!JENKINS_URL!
                echo JOB_NAME=!JOB_NAME!
                '''
            }
        }

        stage('Check Python Installation') {
            steps {
                bat '''
                where python >nul 2>&1 || (
                    echo ❌ Python is not installed or not in PATH.
                    exit /b 1
                )
                '''
            }
        }

        stage('Check Palindrome') {
            steps {
                bat '"C:\\Path\\To\\Python\\python.exe" paly.py %NUMBER%'
            }
        }

        stage('Generate HTML Report') {
            steps {
                script {
                    writeFile file: 'output.html', text: """
                    <html>
                    <head>
                        <title>Palindrome Check Report</title>
                        <style>
                            body { font-family: Arial, sans-serif; text-align: center; }
                            h1 { color: #333; }
                            .result { font-size: 20px; font-weight: bold; }
                            button {
                                background-color: #008CBA;
                                border: none;
                                color: white;
                                padding: 15px 32px;
                                text-align: center;
                                font-size: 16px;
                                margin-top: 20px;
                                cursor: pointer;
                                border-radius: 5px;
                            }
                            button:hover { background-color: #005f73; }
                        </style>
                        <script>
                            function triggerJenkinsBuild() {
                                fetch('${JENKINS_URL}/job/${JOB_NAME}/buildWithParameters?NUMBER=${params.NUMBER}', {
                                    method: 'POST',
                                    headers: {
                                        'Authorization': 'Basic ' + btoa('${JENKINS_USER}:${JENKINS_TOKEN}')
                                    }
                                }).then(response => {
                                    if (response.ok) {
                                        alert('✅ Build triggered successfully!');
                                    } else {
                                        alert('❌ Failed to trigger build.');
                                    }
                                }).catch(error => {
                                    alert('⚠️ Error: ' + error);
                                });
                            }
                        </script>
                    </head>
                    <body>
                        <h1>🔢 Palindrome Check Report</h1>
                        <p><strong>Number:</strong> ${params.NUMBER}</p>
                        <button onclick="triggerJenkinsBuild()">🔄 Run Again</button>
                    </body>
                    </html>
                    """
                }
            }
        }

        stage('Archive & Publish Report') {
            steps {
                archiveArtifacts artifacts: 'output.html', fingerprint: true
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'output.html',
                    reportName: 'Palindrome Report'
                ])
            }
        }
    }

    post {
        success {
            echo "✅ Build succeeded! Check the Palindrome Report."
        }
        failure {
            echo "❌ Build failed. Check logs and report (if generated)."
        }
    }
}
