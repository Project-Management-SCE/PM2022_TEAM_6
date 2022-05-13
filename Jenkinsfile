pipeline {
    agent none
    stages {
        stage('Build'){
               agent  {
                  docker {
                    image 'cimg/base:stable'
                    args '-u root'    }
                      }
            steps {
            echo 'Building a new image'
            script {
                    checkout scm
                    def djangoproj = docker.build("djangoproj:${env.BUILD_ID}")
                    }
             sh 'docker tag djangoproj:latest mohmmdgaber/repository_name:latest'
             sh 'docker push  mohmmdgaber/djangoprohect:latest'
                  }
         }

        stage('run') {
               agent  {
                   docker {
                    image 'djangoproj:latest'}
                      }
            steps {
                    sh 'wget -O - -q https://checkip.amazonaws.com'
                    sh 'python manage.py jenkins'
                    sh 'python manage.py test tests.managerfuncstest'
                    sh 'python manage.py test tests.voulntererfuncs'
                  }
         }
        stage('Deploy to Heroku') {
                 agent {
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
