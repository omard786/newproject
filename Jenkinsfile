pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        docker_hub_credentials = credentials("docker-hub-credentials")
    }
    stages{
        stage('Test'){
            steps{
              sh 'bash ./pre.sh'

            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose build micro-services'
            }
        }
        stage('Push'){
            steps{
                sh "docker login -u ${env.docker_hub_credentials_USR} -p ${env.docker_hub_credentials_PSW}"
                sh 'docker ps'
                sh 'docker-compose push'
            }


        }
        stage('config and Set Swarm'){
            steps{
                 sh 'ansible-playbook -i inventory.yaml playbook-1.yaml'
             }
            
        }
        stage('Deploy'){
            steps{
                sh 'docker stack deploy --compose-file docker-compose.yaml'
                sh 'docker stack services'
            }

        }
    }
}