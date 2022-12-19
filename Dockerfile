FROM python:3.10-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
CMD poetry run python src/