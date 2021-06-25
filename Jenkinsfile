pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                // pytest
                // run for each service
                // produce cov reports
            }
        }
        stage('Build') {
            steps {
                // install docker and docker compose
                // docker-compose build
            }
        }
        stage('Push') {
            steps {
                // install docker and docker compose
                // docker-compose push
            }
        }
        stage('Configuration Management (Ansible)') {
            steps {
                // install ansible on jenkins machine for the Jenkins user
                // ansible-playbook -i inventory.yaml playbook.yaml
            }
        }
        stage('Deploy') {
            steps {
                // create swarm infrastructure
                // copy over docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml animal_noises
            }
        }
    }
}