pipeline {
    agent any
    stages {
        stage('clean'){
            steps{
                sh 'docker kill weatherapp && docker rm weatherapp'
            }
        }
        
        stage('start'){
            steps{
                echo 'pulled from git...'
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t docker_deploy.44.207.98.58/maayanmi/weather .'
            }
        }

        stage('run') {
            steps {
                sh 'docker run --name weatherapp -dit -p 80:5000 maayanmi/weather'
            }
        }
        
        stage('delivery') {
            steps {
                rtDockerPush(
                serverId: 'Artifactory-1',
                image: 'docker_deploy/maayanmi/weather',
                host: 44.207.98.58,
                targetRepo: 'docker-deploy'
            )
                echo 'success'
            }
        }

    }
}
