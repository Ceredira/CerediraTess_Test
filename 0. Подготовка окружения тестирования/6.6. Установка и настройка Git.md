**Установка и настройка Git**

1. В браузере открыть [ссылку](https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/PortableGit-2.35.1.2-64-bit.7z.exe)

2. Скачать архив. Для некоторых браузеров может открыться окно выбора расположения для сохранения (каталог Загрузки по умолчанию). Выбрать каталог и нажать на кнопку Сохранить

3. Создать папку в директории C:\Ceredira\bin с названием 'Git'

4. Распаковать содержимое архива в папку C:\Ceredira\bin\Git (вставить этот путь в диалоговое окно архиватора при запросе директории)

5. Перейти в каталог C:\Ceredira\bin\Git\ и запустить фаил git-bash.exe

6. В появившемся окне ввести команду git config --global init.defaultBranch master затем нажать <kbd>Enter</kbd>

7. Далее ввести команду git config --global user.name "FIRST_NAME LAST_NAME" где "FIRST_NAME LAST_NAME" == ваш "ник" на github, затем нажать <kbd>Enter</kbd>

9. Далее ввести команду git config --global user.email "MY_NAME@example.com" где "MY_NAME@example.com" == ваш email на который зарегестрирован github, затем нажать <kbd>Enter</kbd>

13. Перейти в каталог C:\Ceredira\bin\Git\cmd и запустить фаил git-gui.exe

14. В появившемся окне выбрать пункт 'Clone existing repository'

15. Далее в поле 'Source Location' скопировать https://github.com/Ceredira/CerediraTess_Test.git

16. В поле 'Target Directory' ввести C:\Ceredira\repository\CerediraTess_Test

17. Нажать кнопку <kbd>Clone</kbd>, репозиторий должен скопироваться к вам на машину

**Теперь, мы научимся пушить файлы в репозиторий.**

1. Создать необходимый фаил в каталоге C:\Ceredira\repository\CerediraTess_Test\условная папка

2. Перейти в каталог C:\Ceredira\bin\Git\cmd и запустить фаил git-gui.exe

3. На цетральной панели нажать кнопку <kbd>Rescan</kbd>, чтобы мы увидели вносимые изменения

4. На цетральной панели нажать кнопку <kbd>Stage Changed</kbd> затем кнопку <kbd>Да</kbd> чтобы увидеть содержимое вашего файла

5. Для настройки корректного отоображения в верхнем меню выбрать пункт 'Edit' > 'Options'

6. В появившемся окне в пункте 'Default File Contents Encodng' нажать кнопку <kbd>Change</kbd> и выбрать пункт 'Unicode (UTF-8)' (пройти данный шаг необходимо в двух колонках), затем нажать кнопку <kbd>Save</kbd>

7. В поле 'Commit message' ввести комментарий, на цетральной панели нажать кнопку <kbd>Commit</kbd>

8. На цетральной панели нажать кнопку <kbd>Push</kbd>, в появившемся окне так же нажать <kbd>Push</kbd>

9. На шаге 'Credential Helper Selector' выбрать радиобаттон 'Wincred', отметить внизу чекбокс 'Always use..', затем нажать кнопку <kbd>Select</kbd>

10. На шаге 'OpenSSH' в поле 'Username' ввести ваш юзернейм с гитхаб, затем нажать кнопку <kbd>Ok</kbd>

11. На шаге 'OpenSSH' в поле 'Password' ввести ваш пароль с гитхаб, затем нажать кнопку <kbd>Ok</kbd>

11. Далее ввести команду git config --global credential.helper manager-core затем нажать <kbd>Enter</kbd>

12. Нажать на кнопку Push
13. В появившемся окне Connect to GitHub нажать на кнопку Sign in with your browser
14. Браузер открылся на странице https://github.com/login?client_id=
15. В поле Username or email address ввести имя пользователя
16. В поле Password ввести пароль пользователя
17. Нажать на кнопку Sign In

