import sys
import os
from dotenv import load_dotenv

# טוען משתנים מקובץ .env
load_dotenv()
jenkins_user = os.getenv("JENKINS_USER")
jenkins_token = os.getenv("JENKINS_TOKEN")
jenkins_url = os.getenv("JENKINS_URL", "http://localhost:8080")
job_name = os.getenv("JOB_NAME", "DevOps-Assignment")

# קבלת מספר כפרמטר
number = sys.argv[1]

# בדיקה האם המספר פלינדרום
if number == number[::-1]:
    result = f"✅ The number {number} is a palindrome."
    status = "green"
else:
    result = f"❌ The number {number} is NOT a palindrome."
    status = "red"

# כתיבת דוח HTML עם כפתור להרצת ה-Job מחדש
with open("output.html", "w") as f:
    f.write("""
    <html>
    <head>
        <title>Palindrome Check</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            h1 { color: #333; }
            .result { font-size: 20px; font-weight: bold; }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                font-size: 18px;
                color: white;
                background-color: #28a745;
                border: none;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
                margin-top: 20px;
            }
            .btn:hover { background-color: #218838; }
        </style>
        <script>
            function triggerJenkinsBuild() {
                fetch('{jenkins_url}/job/{job_name}/buildWithParameters?NUMBER={number}', {
                    method: 'POST',
                    headers: {
                        'Authorization': 'Basic ' + btoa('{jenkins_user}:{jenkins_token}')
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
        <p><strong>Number:</strong> {number}</p>
        <p style='color:{status};'>{result}</p>
        <button class="btn" onclick="triggerJenkinsBuild()">🔄 Run Again</button>
    </body>
    </html>
    """.format(number=number, status=status, result=result, jenkins_url=jenkins_url, job_name=job_name, jenkins_user=jenkins_user, jenkins_token=jenkins_token))

print(result)
