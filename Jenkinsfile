pipeline {
    agent any
    environment {
        // dockerhub config
        //HUB_DOCKER_HOST ='https://index.docker.io/v1/'
        HUB_DOCKER_HOST ='https://cloud.docker.com/repository/docker/kivadratik/test'
        HUB_DOCKER_CREDS = credentials('b767963b-c7f6-4274-bccd-e98028d9ace3')
        TAGGED_NAME = 'gitpull_web' 
        IMAGE_NAME = 'test_webapp'
        CONTAINER_NAME = 'gitpull_web_1'
        NAM = 'kivadratik/'
        
        // git config
       //GITHUB_HOST = "gitlab.etton.ru/swish/swish-engine-app"
       // GITHUB_CREDS = credentials('8be32b57-7a12-41c1-a21a-b4c5507392c9')
       BUILD_VERSION = sh(returnStdout: true, script: 'git describe --long --always').trim()

        // ssh prod config
        //SSH_HOST = "18.224.38.108"
        //SSH_PORT = "22"
        //SSH_CREDS = credentials('AKIAJOJ7U6B4SZI25XXA')

        
    }
    stages {
        stage('clear all containers') {
            steps {
				sh "echo 'I will clean all containers'"
				//sh "docker stop `docker ps | grep gitpull_web | awk '{print $1}'` & docker rm `docker ps -a | grep gitpull_web | awk '{print $1}'`"
                sh '(docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}) || echo "No such container"'
				// sh "sudo docker ps -a -q | xargs -r sudo docker stop"
                // sh "sudo     docker ps -a -q | xargs -r sudo docker rm"
                // sh 'sudo docker images | grep -v "postgres\\|python\\|nginx" | awk \'{print $3}\' | grep -v \'IMAGE\' | xargs -r sudo docker rmi --force'
                // sh "sudo docker volume prune --force"
            }
        }
        stage('build') {
            steps {
                sh "pwd"
                //sh "ls -l ../.."
                //sh "pwd"
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
                    dockerVersionTag = "${NAM}/${IMAGE_NAME}:${BUILD_VERSION}"
                    dockerLatestTag = "${NAM}/${IMAGE_NAME}:latest"
                }
                  sh "echo '${dockerLatestTag}'"
                  sh "echo '${dockerVersionTag}'" 
                  sh "docker tag ${IMAGE_NAME} ${dockerLatestTag}"
                  sh "docker tag ${IMAGE_NAME} ${dockerVersionTag}"
                  sh "echo ${HUB_DOCKER_CREDS_PSW} | docker login -u=${HUB_DOCKER_CREDS_USR} --password-stdin ${HUB_DOCKER_HOST}"
                  sh "docker push ${dockerVersionTag}"
                  sh "docker push ${dockerLatestTag}"
            }
        }
        //stage('update prod server'){
        //    steps {
        //        script {
        //            SSH_CMD = "sshpass -p '${SSH_CREDS_PSW}' ssh -o StrictHostKeyChecking=no -p ${SSH_PORT} ${SSH_CREDS_USR}@${SSH_HOST}"
        //        }
        //        sh "sudo tar -czf deployment.tar.gz ./deployment"
        //        sh "cat deployment.tar.gz | ${SSH_CMD} 'tar xzf - -C ~/'"
        //        sh "${SSH_CMD} 'echo ${HUB_DOCKER_CREDS_PSW} | sudo docker login -u=${HUB_DOCKER_CREDS_USR} --password-stdin ${HUB_DOCKER_HOST}'"
        //        sh "${SSH_CMD} 'cd ~/dployment/prod/ && sudo docker-compose pull'"
		//		  sh "${SSH_CMD} 'cd ~/deployment/prod/ && sudo docker-compose up -d'"
		//		  sh "${SSH_CMD} 'sudo docker image prune -a --force'"
        //    }
        //}

    //}
    //post {
    //    failure {
    //        sh "${CURL_CMD} '${NOTIFY_CMD}FAIL!  swish-engine-app   ${BUILD_VERSION}'"
    //    }
    //    success {
    //        sh "${CURL_CMD} '${NOTIFY_CMD}OK!  swish-engine-app   ${BUILD_VERSION}'"
    //    }
    }
}
