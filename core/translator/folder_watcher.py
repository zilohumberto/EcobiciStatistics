import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from core.translator.translator import Translator
from core.settings import (EXTERNAL_PATH,
                           EXTERNAL_PATH_WATCHER_INTERVAL_SECONDS,
                           EXTERNAL_PATH_WITH_ERRORS_PATH,
                           EXTERNAL_PATH_WITH_SUCCESS_PATH)
from core.utils import convert_to_string


class FileHandler(object):

    patters = ['.csv']
    translator = Translator()

    @staticmethod
    def process_all_files_in_folder():
        only_patters_file = [
            os.path.join(EXTERNAL_PATH, f) for f in os.listdir(EXTERNAL_PATH)
            if (os.path.isfile(os.path.join(EXTERNAL_PATH, f)) and
                os.path.splitext(f)[1].lower() in FileHandler.patters)
        ]
        for patterns_file in only_patters_file:
            FileHandler.process(patterns_file)

    @staticmethod
    def process(file_to_translate):
        try:
            FileHandler.translator.translate(file_to_translate)
        except Exception as e:
            FileHandler.move_with_timestamp(file_to_translate,
                                            EXTERNAL_PATH_WITH_ERRORS_PATH)
        finally:
            if os.path.isfile(file_to_translate):
                FileHandler.move_with_timestamp(file_to_translate,
                                                EXTERNAL_PATH_WITH_SUCCESS_PATH)

    @staticmethod
    def move_with_timestamp(file_to_translate, destination_path):
        time_string = '-' + convert_to_string(datetime.now())
        old_name = os.path.splitext(os.path.basename(file_to_translate))
        rename = os.path.join(destination_path, old_name[0] + time_string + old_name[1])
        os.rename(file_to_translate, rename)


if __name__ == '__main__':
    FileHandler.process_all_files_in_folder()
    scheduler = BlockingScheduler()
    scheduler.add_job(
        FileHandler.process_all_files_in_folder, trigger='interval',
        seconds=EXTERNAL_PATH_WATCHER_INTERVAL_SECONDS, id='translator'
    )
    scheduler.start()
