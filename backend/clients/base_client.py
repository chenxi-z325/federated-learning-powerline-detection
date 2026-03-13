class BaseClient:
    """
    A base class for federated learning clients.
    """
    def __init__(self, client_id):
        self.client_id = client_id

    def start(self):
        raise NotImplementedError("Subclasses should implement this method!")

    def communicate(self, data):
        raise NotImplementedError("Subclasses should implement this method!")