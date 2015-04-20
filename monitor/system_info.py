from __future__ import absolute_import, unicode_literals

import psutil
import logging

from tornado.ioloop import PeriodicCallback
from swampdragon.pubsub_providers.data_publisher import publish_data

logger = logging.getLogger(__name__)

pcb = None


def broadcast_sys_info():
    global pcb

    if pcb is None:
        pcb = PeriodicCallback(broadcast_sys_info, 500)
        pcb.start()

    cpu = psutil.cpu_percent()
    net = psutil.net_io_counters()
    mem = psutil.virtual_memory()

    pct_mem = mem.percent


    bytes_sent = '{0:.2f} kb'.format(net.bytes_sent/ 1024)
    bytes_rcvd = '{0:.2f} kb'.format(net.bytes_recv / 1024)

    publish_data('sysinfo', {
        'cpu': cpu,
        'mem': pct_mem,
        'kb_rcvd': bytes_sent,
        'kb_sent': bytes_rcvd,
    })