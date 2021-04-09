pipeline {
    agent any
    environment{
        DATABASE_URI = credientials("DATABASE_URI")
    }
    stages{
        stage('Test'){
            sh 'bash ./pre.sh'
        }
        stage('Build'){
            sh 'docker-compose build'
            sh 'docker-compose up -d'
        }
        stage('Push'){

            sh 'docker ps'
            sh 'docker-compose push'

        }
        stage('config and Send Swarm'){
             sh 'ansible-playbook -i inventory.yaml playbook-1.yaml'
            
        }
        stage('Deploy'){

            sh 'docker stack deploy --compose-file docker-compose.yaml'
            sh 'docker stack services'
        }
    }
}