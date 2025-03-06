pipeline {
    agent any

    stages {
        stage('Validate Parameters') {
            steps {
                script {
                    // Validate the ENVIRONMENT parameter
                    if (!['dev','test','prod'].contains(params.ENVIRONMENT)) {
                        error "❌ Invalid ENVIRONMENT value: ${params.ENVIRONMENT}"
                    }

                    // Validate the NUMBER parameter
                    if (!params.NUMBER.isInteger()) {
                        error "❌ Invalid NUMBER value: ${params.NUMBER} (must be an integer)"
                    }
                }
            }
        }

        stage('Check Palindrome') {
            steps {
                script {
                    def number = params.NUMBER
                    def reversed = number.reverse()
                    def isPalindrome = (number == reversed)

                    // יצירת קובץ HTML עם התוצאה
                    def result = isPalindrome ? 
                        "<p style='color:green;'> The number ${number} is a palindrome.</p>" : 
                        "<p style='color:red;'> The number ${number} is NOT a palindrome.</p>"

                    writeFile file: 'palindrome_report.html', text: """
                    <html>
                    <head>
                        <title>Palindrome Check</title>
                        <style>
                            body { font-family: Arial, sans-serif; text-align: center; }
                            h1 { color: #333; }
                            .result { font-size: 20px; font-weight: bold; }
                        </style>
                    </head>
                    <body>
                        <h1>🔢 Palindrome Check Report</h1>
                        <p><strong>Number:</strong> ${number}</p>
                        ${result}
                        <p><strong>Environment:</strong> ${params.ENVIRONMENT}</p>
                    </body>
                    </html>
                    """
                }
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
