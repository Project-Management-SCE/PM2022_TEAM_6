pipeline {
    agent none
    stages {
        stage('Build') { 
         agent {
               dockerfile {
               filename 'Dockerfile'
                          }
               }
            steps {
                sh 'docker build -t hello_world .'
                  }
         }
        stage('run') { 
         agent {
               dockerfile {
               docker 'hello_world'
                          }
            }   
            steps {
                sh 'docker run --rm hello_world'
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
