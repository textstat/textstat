=========
Changelog
=========

- :release:`0.7.2 <2021-08-11>`
- :feature:`144` Added exception handling for ``ZeroDivisionErrors``.
- :feature:`147` Added Arabic readability support
- :feature:`142` Added Indice Gulpease index for Italian language support
- :feature:`141` Added German readability support
- :bug`143`: Update ``dale_chall_readability_score`` to use new ``syllable_threshold=`` kwarg.
- :release:`0.7.1 <2021-05-20>`
- :bug`138` Improved performance of ``difficult_words`` function.
- :release:`0.7.0 <2020-11-22>`
- :feature:`129` Added Fernandez-Huerta test.
- :feature:`129` Added szigriszt-Pasos formula.
- :feature:`129` Added Gutierrez-Polini index.
- :feature:`129` Added Crawford's formula.
- :feature:`129` Added cache clear method.
- :feature:`135` Added ``is_difficult_word`` and ``is_easy_word`` functions.
- :release:`0.6.2 <2020-04-23>`
- :bug:`-` Hotfix: add missing resource files.
- :release:`0.6.1 <2020-04-22>`
- :feature:`123` Added cache clear method.
- :feature:`120` Added support for different languages in ``difficult_words``.
- :release:`0.6.0 <2020-01-04>`
- :feature:`103` Dropped support for Python 2 🎉.
- :feature:`100` Switched to using Pythons built-in LRU cache.
