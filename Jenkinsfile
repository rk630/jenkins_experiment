pipeline {
    agent any
    stages {
        stage('Copy files') {
            steps {
                git branch: 'main', url: 'https://github.com/rk630/jenkins_experiment.git'
                sh 'cp $WORKSPACE/* /var/jenkins_exp/'
            }
        }
        stage('Install Flask') {
            steps {
                sh 'pip3 install flask'
            }
        }
        stage('Run Flask application') {
            steps {
                sh 'python3 /var/jenkins_exp/jenkins_exp.py'
            }
        }
        
    }
    post {
        success {
            emailext body: 'The Jenkins build was successful',
                     subject: 'Jenkins Build Success',
                     to: 'krevanth630@gmail.com'
        }
        failure {
            emailext body: 'The Jenkins build has failed',
                     subject: 'Jenkins Build Failure',
                     to: 'krevanth630@gmail.com'
        }
        aborted {
            emailext body: 'The Jenkins build was aborted',
                     subject: 'Jenkins Build Aborted',
                     to: 'krevanth630@gmail.com'
        }
    }
}
