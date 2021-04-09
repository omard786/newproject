pipeline {
    agent any
    environment{}
    stages{
        stage('Test'){

            //run pytest
            
        }
        stage('Build'){

            sh 'docker-compose build'
            sh 'docker-compose up -d'
        }
        stage('Push'){

            sh 'docker ps'
            sh 'docker-compose push'

        }
        stage('Sending Swarm'){
            //run playbook define inventory
            
        }
        stage('Deploy'){

            sh 'docker stack deploy --compose-file docker-compose.yaml'
            sh 'docker stack services'
        }
    }
}