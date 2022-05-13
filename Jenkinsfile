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
             echo '////Pushing a tag to Docker.io'
             sh 'docker login -u "mohmmdgaber" -p "sY~_wW(=s2sR@BS" docker.io'
             sh 'docker tag djangoproj:latest  mohmmdgaber/djangoprohect:$BUILD_ID'
             sh 'docker push  mohmmdgaber/djangoprohect:$BUILD_ID'
                  }
         }

        stage('Run') {
               agent  {
                   docker {
                    image 'djangoproj:latest'}
                      }
            steps {
                    echo '////Running the project'
                    sh 'wget -O - -q https://checkip.amazonaws.com'
                    sh 'python manage.py jenkins'
                  }
         }
        stage('Test') {
               agent  {
                   docker {
                    image 'djangoproj:latest'}
                      }
            steps {
                    echo '////Testing pytests'
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
              echo '////Deploying the site'
              sh '''
                    curl https://cli-assets.heroku.com/install.sh | sh;
                    heroku container:login
                    docker tag djangoproj:$BUILD_ID registry.heroku.com/djang-project/web
                    docker push registry.heroku.com/djang-project/web
                    heroku container:release web --app djang-project
                '''
            }
          }

    }
}
