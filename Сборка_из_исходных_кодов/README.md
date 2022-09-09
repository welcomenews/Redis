````
apt update
apt install -y curl build-essential     # без этого не обойдёмся
apt install -y pkg-config zip           # опционально
apt install -y tk tcl                   # для тестирования после сборки

# по указанной ссылке всегда актуальная версия и архив всегда распаковывается в однозначную папку;
# это сделано специально: как раз для упрощения пересборки скриптами
# переходим в папку с исходниками, затем качаем с распаковкой на лету и идём в папку redis-stable:
cd /usr/src
curl https://download.redis.io/redis-stable.tar.gz | tar -xvz
cd redis-stable

make
make test
make install
```
