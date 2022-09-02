### Redis

```
## Установка
$ sudo apt install redis -y
## Вход
$ redis-cli
```

#### Информация о сервевре
127.0.0.1:6379> info server

#### Создать запись first с ключом 1
127.0.0.1:6379> set first 1

#### Прочитать запись по ключу 1
127.0.0.1:6379> get first

#### Команда возвращает количество записей, существующих среди перечисленных ключей.
127.0.0.1:6379> EXISTS key [key ...]

#### Удалить записи по указанным ключам. Отсутствующие ключи — игнорируются: в ответе вернётся количество удалённых записей.
127.0.0.1:6379> DEL key [key ...]

#### Создать запись other key с ключом another value на 20 секунд (EX 20)
SET "other key" "another value" EX 20

