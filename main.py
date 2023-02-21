from loguru import logger
from sys import stderr
from kresko import subscribe_kresko

def main():
    logger.remove()
    logger.add(stderr,
               format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")
    logger.add('logs/log.log',
               format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

    with open('files/proxies.txt') as f:
        all_proxies = f.read().splitlines()

    with open('files/mails.txt') as f:
        all_mails = f.read().splitlines()

    with open('files/registered.txt') as f:
        registered = [f"{row.strip().split(':')[1]}:{row.strip().split(':')[2]}" for row in f]

    with open('files/registered.txt') as file:
        registered_proxies = [row.strip().split(':')[0] for row in file]

    mails = [x for x in all_mails if (x not in registered)]
    proxies = [x for x in all_proxies if (x not in registered_proxies)]

    for proxy, mail in zip(proxies, mails):
        subscribe_kresko(mail, proxy)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.error(err)
