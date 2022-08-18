pipeline {
    environment {
        dockerImage = 'maayanmi/weather'
    }

    agent { label 'docker-builds' }
    stages {

        stage('Building our image') {
            steps{
                script {
                    sh "sudo docker build . -f weatherDockerfile -t $dockerImage:$BUILD_ID"
                }
            }
        }

        stage('Delivery') {
            steps{
                script {
                    sh "docker push $dockerImage:$BUILD_ID"
                }
            }
        }

        stage('clean up'){
            steps{
                script{
                    sh "docker rmi $dockerImage:$BUILD_ID"
                }
            }
        }

        stage('pre deploy deployment'){
            steps{
                sh 'sed -i "s,REPLACE,$dockerImage:$BUILD_ID," weather-deploy.yml'
                stash includes: 'weather-deploy.yml', name: 'DEPLOY'
            }
        }

        stage('deploy deployment') {
            agent { label 'k8s' }
            steps{
                unstash 'DEPLOY'
                script {
                    sh "kubectl apply -f weather-deploy.yml"
                }
            }
        }
    }
}