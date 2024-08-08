from pydantic import Field

from eventiq.models import CloudEvent


class TraceContextCloudEvent(CloudEvent):
    tracecontext: dict[str, str] = Field({}, description="Distributed tracing context")

    @property
    def extra_span_attributes(self) -> dict[str, str]:
        return {}
