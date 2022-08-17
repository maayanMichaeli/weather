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
                sh 'docker build -t docker_deploy/maayanmi/weather .'
            }
        }

        stage('run') {
            steps {
                sh 'docker run --name weatherapp -dit -p 80:5000 docker_deploy/maayanmi/weather'
            }
        }
        
        stage('delivery') {
            steps {
                rtDockerPush(
                serverId: 'Artifactory-1',
                image: 'docker_deploy/maayanmi/weather',
                host: '44.207.98.58',
                targetRepo: 'docker-deploy'
            )
                echo 'success'
            }
        }

    }
}
