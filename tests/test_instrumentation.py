from eventiq import Service
from eventiq.backends.stub import StubBroker
from opentelemetry.instrumentation.eventiq import EventiqInstrumentator
from opentelemetry.test.test_base import TestBase


class TestEventiqInstrumentation(TestBase):
    def test_auto_instruments(self):
        EventiqInstrumentator().instrument()
        self.assertEqual(len(Service.default_middlewares), 2)
        EventiqInstrumentator().uninstrument()
        self.assertEqual(len(Service.default_middlewares), 0)

    def test_instrument_service(self):
        service = Service(name="example-service", broker=StubBroker.from_env())
        EventiqInstrumentator().instrument_service(service)
        self.assertEqual(len(service.middlewares), 2)
        EventiqInstrumentator().uninstrument_service(service)
        self.assertEqual(len(service.middlewares), 0, service.middlewares)
