<table width="100%" border='0'>
 <tr><td width="30%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/saucedemo.png" title="shop" alt="Saucedemo" width="200" height="200"/></td><td valign="middle">
 <h2>Пример организации автотестирования для онлайн магазина <a target="_blank" href="https://www.saucedemo.com/">www.saucedemo.com</a></h2>
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
- [x] Сценарий покупки товара "Sauce Labs Backpack"
- [x] Сценарий покупки товара Sauce Labs Bike Light
- [x] Проверка перехода в пункт меню About
- [x] Заведомо падающий тест (для красивого отчета)

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

Отчет о прохождении теста доступен по ссылке <a target="_blank" href="https://signacher.github.io/saucedemo_ui"> https://signacher.github.io/saucedemo_ui/</a>
*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество прогнанных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты 
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют

###### Главный экран (Owerwiev)
![Screen Allure1](images/AllureReport1.jpg)
###### Пример описания шагов теста
![Screen Allure2](images/AllureReport2.jpg)







