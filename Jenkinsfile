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
                    sh 'docker run --rm ca0bcf53dec5f0510a76b1d0b33a17f7657a5d97'
                  }
         }
//         stage('run') {
//          agent {
//                docker {
//                image 'f9ff0430bc122c205477aa4128c7a955befd5647'
//                           }
//             }
//             steps {
//                 sh 'docker run --rm '
//             }
//           }
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
