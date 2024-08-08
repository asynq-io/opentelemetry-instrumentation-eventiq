from opentelemetry.instrumentation.eventiq import TraceContextCloudEvent


def test_create_trace_context_ce():
    ce = TraceContextCloudEvent.new("Some data", topic="test.topic")
    assert isinstance(ce, TraceContextCloudEvent)
    assert ce.extra_span_attributes == {}
