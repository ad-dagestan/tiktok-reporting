import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    setup_logging()
    logging.info('Starting TikTok Reporting Bot...')
    # Add your bot logic here


if __name__ == '__main__':
    main()