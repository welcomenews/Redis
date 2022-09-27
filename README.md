### Redis

```
## Установка
$ sudo apt install redis -y
## Помощь
$ redis-cli --help
## Вход
$ redis-cli
## Чтобы не получать ответы в кавычках можно зайти с опцией --raw
$ redis-cli --raw
```

#### `Можно получать или вновить данные не заходя в redis-cli.`
$ redis-cli get key

$ redis-cli set key

$ redis-cli keys "*"

$ redis-cli --raw scan 0


#### `Информация о сервевре`
127.0.0.1:6379> info server

#### `Показать колличество ключей(всего)`
127.0.0.1:6379> info keyspace

#### <ins>`Показать колличество ключей(всего) без входа в redis-cli.`</ins>
```diff
- $ redis-cli --scan | wc -l
```

#### <ins>`Показать все ключи без входа в redis-cli.`</ins>
```diff
- $ redis-cli --scan
```

#### `Создать запись first с ключом 1`
127.0.0.1:6379> set first 1

#### `Прочитать запись по ключу 1`
127.0.0.1:6379> get first

#### `Прочитать запись по ключам 1 2 3`
127.0.0.1:6379> mget first second third

#### `Команда возвращает количество записей, существующих среди перечисленных ключей.`
127.0.0.1:6379> EXISTS key [key ...]

#### `Удалить записи по указанным ключам. Отсутствующие ключи — игнорируются: в ответе вернётся количество удалённых записей.`
127.0.0.1:6379> DEL key [key ...]

#### `Создать запись other key с ключом another value на 20 секунд (EX 20)`
127.0.0.1:6379> SET "other key" "another value" EX 20

#### `Получает значение и удаляет запись`
127.0.0.1:6379> GETDEL key

#### `Получает значение и обновляет время жизни`
127.0.0.1:6379> GETEX key [...]

```
#### Работает только в 7.0.0 и выше

127.0.0.1:6379> EXPIRE key seconds [NX|XX|GT|LT]

NX - только если время истечения не указано
XX - только если время истечения указано
GT - позволяют ввести условие относительно существующего времени истечения — если новое время больше
LT - позволяют ввести условие относительно существующего времени истечения — если новое время меньше

К существующим ключас можно ставить время таким образом 
127.0.0.1:6379> EXPIRE key 60

```

#### `Возвращает оставшееся время жизни значения по указанному ключу (в секундах).`
127.0.0.1:6379> TTL key

#### `Возвращает оставшееся время жизни значения по указанному ключу (в милисекундах).`
127.0.0.1:6379> PTTL key

#### `Обновляет временну́ю метку доступа на чтение указанных ключей (не связано с временем жизни).`
127.0.0.1:6379> TOUCH key [key ...]

#### `Получает информацию о времени, прошедшем с момента предыдущего доступа на чтение указанного ключа.`
127.0.0.1:6379> OBJECT IDLETIME key

#### `Увеличивает число, сохраненное в ключе, на единицу. Если ключ не существует, перед выполнением операции ему присваивается значение 0. Эта операция ограничена 64-битными целыми числами со знаком.`
127.0.0.1:6379> INCR key

#### `Уменьшает число, хранящееся в ключе, на единицу. Если ключ не существует, перед выполнением операции ему присваивается значение 0. Эта операция ограничена 64-битными целыми числами со знаком.`
127.0.0.1:6379> DECR key

#### `Увеличивает число, хранящееся в ключе, на значение после ключа. Если ключ не существует, ему присваивается значение 0. Эта операция ограничена 64-битными целыми числами со знаком.`
127.0.0.1:6379> INCRBY key increment

#### `Уменьшает число, хранящееся в ключе, на значение после ключа. Если ключ не существует, перед выполнением операции ему присваивается значение 0. Эта операция ограничена 64-битными целыми числами со знаком.`
127.0.0.1:6379> DECRBY key decrement

#### `Увеличить или уменьшить строку, представляющую число с плавающей запятой, хранящееся в key, на указанное приращение.`
127.0.0.1:6379> INCRBYFLOAT key increment

