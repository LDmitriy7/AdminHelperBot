ENV_FILE_NAME=".env"
APP_NAME="admin-helper-bot"

if [ ! -f $ENV_FILE_NAME ]; then
  echo "You must create file '$ENV_FILE_NAME'"
  return
fi

docker build . -t $APP_NAME
docker run -ti $APP_NAME --restart=always --name=$APP_NAME -e TZ=Europe/Moscow

#docker compose up --build -d
