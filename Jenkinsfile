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
                sh 'sudo /usr/local/bin/python3 -m pip install --upgrade pip'
                sh 'python -m pip install --upgrade Pillow'
                sh 'pip install evdev'
                sh 'pip install -r requirements.txt'
                sh 'python -m py_compile manage.py'
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
