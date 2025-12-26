FROM python:3.13.5
WORKDIR /code


RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml ./
COPY uv.lock ./

RUN uv sync --frozen

COPY predict.py .
COPY stroke-prediction-model.bin .

EXPOSE 32000

ENTRYPOINT ["uv", "run", "gunicorn", "predict:app", "-b", "0.0.0.0:32000"]