#### RDS 12: Масштабирование и кластер

- Запустите работающий кластер Redis, задействовав все предоставленные в ваше распоряжение хосты.
- Кластер должен оставаться работоспособным при отказе любого из хостов.



#### На каждом сервере запускаем
$ sudo apt install redis-server redis-tools -y

$ sudo vim /etc/redis/redis.conf
```
bind 0.0.0.0
appendonly yes
cluster-enabled yes
cluster-config-file nodes-6379.conf
cluster-node-timeout 15000
```
$ sudo systemctl restart redis.service

#### Запускаем на одном сервере. Получаем 3 мастера и 3 слэйва.
$ redis-cli --cluster create 10.110.0.{2,3,4,5,6,7}:6379 --cluster-replicas 1
