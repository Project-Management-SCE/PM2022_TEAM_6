pipeline {
    agent  {
               dockerfile {
               filename 'Dockerfile'
                          }
               }
    stages {
        stage('run') {
            steps {
                    sh 'wget -O - -q https://checkip.amazonaws.com'
                    sh 'python manage.py jenkins'
                  }
         }
        stage('test') {

            steps {
                sh 'python manage.py tests.managerfuncstest'
                sh 'python manage.py tests.voulntererfuncs'


            }
          }

    }
}
