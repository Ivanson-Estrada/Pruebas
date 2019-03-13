# projectpyspark2 version 0.1.0-SNAPSHOT user dataproc

The application should be launched through spark-submit, providing a configuration file as the only argument
An example of command line used for launching this process is as follows:

```
spark-submit --master local worker.py application.conf
```

The apppplication.conf file contents should have the following structure:

```
{
    config {
        input_file = "<PATH TO FILE>"
    }
}
```

Where PATH TO FILE should contain the path to a plan text file, as supported by hadoop.
