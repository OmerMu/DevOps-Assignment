pipeline {
    agent any

    parameters {
        string(name: 'NUMBER', defaultValue: '12321', description: 'Enter a number to check if it is a palindrome')
    }

    stages {

        stage('Copy .env to Jenkins Workspace') {
            steps {
                bat 'copy C:\\omer\\year3\\Devops\\DevOps-Assignment\\.env C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\DevOpsPrj\\.env /Y'
            }
        }

        stage('Check .env file') {
            steps {
                bat 'if exist .env (echo ✅ .env file found) else (echo ❌ ERROR: .env file NOT found & exit /b 1)'
            }
        }

        stage('Load Environment Variables') {
            steps {
                bat 'call load_env.bat'
            }
        }

        stage('Print Loaded Environment Variables') {
            steps {
                bat 'set JENKINS_USER && set JENKINS_TOKEN && set JENKINS_URL && set JOB_NAME'
            }
        }

        stage('Print .env contents') {
            steps {
                bat 'type .env'
            }
        }

        stage('Validate Parameters') {
            steps {
                script {
                    if (!params.NUMBER.isInteger()) {
                        error "❌ Invalid NUMBER value: ${params.NUMBER} (must be an integer)"
                    }
                }
            }
        }

        stage('Check Palindrome') {
            steps {
                script {
                    def number = params.NUMBER.toString()
                    def reversed = number.reverse()
                    def isPalindrome = (number == reversed)

                    def result = isPalindrome ? 
                        "<p style='color:green;'>✅ The number ${number} is a palindrome.</p>" : 
                        "<p style='color:red;'>❌ The number ${number} is NOT a palindrome.</p>"

                    writeFile file: 'palindrome_report.html', text: """
                    <html>
                    <head>
                        <title>Palindrome Check</title>
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
                                fetch('${JENKINS_URL}/job/${JOB_NAME}/buildWithParameters?NUMBER=${number}', {
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
                        <p><strong>Number:</strong> ${number}</p>
                        ${result}
                        <button onclick="triggerJenkinsBuild()">🔄 Run Again</button>
                    </body>
                    </html>
                    """
                }
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python palindrome.py %NUMBER%'  // התאמה להרצת פייתון ב-Windows
            }
        }

        stage('Archive & Publish Report') {
            steps {
                archiveArtifacts artifacts: 'palindrome_report.html', fingerprint: true
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'palindrome_report.html',
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
