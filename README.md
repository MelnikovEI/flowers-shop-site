# [Сайт доставки цветочных букетов в Красноярске](https://alexmashukov.ru/)

Закажите доставку праздничного букета, собранного специально для ваших друзей, родственников или возлюбленных. Наделим букет смыслом, сделаем его главным подарком на празднике.

![скриншот сайта](https://downloader.disk.yandex.ru/preview/d2a0975044fae6fd5fe005fa509f7dcd5cb158c9a3b0158b296f22ce02793482/64ec65c0/sFOYBx1fwC4_nosd-W_nkPrqdtkupRZCc2xLScRK38CYGVNFAzsJGQKbwHi7A5skPlq2fwGVAhlAhD_MvDY9lg%3D%3D?uid=0&filename=Flower-shop-site.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

## Как запустить сайт

Скачайте код:
```sh
git clone https://github.com/MelnikovEI/flowers-shop-site.git
```

Перейдите в каталог проекта:
```sh
cd flowers-shop-site
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.8  
Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.   
В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:  
- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменные окружения. Создать файл `.env` в каталоге `star_burger/` и положите туда такой код:
- `DEBUG=FALSE` - отключить режим отладки, для включения - TRUE
- `SECRET_KEY=django-insecure-zjf(7%&g@_(a4jrxgi#0(l$#0kpg=b9w3c%j&y#e7l59)g5ak&` - замените на свой ключ
- `ALLOWED_HOSTS=127.0.0.1,localhost` - добавьте через запятую без пробела IP вашего сервера, домен

Создайте файл базы данных SQLite и отмигрируйте её следующей командой:
```sh
python manage.py migrate
```

Запустите сервер:
```sh
python manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
