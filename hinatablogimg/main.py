# vi: set et sw=4 ts=4 softtabstop=4 :
import sys
import logging
import logging.config
import yaml
from dotenv import load_dotenv
from pathlib import Path
from tqdm import tqdm

from hinatablogimg import __name__ as modname
from hinatablogimg import (HINATADIR,
                           LOGCONFPATH)
from hinatablogimg.utils import fetch_one_page


def main():
    load_dotenv()
    logger = load_logger()
    maxpage = 3
    for i in tqdm(range(maxpage)):
        logger.debug(f"{i}ページ目の処理開始")
        try:
            fetch_one_page(i, HINATADIR)
        except Exception as error:
            logger.error(error)
            sys.exit(1)

def load_logger():
    logpath = Path(LOGCONFPATH)
    if logpath.exists():
        with logpath.open() as fd:
            confdata = yaml.safe_load(fd)
            print(confdata)
            logging.config.dictConfig(confdata)
    print(modname)
    return logging.getLogger(modname)


if __name__ == '__main__':
    main()
