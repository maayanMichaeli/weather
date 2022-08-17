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
                sh 'docker build -t 44.207.98.58/docker_deploy/maayanmi/weather .'
            }
        }

        stage('run') {
            steps {
                sh 'docker run --name weatherapp -dit -p 80:5000 44.207.98.58/docker_deploy/maayanmi/weather'
            }
        }
        
        stage('delivery') {
            steps {
                rtDockerPush(
                serverId: 'artifactoryID',
                image: '44.207.98.58/docker_deploy/maayanmi/weather',
                targetRepo: 'docker-deploy'
            )
                echo 'success'
            }
        }

    }
}
