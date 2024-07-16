from opentelemetry.instrumentation.instrumentor import BaseInstrumentor

from eventiq.broker import Broker

from ._middleware import OpenTelemetryMiddleware


class EventiqInstrumentator(BaseInstrumentor):
    def _instrument(self, **kwargs):
        tracer_provider = kwargs.get("tracer_provider")
        record_exceptions = kwargs.get("record_exceptions", True)
        middleware = OpenTelemetryMiddleware(tracer_provider, record_exceptions)
        Broker.default_middlewares.append(middleware)

    def _uninstrument(self, **kwargs):
        for middleware in Broker.default_middelwares:
            if isinstance(middleware, OpenTelemetryMiddleware):
                Broker.default_middlewares.remove(middleware)
