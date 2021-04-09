pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
    }
    stages{
        stage('Test'){
            steps{
              sh 'bash ./pre.sh'

            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose up -d'
                sh 'docker-compose build'
            }
        }
        stage('Push'){
            steps{
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