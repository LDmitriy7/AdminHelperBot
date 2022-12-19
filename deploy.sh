ENV_FILE_NAME=".env"
APP_NAME="admin-helper-bot"

if [ ! -f $ENV_FILE_NAME ]; then
  echo "You must create file '$ENV_FILE_NAME'"
  return
fi

docker build -t $APP_NAME .
docker run -ti --restart=always --name=$APP_NAME -e TZ=Europe/Moscow $APP_NAME

#docker compose up --build -d
