<table width="100%" border='0'>
 <tr><td width="20%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/saucedemo.png" title="shop" alt="Saucedemo" width="200" height="200"/></td><td valign="middle">
 <h1>Пример организации автотестирования для онлайн магазина <a target="_blank" href="https://www.saucedemo.com/">www.saucedemo.com</a></h1>
 </td></tr>
</table>

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Реализованные проверки](#ballot_box_with_check-реализованные-проверки)
- [Как запускать тесты](#on-как-запускать-тесты)
- [Allure отчет](#bar_chart-allure-отчет-о-прохождении-тестов)
  
## :heavy_check_mark: Описание:
>В этом репозитории:
>- Демо-проект с примерами автотестов, написанных на языке <code>Python</code> с помощью библиотеки <code>Selenium</code>.
>- Тесты запускаются в браузере Chrome в Headless режиме с помошью <code>Github Actions</code>.
>- Пайплайн запуска настроен в файле `run_tests.yaml`, который расположен в папке `.github/workflows`
>- Формируется <code>Allure отчет</code> о результатах прохождения тестов с историей запусков публикуется в <code>Github Pages</code> <a target="_blank" href="https://signacher.github.io/saucedemo_ui"> Ссылка на отчет</a>

## :gear: Технологии и инструменты:
<div align="center">
  <img src="https://github.com/signacher/signacher/blob/main/images/python.png" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/selenium.png" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/github.png" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/actions1.png" title="Github Actions" alt="Github Actions" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/yaml.png" title="yaml" alt="yaml" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure.png" title="Allure" alt="Allure" width="40" height="40"/>&nbsp;
</div>

## :ballot_box_with_check: Реализованные проверки:
- [x] vj;tn gbcfnm
- [x]

## :on: Как запускать тесты:

>1. Перейти во вкладку `Actions`
>2. В левом меню выбрать воркфлоу `Saucedemo UI tests`
>3. Выбрать в выпадающем списке какие тесты будут запускаться
>   - `All tests` - будут запущены все тесты
>   - `Buy tests` - будут запущены тесты покупки товаров
>4. Нажать **Run workflow**
>5. Дождаться завершения пайплайна и можно смотреть отчет о пройденных тестах

![Screen Actions1](images/run_actions.png)

## :bar_chart: Allure отчет о прохождении тестов