#### `Возвращает длину строкового значения, хранящегося в key. Ошибка возвращается, когда ключ содержит нестроковое значение.`
127.0.0.1:6379> STRLEN key

#### `Получить содержимое в указанном диапазоне`
127.0.0.1:6379> GETRANGE key start end

#### `Перезаписать содержимое по указанному смещению`
127.0.0.1:6379> SETRANGE key offset value

#### `Конкатенация`
127.0.0.1:6379> APPEND key value

#### `Добавить несколько ключей одновременно`
127.0.0.1:6379> MSET key value key value

#### `Возвращает список ключей, удовлетворяющих шаблону pattern. Например (KEYS *) вернёт все ключи. Вызывает просадку по производительности.`
127.0.0.1:6379> KEYS pattern

#### `Возвращает список ключей. Например (KEYS 0) вернёт все ключи. НЕ вызывает просадку по производительности.`
127.0.0.1:6379> KEYS 0
#### <ins>https://redis.io/commands/scan/ </ins>

#### `Узнать тип ключа`
127.0.0.1:6379> TYPE key

### List
--------------------- Работа со списком (List) BEGIN ----------------------------------------------------------------------
#### `Добавляет каждый перечисленный элемент в конец (R — "справа") указанного списка.`
127.0.0.1:6379> RPUSH key element [element ...]

#### `Добавляет каждый перечисленный элемент в конец  (L — слева) указанного списка.`
127.0.0.1:6379> LPUSH key element [element ...]

#### `Возвращает длину списка. При отсутствии записи по указанному ключу возвращается 0. Если запись содержит другой тип, то, естественно, это приведёт к ошибке`
127.0.0.1:6379> LLEN key

#### `Для списка, доступного по ключу key вставляет element перед или после (BEFORE или AFTER, соответственно) указанного элемента pivot. Если список пуст (ключ отсутствует), операция не выполняется, а ответом будет -1`
127.0.0.1:6379> LINSERT key BEFORE|AFTER pivot element

#### `Читает и возвращает элемент с указанным индексом.`
127.0.0.1:6379> LINDEX key index

#### `Реализация LINDEX, позволяющая прочитать срез списка: слева направо от элемента с индексом start до элемента с индексом stop — включительно.`
127.0.0.1:6379> LRANGE key start stop

#### `Извлекает (не только читает, но и удаляет) элемент в начале списка и возвращает его. Извлекает (не только читает, но и удаляет) элемент в начале списка и возвращает его`
127.0.0.1:6379> LPOP key [count]

#### `Извлекает (не только читает, но и удаляет) элемент, работает с концом списка, при указании count так же возвращая массив`
127.0.0.1:6379> RPOP key [count]

#### `LTRIM выполняет обрезку списка, оставляя в нём только элементы из указанного между индексами start и stop диапазона (включительно). Логика диапазона работает аналагично LRANGE. Результат всегда OK`
127.0.0.1:6379> LTRIM key start stop

```
При count = 0 удаляет из списка все соответствующие element значения, иначе удаляет не более, чем абсолютное значение count, но направление зависит от знака:

Если count > 0, поиск происходит слева направо
Если count < 0, поиск происходит справа налево

127.0.0.1:6379> LREM key count element
```
#### `Атомарно извлекает крайний правый элемент из списка source, добавляет его в начало (слева) списка destination и возвращает значение этого элемента. `
127.0.0.1:6379> RPOPLPUSH source destination

--------------------- Работа со списком (List) END ----------------------------------------------------------------------

### SET
--------------------- Работа со списком (Set) BEGIN ----------------------------------------------------------------------

#### `Добавляет элемент(ы) в набор. Отвечает количеством созданных элементов.`
127.0.0.1:6379> SADD key member [member ...]

#### `Удаляет элемент(ы), существующие среди перечисленных. Возвращает количество затронутых элементов.`
127.0.0.1:6379> SREM key member [member ...]


