pipeline {
    agent any
    environment {
        // dockerhub config
        HUB_DOCKER_HOST ='https://index.docker.io/v1/'
        HUB_DOCKER_CREDS = credentials('b767963b-c7f6-4274-bccd-e98028d9ace3')
        TAGGED_NAME = 'gitpull_web' 
        IMAGE_NAME = 'test_webapp'
        CONTAINER_NAME = 'gitpull_web_1'
        BUILD_VERSION = sh(returnStdout: true, script: 'git describe --long --always').trim()

        // ssh prod config
        SSH_HOST = "192.168.2.21"
        SSH_PORT = "22"
        SSH_CREDS = credentials('6835ab31-5ba5-4a93-814b-6713e4b4160a')

        // aws test config
		AWS_HOST = "18.224.38.108"
		AWS_PORT = "22"
		AWS_T2MICRO_CREDS = credentials('AKIAJOJ7U6B4SZI25XXA')
		AWS_USER = 'admin'
		
    }
    stages {
        stage('clear all containers') {
            steps {
                sh "echo 'I will clean all containers'"
                sh '(docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}) || echo "No such container"'
            }
        }
        stage('build') {
            steps {
                sh "docker-compose -f ../git-pull/docker-compose.yml up -d --build"
                sh "docker images"
            }
        }
        stage('test and preparing') {
            steps {
                sh "echo 'I will test'"
                sh "docker exec ${CONTAINER_NAME} bash -c 'python manage.py test'"
            }
            post {
                always {
                sh "echo 'I will copy'"
                    //sh "sudo docker cp swish-engine-app:/var/www/swish-engine-app/nosetests.xml nosetests.xml"
                    // junit '**/nosetests.xml'
                }
            }
        }

        stage('docker tag and push') {
            steps {
                script {
                    dockerVersionTag = "${HUB_DOCKER_CREDS_USR}/${IMAGE_NAME}:${BUILD_VERSION}"
                    dockerLatestTag = "${HUB_DOCKER_CREDS_USR}/${IMAGE_NAME}:latest"
                }
                  sh "echo '${dockerLatestTag}'"
                  sh "echo '${dockerVersionTag}'" 
                  sh "docker tag ${TAGGED_NAME} ${dockerLatestTag}"
                  sh "docker tag ${TAGGED_NAME} ${dockerVersionTag}"
                  sh "echo ${HUB_DOCKER_CREDS_PSW} | docker login -u=${HUB_DOCKER_CREDS_USR} --password-stdin ${HUB_DOCKER_HOST}"
                  sh "docker push ${dockerVersionTag}"
                  sh "docker push ${dockerLatestTag}"
            }
        }
        stage('update prod server'){
            steps {
                script {
                    SSH_CMD = "sshpass -p '${SSH_CREDS_PSW}' ssh -o StrictHostKeyChecking=no -p ${SSH_PORT} ${SSH_CREDS_USR}@${SSH_HOST}"
                }
                sh "tar -czf deployment.tar.gz prod_docker-compose.yml"
                sh "cat deployment.tar.gz | ${SSH_CMD} 'tar xzf - -C ~/'"
                sh "${SSH_CMD} 'echo ${HUB_DOCKER_CREDS_PSW} | docker login -u=${HUB_DOCKER_CREDS_USR} --password-stdin ${HUB_DOCKER_HOST}'"
                sh "${SSH_CMD} 'docker ps -a -q | xargs -r sudo docker stop'"
                sh "${SSH_CMD} 'docker ps -a -q | xargs -r sudo docker rm'"
                sh "${SSH_CMD} 'sudo docker volume prune --force'"
                sh "${SSH_CMD} 'docker-compose -f prod_docker-compose.yml pull'"
                sh "${SSH_CMD} 'docker-compose -f prod_docker-compose.yml up -d'"
                sh "${SSH_CMD} 'docker image prune -a --force'"
            }
        }
        stage('update AWS server'){
            steps {
                script {
                    SSH_CMD = "ssh -p ${AWS_PORT} ${AWS_USER}@${AWS_HOST}"
                }
                sh "tar -czf deployment.tar.gz aws_docker-compose.yml"
                sh "cat deployment.tar.gz | ${SSH_CMD} 'tar xzf - -C ~/'"
                sh "${SSH_CMD} 'echo ${HUB_DOCKER_CREDS_PSW} | docker login -u=${HUB_DOCKER_CREDS_USR} --password-stdin ${HUB_DOCKER_HOST}'"
                sh "${SSH_CMD} 'docker ps -a -q | xargs -r sudo docker stop'"
                sh "${SSH_CMD} 'docker ps -a -q | xargs -r sudo docker rm'"
                sh "${SSH_CMD} 'sudo docker volume prune --force'"
                sh "${SSH_CMD} 'docker-compose -f prod_docker-compose.yml pull'"
                sh "${SSH_CMD} 'docker-compose -f prod_docker-compose.yml up -d'"
                sh "${SSH_CMD} 'docker image prune -a --force'"
            }
        }
    }
}
