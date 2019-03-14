# -*- coding: utf-8 -*-
import sys

import sparkutils
from sparkutils.task import PySparkTask, BusinessInformation


class WordCountTask(PySparkTask):
    """
    WordCountTask counts the word from a given file
    """
    def __init__(self):
        """
        Constructor
        """
        self.__logger = sparkutils.get_logger(WordCountTask.__qualname__)

    def runProcess(self, spark, app_config) -> int:
        """
        Execute the task
        :param spark: the applicable Spark session
        :param app_config: the process configuration
        :return: an exit code that describes the process results
        """
        input_file = app_config.getString("config.input_file")

        text_file = spark.sparkContext.textFile(input_file)
        counts = text_file.flatMap(lambda line: line.split(" ")) \
                          .map(lambda word: (word, 1)) \
                          .reduceByKey(lambda a, b: a + b)
        output = counts.collect()

        self.__logger.info("WORD COUNT RESULTS FOR %s" % input_file)
        for (word, count) in output:
            self.__logger.info("%s: %i" % (word, count))
        return 0

    def defineBusinessInfo(self, config) -> BusinessInformation:
        """
        Define the BusinessInformation for the implemented process
        :param config: the process configuration
        :return: the BusinessInformation object for this process
        """
        return BusinessInformation(0, "", "", "", "", "", "")


def run() -> int:
    """
    Application entry point
    """
    if len(sys.argv) != 2:
        print("Usage: spark-submit <MASTER_OPTIONS> worker.py <CONFIG_FILE>", file=sys.stderr)
        return -1

    task = WordCountTask()
    ret_code = sparkutils.run(task)
    print("#####################################################################")
    print("Exit code: %s" % ret_code)
    print("#####################################################################")
    return ret_code
