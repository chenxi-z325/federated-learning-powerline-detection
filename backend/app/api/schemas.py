from pydantic import BaseModel


class ClientModel(BaseModel):
    id: int
    name: str
    status: str
    metrics: dict

class MetricsModel(BaseModel):
    accuracy: float
    loss: float
    precision: float
    recall: float

class GlobalMetricsModel(BaseModel):
    global_accuracy: float
    global_loss: float
    total_clients: int
    metrics: MetricsModel