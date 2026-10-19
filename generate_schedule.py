"""Generate countdown_schedule.json (date -> message) for the iPhone Shortcut."""

import json
import random
import sys
from datetime import date, timedelta
from pathlib import Path

from messages import FINAL, REGULAR, SPECIAL

HERE = Path(__file__).parent
FINAL_STRETCH = 20


class Picker:
    """Draws templates from a shuffled pool, refilling once it is exhausted."""

    def __init__(self, pool, rng):
        self.pool, self.rng, self.queue, self.last = pool, rng, [], None

    def next(self):
        if not self.queue:
            self.queue = self.pool[:]
            self.rng.shuffle(self.queue)
            # Avoid repeating the previous template across a refill boundary.
            if len(self.queue) > 1 and self.queue[-1] == self.last:
                self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.last = self.queue.pop()
        return self.last


def should_post(days_left):
    return days_left > 0 and (days_left <= FINAL_STRETCH or days_left % 10 == 0)


def build_schedule(cfg):
    trip = date.fromisoformat(cfg["trip_date"])
    start = date.fromisoformat(cfg["start_date"]) if cfg.get("start_date") else date.today()
    rng = random.Random(cfg.get("seed"))
    regular, final = Picker(REGULAR, rng), Picker(FINAL, rng)
    back = date.fromisoformat(cfg["return_date"]) if cfg.get("return_date") else None
    fields = {
        "destination": cfg["destination"],
        "emoji": cfg.get("emoji", ""),
        "flight_time": cfg.get("flight_time", ""),
        "trip_date": trip.strftime("%d %b"),
        "nights": (back - trip).days if back else "",
        "return_date": back.strftime("%d %b") if back else "",
        "return_flight_time": cfg.get("return_flight_time", ""),
    }

    schedule = {}
    d = start
    while d < trip:
        days_left = (trip - d).days
        if should_post(days_left):
            if days_left in SPECIAL:
                template = SPECIAL[days_left]
            elif days_left <= FINAL_STRETCH:
                template = final.next()
            else:
                template = regular.next()
            schedule[d.isoformat()] = template.format(days=days_left, **fields)
        d += timedelta(days=1)
    return schedule


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252
    cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
    schedule = build_schedule(cfg)
    out = HERE / "countdown_schedule.json"
    out.write_text(json.dumps(schedule, ensure_ascii=False, indent=2), encoding="utf-8")

    trip = date.fromisoformat(cfg["trip_date"])
    for day, msg in schedule.items():
        print(f"{day}  ({(trip - date.fromisoformat(day)).days:>3} left)  {msg}")
    print(f"\n{len(schedule)} posts written to {out}")


if __name__ == "__main__":
    main()
