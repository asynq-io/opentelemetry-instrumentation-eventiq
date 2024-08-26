from pydantic import Field

from eventiq.models import CloudEvent, D


class TraceContextCloudEvent(CloudEvent[D]):
    tracecontext: dict[str, str] = Field({}, description="Distributed tracing context")

    @property
    def extra_span_attributes(self) -> dict[str, str]:
        return {}
