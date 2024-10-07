# qa_guru_python_hw_9

#Задание
Провести рефакторинг своего теста на регистрацию студента по форме https://demoqa.com/automation-practice-form, используя инструменты объектно-ориентированной парадигмы для инкапсуляции деталей реализации бизнес-шагов пользователя, таким образом реализовав идеи шаблона PageObject.

Задание состоит из нескольких частей, каждую из которых следует сдавать в виде отдельной ссылки на соответствующую бренчу в репозитории с тестами на приложение demoqa (все ссылки в одном сообщении в комментариях ниже).



ЧАСТЬ I (реализовать в бренче mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).

Дополнительные условия и подсказки:

* Все элементы выносить в отдельные поля объекта класса не обязательно, но стоит это сделать с теми элементами, которые будут повторяться.

* Класс для PageObject должен лежать в выделенном модуле в выделенном пакете внутри проекта, как было показано на уроке



ЧАСТЬ II (реализовать в бренче high-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «отправить форму с данными» или другими словами «провести регистрацию через форму». Также шагом считаем подтверждение результата проделанной работы (как например, подтверждение, что регистрация прошла успешно).



Также в этой части следует провести рефакторинг работы с данными пользователя, представив их в виде объекта датакласса, используя уже имеющиеся знания из предыдущих уроков.

Дополнительные условия и подсказки:

* Не обязательно на уровне с высокоуровневыми шагами типа .register(user) добавлять в PageObject средне-уровневые шаги типа .fill_email(user.email), но можно

  * если их добавлять – это будет сделать не сложно, просто скопировав из предыдущей версии решения из Часть I, – то возможно их стоит сделать "приватными" (добавив перед именем подчеркивание), чтобы не дать возможность в тесте – миксовать подход, а использовать только высокоуровневые шаги, но можно и не вводить такое ограничение.

  * вероятно, проще вместо добавления таких средне-уровневых шагов из Часть I – добавить в init поля объекта для всех элементов и переиспользовать их внутри реализации .register(user). Таким образом реализация будет более лаконичная и все еще достаточно гибкая, чтобы в будущем иметь доступ к элементам в контексте других "бизнес задач" на этой странице.

* Классы для PageObject и модели данных должны лежать в выделенных модулях в выделенных пакетах внутри проекта, как было показано на уроке 😉

* При реализации модели данных для реализации тех или иных полей будет неплохо использовать специальные типы данных, например, для даты использовать datetime.date, а для хобби использовать Enum 😉 Если пока не хватает знаний, сделай как можешь, или посмотри разбор этого домашнего задания когда оно будет доступно.





Часть III – ДОПОЛНИТЕЛЬНО/НЕ-ОБЯЗАТЕЛЬНО (реализовать в бренче application-manager)

* добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box  и соответствующий PageObject. 

  * Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.

  * в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(), который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')

    * cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера
