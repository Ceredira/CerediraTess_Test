### Предусловия
1. Распаковать релиз
    1. Перейти по ссылке https://github.com/Ceredira/CerediraTess/releases
    2. Скачать с Pre-release архив (например CerediraTess.v.0.5.1.zip)
    3. Создать каталоги bin -> CerediraTess
    4. Распаковать туда все содержимое архива
    5. Создать каталоги data -> CerediraTess
    6. Распаковать туда 3 каталога из архива
    (resources, scripts, www)

2. Создать запускатор для всей этой системы
    1. Создать файл CerediraTess.bat
    2. Внутри него написать следующее:

```
        @echo off
        chcp 6501

        set "CT_BASEDIR=C:\Ceredira\data\CerediraTess"

        "bin\CerediraTess\CerediraTess.exe"
```
где, "bin\CerediraTess\CerediraTess.exe" - это относительный путь к исполняемому файлу. Его можно получить перейдя в bin -> CareDiraTess (куда мы выше скопировали файлы из архива) и найти там файл CerediraTess.exe.

3. Запустить CerediraTess.bat

4. Скопировать IP адрес из консоли (напр. http://192/168...) и вставить его в адресную строку
    * Если в заголовке командной строки появляется слово "Выбрать"/сайт не загружается то нажать клавишу Esc.

5. В браузере чтобы войти ввести:
    - Логин: admin
    - Пароль: admin
