pipeline {
    agent none
    stages {
        stage('Build') { 
         agent {
               dockerfile {
               filename 'Dockerfile'
               label 'hello_world'
                          }
               }
            steps {
                sh ''
                  }
         }
        stage('run') { 
         agent {
               docker {
               image 'hello_world'
                          }
            }   
            steps {
                sh 'sudo docker run --rm hello_world'
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
