pipeline {
    /*------------------------------------------------------
      הגדרת ה-Pipeline ב-Jenkins:
      - Agent any: שימוש בכל Node זמין
      - הגדרת פרמטר "ENVIRONMENT" עם ברירת מחדל "dev"
      - שלבים:
         1. Validate ENV
         2. Build
         3. Generate HTML Report
      - Post: פעולות במקרה הצלחה או כישלון
    ------------------------------------------------------*/
    agent any

    parameters {
        // פרמטר מחרוזת, ברירת מחדל dev
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'בחר סביבה (dev/test/prod)')
    }

    stages {
        stage('Validate ENV') {
            steps {
                script {
                    /*------------------------------------------------------
                      שלב ולידציה:
                      אם הפרמטר ENVIRONMENT אינו אחד מהערכים dev/test/prod,
                      נזרוק שגיאה שתפיל את ה-Build.
                    ------------------------------------------------------*/
                    if (!['dev','test','prod'].contains(ENVIRONMENT)) {
                        error "ערך ENVIRONMENT לא חוקי: ${ENVIRONMENT}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                /*------------------------------------------------------
                  הדפסת שם הסביבה שנבחרה בקונסול
                ------------------------------------------------------*/
                echo "Building for environment: ${ENVIRONMENT}"
            }
        }

        stage('Generate HTML Report') {
            steps {
                script {
                    /*------------------------------------------------------
                      יוצרים קובץ HTML פשוט באמצעות פקודות Shell
                      המתאר את תוצאות הבנייה והסביבה שנבחרה.
                    ------------------------------------------------------*/
                    sh '''
                      echo "<html><head><title>Build Report</title></head><body>" > build_report.html
                      echo "<h1>תוצאות הבנייה</h1>" >> build_report.html
                      echo "<p>הסביבה שנבחרה: ${ENVIRONMENT}</p>" >> build_report.html
                      echo "<p>ניתן לצפות בלינק לתוצאות כאן: <a href='http://example.com'>צפה בתוצאה</a></p>" >> build_report.html
                      echo "</body></html>" >> build_report.html
                    '''
                }
                /*------------------------------------------------------
                  ארכוב (Archive) של קובץ ה-HTML כך שיהיה זמין ב-Artifacts
                ------------------------------------------------------*/
                archiveArtifacts artifacts: 'build_report.html', fingerprint: true

                /*------------------------------------------------------
                  פרסום ה-HTML דרך Publish HTML Plugin
                  -> יופיע תחת לשונית "Build Report" ב-Jenkins
                ------------------------------------------------------*/
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
            echo "ה-Build הסתיים בהצלחה! ניתן לעיין בדו"ח HTML בקישור שהתפרסם"
        }
        failure {
            echo "ה-Build נכשל. נא לעיין בלוגים ובדו"ח (אם נוצר)"
        }
    }
}
