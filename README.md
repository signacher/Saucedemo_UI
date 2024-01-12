# Main_Project
Для запуска тестов нужно перейти  в директорию с тестами \tests
Для работы в корневом каталоге проекта создать папки logs и screen

Запуск всех тестов:
pytest -s -v  -p no:warnings

Запуск отдельного файла с тестами:
pytest -s -v  -p no:warnings {имя_файла} Запуск отдельного файла с тестами
 
Запуск отдельного теста в файле
 pytest -s -v  -p no:warnings -k  {имя_теста}

Запуск всех тестов с формированием файлов для отчета Allure(файлы сохраняются в указанной папке test_result)
 pytest --alluredir=test_result/ tests/

Отчет на mail
java "-DconfigFile=notifications/config.json" -jar notifications/allure-notifications-4.2.1.jar


