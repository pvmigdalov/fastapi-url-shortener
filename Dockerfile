FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt update && apt upgrade -y

WORKDIR /fastapi-url-shortener

COPY ./pyproject.toml ./uv.lock .

RUN uv sync

COPY . . 

CMD ["uv", "run", "-m", "app.main"]