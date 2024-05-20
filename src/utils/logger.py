import logging

def setup_logging(log_level=logging.INFO):
    # Build basic logger
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

    logger = logging.getLogger()
    return logger

logger = setup_logging()
