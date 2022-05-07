pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-alpine'
                }
            }
            steps {
                sh 'virtualenv projectrun -p python'
                sh 'source projectrun/bin/activate'
                sh 'pip list --no-cache-dir'
                sh 'python -m pip install --upgrade Pillow --no-cache-dir'
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
