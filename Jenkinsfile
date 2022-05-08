pipeline {
    agent  {
               dockerfile {
               filename 'Dockerfile'
                          }
               }
    stages {
        stage('Build') {
            steps {
                    sh 'python manage.py runserver'
                  }
         }
        stage('run') {

            steps {
                sh ''
            }
          }
//         stage('Test') {
//             agent {
//                 docker {
//                     image 'qnib/pytest'
//                 }
//             }
//             steps {
//                 sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
//             }
//             post {
//                 always {
//                     junit 'test-reports/results.xml'
//                 }
//             }
//         }
    }
}
