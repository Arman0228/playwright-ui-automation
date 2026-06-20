# UI Autotests (Playwright + PyTest)

Фреймворк UI-автотестов на **Playwright + PyTest + Pydantic Settings + Allure**.

Тестируется демо-приложение [QA Automation Engineer UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course).

## Архитектура

```
pages/          # Page Object Model
components/     # Переиспользуемые UI-блоки (формы, navbar, sidebar)
elements/       # Базовые элементы (Button, Input, Link)
fixtures/       # PyTest fixtures (browser, pages, allure)
tools/          # Routes, logger, playwright helpers
config.py       # Pydantic Settings (.env)
tests/          # Тесты по фичам (authentication, dashboard, courses)
```

## Быстрый старт

```bash
git clone https://github.com/Arman0228/autotests-ui.git
cd autotests-ui
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
pytest -m regression -v
```

## Конфигурация

Скопируйте `.env.example` → `.env` и при необходимости измените:

| Переменная | Описание |
|------------|----------|
| `APP_URL` | URL тестируемого приложения |
| `HEADLESS` | `true` / `false` |
| `BROWSERS` | Список браузеров: `["chromium"]` |
| `TEST_user.EMAIL` | Email тестового пользователя |
| `TEST_user.USERNAME` | Username |
| `TEST_user.PASSWORD` | Password |

## Запуск

```bash
# Regression suite
pytest -m regression -v

# Smoke
pytest -m smoke -v

# Параллелльно (2 воркера)
pytest -m regression -n 2

# Allure report
pytest -m regression --alluredir=allure-results
allure serve allure-results
```

## CI

GitHub Actions (`.github/workflows/tests.yml`):
- прогон regression-тестов на push/PR
- UI coverage report + Allure → GitHub Pages

## Стек

Python 3.11 · Playwright · PyTest · Pydantic Settings · Allure · pytest-xdist · ui-coverage-tool
