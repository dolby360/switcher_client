import asyncio
import pathlib
import os
import json
import datetime
from aioswitcher.api import SwitcherApi
from aioswitcher.api import Days

CUR_DIR = pathlib.Path(__file__).parent
SCHEDULES_CONF_PATH = os.path.join(CUR_DIR, "schedules.json")
DEVICE_IP = "10.0.0.6"
DEVICE_NAME = "e4bb64"
CONST_TO_DAYS_MAP = {
    "Monday" : Days.MONDAY,
    "Tuesday" : Days.TUESDAY,
    "Wednesday": Days.WEDNESDAY,
    "Thursday": Days.THURSDAY,
    "Friday": Days.FRIDAY,
    "Saturday": Days.SATURDAY,
    "Sunday": Days.SUNDAY
}

async def sleep_until(day: int = 0, hour: int = 0, minute: int = 0, second: int = 0):
    """Asynchronous wait until specific hour, minute and second"""

    current_time = datetime.datetime.today()
    future = current_time + datetime.timedelta(
        days=day, hours=hour, minutes=minute, seconds=second
    )
    if current_time.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    await asyncio.sleep((future - current_time).total_seconds())


def save_schedule(data: list):
    with open(SCHEDULES_CONF_PATH, "w") as schedules:
        schedules.write(json.dumps(data, indent=4))


async def restore_schedules():
    with open(SCHEDULES_CONF_PATH, "r") as schedules:
        data = json.load(schedules)
    async with SwitcherApi(DEVICE_IP, DEVICE_NAME) as swapi:
        for item in data:
            d = set([CONST_TO_DAYS_MAP[i] for i in item["days"]])
            await swapi.create_schedule(
                start_time=item["start"], end_time=item["end"], days=d
            )


async def func():
    # TODO: cache the water heater IP and names and if changed go search them.
    async with SwitcherApi(DEVICE_IP, DEVICE_NAME) as swapi:
        data_to_save = []
        all_schedules = await swapi.get_schedules()
        for schedule in all_schedules.schedules:
            data_to_save.append(
                {
                    "days": [item.name for item in schedule.days],
                    "start": schedule.start_time,
                    "end": schedule.end_time,
                }
            )
            await swapi.delete_schedule(schedule.schedule_id)
        save_schedule(data_to_save)
    await sleep_until(second=6)
    await restore_schedules()


if __name__ == "__main__":
    asyncio.run(func())
