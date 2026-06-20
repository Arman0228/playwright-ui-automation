# UI Autotests (Playwright + PyTest)

Фреймворк UI-автотестов на **Playwright + PyTest + Pydantic Settings + Allure**.

Тестируется демо-приложение [QA Automation Engineer UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course).

## Portfolio

| Проект | Описание |
|--------|----------|
| **UI** (этот repo) | [playwright-ui-automation](https://github.com/Arman0228/playwright-ui-automation) |
| **API** | [pytest-api-automation](https://github.com/Arman0228/pytest-api-automation) |
| **LLM QA** | [llm-qa-automation-framework](https://github.com/Arman0228/llm-qa-automation-framework) |

## Архитектура

```
pages/              # Page Object Model
components/         # UI-блоки (forms, navbar, sidebar)
elements/           # Button, Input, Link (Component Factory)
fixtures/           # browser, pages, allure
tests/
  authentication/   # TestPositiveAuthorization / TestNegativeAuthorization
  dashboard/      # TestPositiveDashboard
  courses/        # TestPositiveCourses
scripts/            # Playwright learning examples (не часть CI suite)
tests/pytest/       # PyTest learning examples (не часть CI suite)
```

## Быстрый старт

```bash
git clone https://github.com/Arman0228/playwright-ui-automation.git
cd playwright-ui-automation
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
pytest -m regression -v
```

## Запуск

```bash
pytest -m positive -v          # happy path
pytest -m negative -v          # validation / error cases
pytest -m smoke -v             # smoke suite
pytest -m regression -n 2 -v   # parallel regression
pytest -m regression --alluredir=allure-results
```

## CI

GitHub Actions — regression на push/PR, Allure + UI coverage → GitHub Pages.

## Стек

Python 3.11 · Playwright · PyTest · Pydantic Settings · Allure · pytest-xdist
