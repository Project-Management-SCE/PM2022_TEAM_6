pipeline {
    agent none
    stages {
        stage("build") {    
            steps {
                sh 'docker build -t hello_world .'
            }
         }
        stage("run") {    
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
