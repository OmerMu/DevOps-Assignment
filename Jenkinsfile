pipeline {
    agent any

    parameters {
        string(name: 'NUMBER', defaultValue: '12321', description: 'Enter a number to check if it is a palindrome')
    }

    stages {
        stage('Check Palindrome') {
            steps {
                script {
                    def number = params.NUMBER.toString()
                    def reversed = number.reverse()
                    def isPalindrome = (number == reversed)

                    if (isPalindrome) {
                        echo "✅ The number ${number} is a palindrome."
                    } else {
                        echo "❌ The number ${number} is NOT a palindrome."
                    }
                }
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
                </style>
            </head>
            <body>
                <h1>🔢 Palindrome Check Report</h1>
                <p><strong>Number:</strong> ${params.NUMBER}</p>
            </body>
            </html>
            """
        }
    }
}

    }

    post {
        success {
            echo "✅ Build succeeded!"
        }
        failure {
            echo "❌ Build failed."
        }
    }
}
