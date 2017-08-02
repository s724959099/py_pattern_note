class EventHelper:
    events = []
    trigger_events = []

    @classmethod
    def __listen_events(cls, events, key, fn):
        if any(obj["key"] == key for obj in events):
            for item in events:
                if item["key"] == key:
                    item["listeners"].append(fn)
                    break
        else:
            events.append({
                "key": key,
                "listeners": [fn]
            })

    @classmethod
    def listen(cls, key, fn, accept_before_trigger=False):
        cls.__listen_events(cls.events, key, fn)
        if accept_before_trigger:
            for item in cls.trigger_events:
                if item["key"] == key:
                    fn(*item["args"], **item["kwargs"])
                    break

    @classmethod
    def __trigger_event(cls, key, *args, **kwargs):
        if any(obj["key"] == key for obj in cls.trigger_events):
            for item in cls.trigger_events:
                if item["key"] == key:
                    item.update({
                        "args": args,
                        "kwargs": kwargs
                    })
                    break
        else:
            cls.trigger_events.append({
                "args": args,
                "kwargs": kwargs,
                "key": key,
            })

    @classmethod
    def trigger(cls, key, *args, **kwargs):
        for item in cls.events:
            if item["key"] == key:
                for fn in item["listeners"]:
                    fn(*args, **kwargs)
                break

        cls.__trigger_event(key, *args, **kwargs)


def fn1():
    print("fn1")


def fn2():
    print("fn2")


def fn3():
    print("fn3")


EventHelper.listen("fn", fn1)
EventHelper.trigger("fn")
EventHelper.listen("fn", fn2, accept_before_trigger=True)
