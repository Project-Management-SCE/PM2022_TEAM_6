pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-alpine'
                }
            }
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install --upgrade Pillow'
                sh 'pip3 install evdev'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m py_compile manage.py'
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
