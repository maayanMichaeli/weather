pipeline {
    agent any
    environment {
        dockerhub=credentials('5fe6930e-aa21-4e54-807e-311656614d20')
    }
    stages {
        stage('start'){
            steps{
                echo 'pulled from git...'
            }
        }
        stage('clean'){
            steps{
                sh 'docker kill weatherapp && docker rm weatherapp'
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
        stage('deploy') {
            steps {
                sh 'echo $dockerhub_PSW | sudo docker login -u $dockerhub_USR --password-stdin'
                sh 'sudo docker push maayanmi/myrepo'
                echo 'success'
            }
        }
    }
}
