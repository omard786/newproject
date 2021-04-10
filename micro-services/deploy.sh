#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@project:docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@project << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml main-services
EOF