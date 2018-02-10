import logging
import logstash

logstash_port = 5000
logstash_addr = "localhost"

logger = logging.getLogger('appname')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(
    logstash_addr, logstash_port, version=1))
