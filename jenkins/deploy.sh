scp docker-compose.yaml newestinstance1:
ssh newestinstance1 << EOF
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml app
EOF
