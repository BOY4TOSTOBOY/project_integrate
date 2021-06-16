.. _code_style:

Форматирование кода(coding style)
=================================


Основные правила
----------------

Следуйте этим конвенциям при в ходе работы на текущем проекте:

- `PEP8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_
- `PEP257 -- Docstring Conventions <https://www.python.org/dev/peps/pep-0257/>`_
- `Django Coding Style <https://docs.djangoproject.com/en/3.0/internals/contributing/writing-code/coding-style/>`_
- `Django Best Practices <https://django-best-practices.readthedocs.io/en/latest/code.html>`_

Дополнительные ресурсы
~~~~~~~~~~~~~~~~~~~~~~

- `Code Like a Pythonista <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`_ - рекомендовано к прочтению.


Расположение кода
-----------------

При разработке коде руководствуйтесь этими правилами:

* Код в **model method** - если код отсылает к конкретному экземпляру модели
* Код в **manager method** - если код затрагивает таблицу(модель) целиком
* Код в **form method/serializator** - если код валидирует и производит предобработку данных из запроса
* Код в **CBV method** который заторагивает обработку запроса
* In **utils.py**, code not directly related to the project
* В **utils.py**, сторонний код напрямую не относящийся архитектуре Django/DRF


Модели
---------

Предпочитаемый порядок атрибутов и методов в
модели(с разделительной строкой между пунктами):

* константы (Для :code:`choices` и др.)
* поля модели
* :code:`custom manager indication`
* :code:`Meta`
* :code:`def __unicode__` (python 2) or :code:`def __str__` (python 3)
* другие магические методы
* :code:`def clean`
* :code:`def save`
* :code:`def get_absolut_url`
* другие методы

Имена классов
--------------

* Имена классов должны соответствовать следующему шаблону::

  '%s%sView' % (class_name, verb)

Например, :code:`ProductUpdateView, OfferCreateView and PromotionDeleteView`.
Это подходит не под все ситуации, но это хорошее начало.
