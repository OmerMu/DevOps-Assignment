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
