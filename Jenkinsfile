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

            steps {
              sh '''
                    curl https://cli-assets.heroku.com/install.sh | sh;
                    heroku config:add \ HEROKU_OAUTH_ID=09261dc3-b4cf-477b-b237-cf2f61e4c8e7 \ HEROKU_OAUTH_SECRET=7caac8e8-1dc6-4a26-aeab-58e7208be634                    heroku container:login
                    heroku container:push web --app djang-project
                    heroku container:release web --app djang-project
                '''
            }
          }

    }
}
