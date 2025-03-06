import sys
import os
import requests
from dotenv import load_dotenv

# טוען משתנים מקובץ .env (אם קיים)
load_dotenv()

# משתני הסביבה
jenkins_url = os.getenv("JENKINS_URL", "http://localhost:8080")
job_name = os.getenv("JOB_NAME", "DevOps-Assignment")
jenkins_user = os.getenv("JENKINS_USER", "")
jenkins_token = os.getenv("JENKINS_TOKEN", "")

# קבלת מספר כפרמטר
if len(sys.argv) < 2:
    print("❌ Error: No number provided. Usage: python paly.py <number>")
    sys.exit(1)

number = sys.argv[1]

# בדיקת פלינדרום
is_palindrome = number == number[::-1]
status = "green" if is_palindrome else "red"
result = f"✅ The number {number} is a palindrome." if is_palindrome else f"❌ The number {number} is NOT a palindrome."

# כתיבת דוח HTML
html_content = f"""
<html>
<head>
    <title>Palindrome Check</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; }}
        h1 {{ color: #333; }}
        .result {{ font-size: 20px; font-weight: bold; color: {status}; }}
        .btn {{
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
        }}
        .btn:hover {{ background-color: #218838; }}
    </style>
    <script>
        function triggerJenkinsBuild() {{
            fetch("{jenkins_url}/job/{job_name}/buildWithParameters?NUMBER={number}", {{
                method: 'POST',
                headers: {{
                    'Authorization': 'Basic ' + btoa('{jenkins_user}:{jenkins_token}'),
                    'Content-Type': 'application/json'
                }}
            }}).then(response => {{
                if (response.ok) {{
                    alert('✅ Build triggered successfully!');
                }} else {{
                    alert('❌ Failed to trigger build.');
                }}
            }}).catch(error => {{
                alert('⚠️ Error: ' + error);
            }});
        }}
    </script>
</head>
<body>
    <h1>🔢 Palindrome Check Report</h1>
    <p><strong>Number:</strong> {number}</p>
    <p class="result">{result}</p>
    <button class="btn" onclick="triggerJenkinsBuild()">🔄 Run Again</button>
    <p>📜 <a href="{jenkins_url}/job/{job_name}/ws/output.html" target="_blank">View Report</a></p>
</body>
</html>
"""

# שמירת הדוח
with open("output.html", "w") as f:
    f.write(html_content)

# הדפסת התוצאה
print(result)
