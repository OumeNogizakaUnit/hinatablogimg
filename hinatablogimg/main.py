# vi: set et sw=4 ts=4 softtabstop=4 :
import sys
import click
import logging
import logging.config
import yaml
from dotenv import load_dotenv
from pathlib import Path

from hinatablogimg import __name__ as modname
from hinatablogimg import __version__ as modversion
from hinatablogimg import LOGCONFPATH
from hinatablogimg.utils import fetch_one_page


@click.command()
@click.option('--startpage',
              type=click.IntRange(0),
              default=0,
              show_default=True,
              help='探索開始ページ')
@click.option('--endpage',
              type=click.IntRange(0),
              default=3,
              show_default=True,
              help='探索終了ページ')
@click.option('--logpath',
              type=click.Path(exists=False),
              default='./log/hinatablogimg.log',
              show_default=True,
              help='ログファイル出力先パス')
@click.option('--loglevel',
              default='INFO',
              type=click.Choice(['DEBUG', 'INFO',
                                 'WARNING', 'ERROR', 'CRITICAL'],
                                case_sensitive=False),
              show_default=True,
              help='ログレベル')
@click.argument('savedir',
                type=click.Path(exists=True))
@click.version_option(modversion, prog_name=modname)
def main(startpage,
         endpage,
         logpath,
         loglevel,
         savedir):
    '''
Argument:

    SAVEDIR\t\t探索画像保存先パス
    '''
    load_dotenv()
    logger = load_logger(logpath=logpath)
    logger.setLevel(loglevel)
    for i in range(startpage, endpage+1):
        logger.debug(f"{i}ページ目の処理開始")
        try:
            fetch_one_page(i, savedir)
        except Exception as error:
            logger.error(error)
            sys.exit(1)


def load_logger(logpath=None):
    logconfpath = Path(LOGCONFPATH)
    if logconfpath.exists():
        with logconfpath.open() as fd:
            confdata = yaml.safe_load(fd)
            if logpath:
                try:
                    confdata['handlers']['filehandler']['filename'] = logpath
                except KeyError as error:
                    sys.stderr.write(error)
            logging.config.dictConfig(confdata)
    return logging.getLogger(modname)


if __name__ == '__main__':
    main()
