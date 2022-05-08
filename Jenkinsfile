pipeline {
    agent any
    stages {
        stage('Build') { 
         agent {
               dockerfile {
               filename 'Dockerfile'
                          }
               }
            steps {
                    sh ''
                  }
         }
        stage('run') {
         agent {
               docker {
               image 'ca0bcf53dec5f0510a76b1d0b33a17f7657a5d97'
                          }
            }
            steps {
                sh 'docker run --rm ca0bcf53dec5f0510a76b1d0b33a17f7657a5d97'
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
