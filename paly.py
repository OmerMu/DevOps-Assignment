import sys
import os
import requests
from dotenv import load_dotenv

# טוען משתנים מקובץ .env
load_dotenv()
jenkins_url = os.getenv("JENKINS_URL", "http://localhost:8080")
job_name = os.getenv("JOB_NAME", "DevOps-Assignment")
number = sys.argv[1]

# בדיקה האם המספר פלינדרום
is_palindrome = number == number[::-1]
status = "green" if is_palindrome else "red"
result = f"✅ The number {number} is a palindrome." if is_palindrome else f"❌ The number {number} is NOT a palindrome."

# כתיבת דוח HTML עם כפתור להרצת ה-Job מחדש
with open("output.html", "w") as f:
    f.write(f"""
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
                fetch('/trigger-build', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify({{"NUMBER": "{number}"}})
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
    </body>
    </html>
    """)

print(result)
