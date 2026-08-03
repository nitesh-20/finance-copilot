# Stage 1: Build python dependencies
FROM python:3.13-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libfreetype6-dev \
    libfontconfig1-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-equity.txt .
RUN pip install --no-cache-dir --user -r requirements-equity.txt

# Stage 2: Final runtime container
FROM python:3.13-slim

WORKDIR /app

# Install runtime system dependencies for wkhtmltopdf, weasyprint, and matplotlib
RUN apt-get update && apt-get install -y --no-install-recommends \
    wkhtmltopdf \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    shared-mime-info \
    libfreetype6 \
    libfontconfig1 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Copy installed site-packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application source code
COPY . .

# Set dynamic default environment port and configurations
ENV PORT=8001
EXPOSE 8001

CMD ["sh", "-c", "uvicorn finance_copilot_equity.web_app.main:app --host 0.0.0.0 --port ${PORT}"]

