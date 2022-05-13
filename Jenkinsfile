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
        stage('Deploy to Heroku') {
            agent  {
            docker {
                    image 'cimg/base:stable'
                    args '-u root'
                }
               }


            steps {
              sh '''
                    curl https://cli-assets.heroku.com/install.sh | sh;
                    heroku container:login
                    heroku container:push web --app djang-project
                    heroku container:release web --app djang-project
                '''
            }
          }

    }
}
