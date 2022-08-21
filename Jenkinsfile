pipeline {
    environment {
        dockerImage = 'maayanmi/weather'
        KUBECONFIG='/home/ubuntu/admin.conf'
        //dockerhub=credentials('dckr_pat_j420nMPpk_HarddaASm86gNZzjc')
    }

    agent { label 'docker-builds' }
    stages {

        stage('Building our image') {
            steps{
                script {
                    sh "sudo docker build -t $dockerImage:$BUILD_ID ." 
                }
            }
        }

        stage('Delivery') {
            steps{
                script {
                    //sh 'echo $dockerhub_PSW | sudo docker login -u $dockerhub_USR --password-stdin docker.io' 
                    sh 'docker login -u maayanmi -p BdZcFBpNhKnABQ2'                   
                    sh "docker push $dockerImage:$BUILD_ID"
                }
            }
        }

        stage('pre deploy deployment'){
            steps{
                sh 'sed -i "s,REPLACE,$dockerImage:$BUILD_ID," deployment.yml'
                stash includes: 'deployment.yml', name: 'DEPLOY'
            }
        }

        stage('clean up'){
            steps{
                script{
                    sh "docker rmi -f $dockerImage:$BUILD_ID"
                }
            }
        }

        stage('deploy deployment') {
            agent { label 'k8smaster' }
            steps{
                unstash 'DEPLOY'
                script {
                    sh "kubectl apply -f deployment.yml"
                }
            }
        }
    }
}