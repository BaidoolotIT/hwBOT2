from aiogram.utils import executor
from config import dp
import logging

from handlers import client, extra, callback

client.register_handlers_client(dp)
extra.register_handlers_extra(dp)
callback.register_handlers_callback(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)