#### `Если указанный элемент member не существует в наборе source, то ничего не произойдёт и ответом будет 0. Иначе этот элемент будет удалён из source и добавлен в destination`
127.0.0.1:6379> SMOVE source destination member

#### `Возвращает количество элементов в наборе.`
127.0.0.1:6379> SCARD key

#### `Возвращает 1, если member присутствует в указанном множестве, иначе 0`
127.0.0.1:6379> SISMEMBER key member

#### `Возвращает массив со всеми элементами набора.`
127.0.0.1:6379> SMEMBERS key

#### `Возвращает случайный элемент набора. При наличии аргумента count вместо единственного значения вернётся массив`
127.0.0.1:6379> SRANDMEMBER key [count]

#### `Вычислить объединение (union) всех указанных наборов. Возвращает результат в виде массива (из уникальных элементов среди всех перечисленных наборов)`
127.0.0.1:6379> SUNION key [key ...]

#### `Вычислить пересечение (intersection) всех указанных наборов. Возвращает результат в виде массива (из элементов, которые присутствуют во всех перечисленных наборах)`
127.0.0.1:6379> SINTER key [key ...]

#### `Вычислить разницу (difference) между первым набором и остальными: то есть из набора, указанного первым, "вычесть" элементы, которые есть во всех остальных наборах. Возвращает результат в виде массива (из элементов, которые присутствует только в первом наборе)`
127.0.0.1:6379> SDIFF key [key ...]

--------------------- Работа со списком (Set) END ----------------------------------------------------------------------

### HASH
--------------------- Работа с (Hash) BEGIN ----------------------------------------------------------------------

#### `Создать или обновить в указанном поле его значение`
127.0.0.1:6379> HSET key field value [field value ...]

#### `Получить значение указанного поля. HMGET key field [field ...] позволяет прочитать не одно, а несколько значений из разных полей`
127.0.0.1:6379> HGET key field

#### `Удаляет перечисленные поля. Возвращает количество удалённых элементов.`
127.0.0.1:6379> HDEL key field [field ...]

#### `Возвращает количество записей.`
127.0.0.1:6379> HLEN key

#### `Возвращает 1, если поле существует, иначе 0.`
127.0.0.1:6379> HEXISTS key field

#### `Возвращает длину строки, являющейся значением для указанного поля в hash по указанному ключу. Если ключ отсутствует или такого поля в нём не найдено, ответом будет 0.`
127.0.0.1:6379> HSTRLEN key field

#### `Чтение всех имён полей из hash по указанному ключу.`
127.0.0.1:6379> HKEYS key

#### `Аналогично HKEYS, но читает значения.`
127.0.0.1:6379> HVALS key

#### `Читает весь hash, возвращает одномерный массив, в котором нечётные элементы — имена полей, а чётные — значения.`
127.0.0.1:6379> HGETALL key

--------------------- Работа с (Hash) END ----------------------------------------------------------------------




#### `Возвращает значение message в неизменном виде.`
127.0.0.1:6379> ECHO mEssАge

#### `Возвращает значение message в неизменном виде. Если значение отсутствует, возвращает просто строку "PONG". Разница в том, что PING, в отличие от ECHO, можно вызвать, когда подключение находится в режим pub/sub`
127.0.0.1:6379> PING mEssagE

#### `Возвращает системное время сервера в виде массива из двух элементов: полные секунды от начала эпохи Unix и микросекунды текущей неполной секунды.`
127.0.0.1:6379> TIME

#### `Команда для отключения от сервера. Всегда отвечает "OK". Вызов QUIT говорит серверу, что перед отключением вы хотите дождаться всех этих данных.(завершения обработки любых предыдущих команд и получения результатов их работы)`
127.0.0.1:6379> QUIT


---------------------------------------------------------

https://redis.io/docs/clients/#python

https://redis.io/commands/incrbyfloat/

https://redis.io/commands/ttl/

https://redis.io/download/#redis-downloads

https://github.com/redis/redis/tree/unstable


