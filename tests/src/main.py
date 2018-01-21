import unittest
import time
import sys
import logging
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from multiprocessing import Process


class Consumer(unittest.TestCase):

    def __init__(self):
        try:
            self.__consumer = KafkaConsumer(bootstrap_servers=['kafka'],
                                            client_id='platform', group_id='platform',
                                            auto_offset_reset='earliest', enable_auto_commit=False)
            self.__attendedResult = dict({"test": ["test send message", str(dict({"flags": "send json"}))],
                                          "testSec": ["test new topic", "retry"]})
        except:
            print("Consumer init error fail to connect.")
            sys.exit()

    # get message from kafka with all informations about the topic.
    def recv(self, topic):
        for partition in self.__consumer.partitions_for_topic(topic):
            topicpart = TopicPartition(topic, partition)
            self.__consumer.assign([topicpart])
            committed = self.__consumer.committed(topicpart)
            self.__consumer.seek_to_end(topicpart)
            last_offset = self.__consumer.position(topicpart)
            print("topic: %s partition: %s committed: %s last: %s " %
                  (topic, partition, committed, last_offset, ))
            self.__consumer.seek(topicpart, last_offset - 2)
            for e in range(2):
                a = next(self.__consumer)
                attendedValue = self.__attendedResult[topic][e]
                print("topic: {}, message: {} ".format(topic, a.value.decode()))
                assert attendedValue == a.value.decode()
                print("Assert value: ok")
            self.__consumer.close(autocommit=False)


class Producer:

    def __init__(self):
        try:
            self.__producer = KafkaProducer(bootstrap_servers=['kafka'],
                                            api_version=(0, 10, 1))
        except:
            sys.exit("Producer init error, fail to connect.")

    def send(self, topic, message):
        try:
            res = self.__producer.send(topic, message.encode('utf-8'))
            t = res.get(timeout=5)
        except:
            sys.exit("Producer send, fail to send.")


def consumeTopic(topicName):
    consumerTest = Consumer()
    consumerTest.recv(topicName)


class TestStringMethods(unittest.TestCase):

    # TEST 1 try connect to kafka with producer.
    def test_0_init(self):
        print("test_0_init:")
        producer = Producer()
        print("producer connect: ok")

    # TEST 2 send message to kafka with producer.
    def test_1_send(self):
        print("test_1_send")
        print("sleep(5)")
        time.sleep(5)
        producer = Producer()
        producer.send("test", "test send message")
        producer.send("test", str(dict({"flags": "send json"})))
        producer.send("testSec", "test new topic")
        producer.send("testSec", "retry")
        print("producer send test: ok")

    # TEST 3 recive message to kafka with consumer.
    def test_2_recv(self):
        print("test_2_recv")
        print("sleep(10)")
        time.sleep(10)
        processTopicTest = Process(target=consumeTopic, args=("test",))
        processTopicTestSec = Process(
            target=consumeTopic, args=("testSec",))
        processTopicTestSec.start()
        processTopicTest.start()
        print("sleep(15)")
        time.sleep(15)
        processTopicTestSec.join()
        processTopicTest.join()
        print("consumer read and multiple client tests: ok")


if __name__ == '__main__':
    print("Wait 10sec to be sure Kafka and Zookeeper is up.")
    time.sleep(5)
    print("Waiting modules: ok")
    unittest.main()
