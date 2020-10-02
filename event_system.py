class EventSystem:
    subscribers = []

    @staticmethod
    def emit(message, emitter=None, data=None):
        for s in EventSystem.subscribers:
            s.receive(message, emitter, data)

    @staticmethod
    def subscribe(subscriber):
        EventSystem.subscribers.append(subscriber)
