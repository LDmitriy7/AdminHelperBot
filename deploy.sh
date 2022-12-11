ENV_FILE='.env'

if [ ! -f "$ENV_FILE" ]; then
  echo "You must create file '$ENV_FILE'"
  return
fi

#docker compose up --build -d
docker build -t adminhelperbot_app . && docker run -ti --restart=always -e TZ=Europe/Moscow adminhelperbot_app