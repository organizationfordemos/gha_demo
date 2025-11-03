# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /src

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml poetry.lock /src/

# Install dependencies
RUN poetry install --no-root --no-interaction

# Copy the rest of the code
COPY . /src

# Default command
CMD ["poetry", "run", "python", "src/functions.py"]
