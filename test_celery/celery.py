"""
Celery : 비동기 작업 대기열
비동기적으로 실행해야 하는 모든 것에 사용 가능
RabbitMQ : Celery와 함께 사용하는 메세지 브로커

Broker : 작업 큐 생성, 일부 라우팅 규칙에 따라 작업 큐에 작업 발송, 작업 큐에서 worker로 작업 전달을 담당
Consumer (Celery worker) : 작업을 수행하는 하나 이상의 Celery Worker, UseCase에 따라 많은 worker를 시작할 수 있다.
Result Backend : 작업 결과를 저장하는데 사용, 필수요소는 아니기 때문에 설정에 포함시키지 않음
"""

from __future__ import absolute_import
from celery import Celery

app = Celery(
    'test_celery',
    broker='',
    backend='rpc://',
    include=['test_celery.tasks']
)

