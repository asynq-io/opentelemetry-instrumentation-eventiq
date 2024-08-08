![Tests](https://github.com/asynq-io/opentelemetry-instrumentation-eventiq/workflows/Tests/badge.svg)
![Build](https://github.com/asynq-io/opentelemetry-instrumentation-eventiq/workflows/Publish/badge.svg)
![License](https://img.shields.io/github/license/asynq-io/opentelemetry-instrumentation-eventiq)
![Mypy](https://img.shields.io/badge/mypy-checked-blue)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![Python](https://img.shields.io/pypi/pyversions/opentelemetry-instrumentation-eventiq)
![Format](https://img.shields.io/pypi/format/opentelemetry-instrumentation-eventiq)
![PyPi](https://img.shields.io/pypi/v/opentelemetry-instrumentation-eventiq)

# opentelemetry-instrumentation-eventiq

Opentelemetry instrumentation for eventiq

## Installation

```shell
pip install opentelemetry-instrumentation-eventiq
```

## Usage

```python
from eventiq import Service
from opentelemetry.instrumentation.eventiq import EventiqInstrumentor, TraceContextCloudEvent, OpenTelemetryTracingMiddleware

EventiqInstrumentor().instrument()
# or directly instrument a service instance
service = Service(...)
EventiqInstrumentor().instrument_service(service)
# or by manually adding middleware
service.add_middleware(OpenTelemetryTracingMiddleware)

@service.subscribe(topic="example.topic")
async def handler(message: TraceContextCloudEvent):
    print(message.data, message.tracecontext)
```

## Classes
- `EventiqInstrumentor` - Opentelemetry instrumentor for eventiq
- `OpenTelemetryTracingMiddleware` - Middleware for tracing messages with OpenTelemetry
- `OpenTelemetryMetricsMiddleware` - Middleware for exporting metrics with OpenTelemetry
- `TraceContextCloudEvent` - CloudEvent extension for OpenTelemetry trace context
