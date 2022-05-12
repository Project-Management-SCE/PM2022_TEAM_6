pipeline {
    agent  {
               dockerfile {
               filename 'Dockerfile'
                args '-u root'
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
                sh 'python manage.py test tests.managerfuncstest'
                sh 'python manage.py test tests.voulntererfuncs'


            }
          }

    }
}
