pipeline {
    agent any
    stages {
        stage('start'){
            steps{
                echo 'pulled from git...'
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t maayanmi/myrepo .'
            }
        }

        stage('run') {
            steps {
                sh 'docker run --name weatherapp -dit -p 80:5000 maayanmi/myrepo'
            }
        }
        stage('test') {
            steps {
                sh 'docker exec weatherapp python3 testing.py'
            }
        }
        stage('delivery') {
            steps {
                sh 'sudo docker push docker_deploy.44.207.98.58/maayanmi/myrepo'
                echo 'success'
            }
        }

        stage('clean'){
            steps{
                sh 'docker kill weatherapp && docker rm weatherapp'
            }
        }
    }
}
