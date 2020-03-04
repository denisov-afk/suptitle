import datetime

import pika
import logging
import json
from django.conf import settings


class AmqpPublisher:
    QUEUE = settings.QUEUE_VIDEORESIZER
    EXCHANGE = ''

    def __init__(self, amqp_url=settings.BROKER_URL):
        self.amqp_url = amqp_url
        self.conn = None
        self.ch = None
        self.logger = logging.getLogger(__name__)
        self._connect()

    def _connect(self):
        try:
            self.conn = pika.BlockingConnection(pika.URLParameters(settings.BROKER_URL))
            self.logger.info(f'Connection is established: {self.conn}')
            self.ch = self.conn.channel()
            self.ch.queue_declare(self.QUEUE)

        except RuntimeError as e:
            self.logger.error(f'Connect to broker raise error {e}')

    def publish(self, body, headers=None):
        properties = pika.BasicProperties()
        properties.timestamp = int(datetime.datetime.now().timestamp())
        properties.app_id = settings.WEBSITE_APP_ID
        if headers:
            properties.headers = headers

        try:
            body = json.dumps(body)
        except ValueError as e:
            self.logger.error(f'body to json encode error: {e}')
            return False

        self.ch.basic_publish(self.EXCHANGE, self.QUEUE, body, properties)
        self.logger.info(f'Publish: {body}')
        self._close()
        return True

    def _close(self):
        self.conn.close()
        self.logger.info('Connection closed')
