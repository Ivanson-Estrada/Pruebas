# fdev Project

Skynet-CLI dependency and Skynet Maven plugin allow you to perform the following functionalities:

* Initializes your ingestion and schema files.
* Deploys your files in Bitbucket,
* Executes a Kirby job (or another Spark job) in your local machine.
* Executes a Feature job in your local machine.
* Reads a path containing Avro or Parquet files to show the content of those files.


If you want to use Skynet features, you can use **skynet-cli** module through IntelliJ configuration or
**skynet-maven-plugin** through the command line.


1. Add new Run/Debug Configuration of type Application (in the Run menu).
2. Set ``com.datio.skynet.cli.SkynetCli`` as the main class.
3. Set ``fdev-ingestion/fdev`` as working directory.
4. Set ``fdev`` in "Use classpath of module" option.
5. Fill "Program arguments" field with the action and arguments you want (arguments for each step are 
detailed below):

    1. Initialize your ingestion files: ``init``.
    2. Initialize your schema files: ``init-schemas``.
    3. Initialize all the schema files: ``init-all-schemas``.
    4. Deploy your ingestion files in Git and create a PR: ``deploy``.
    5. Deploy your schema files in Git and create a PR: ``deploy-schemas``.
    6. Deploy all the schema files in Git and create a PR: ``deploy-all-schemas``.
    7. Change to another Git branch: ``go-to``
    8. Run local Kirby jobs: ``run-kirby``.
    9. Run local Feature jobs: ``run-feature``.
    10. Run local Spark jobs: ``run-job``.
    11. Read files containing Avro or Parquet files in a directory: ``read-path``.
    12. Generate and fill the required tabs to import the data dictionary in Sophia: ``sophia-tabs``.
    
NOTE: when creating the project via the archetype, you will have in the root folder a folder named ``runConfigurations``.
If you copy this folder into the ``.idea`` folder (after creating the project in IntelliJ) and reopen the project,
you'll get all configurations already done. 
    

Same functionalities listed above can be executed using Maven. To run Skynet commands with Maven,
just run the Maven command (inside of the ``fdev`` submodule or with -pl ``fdev`` option)
followed by the goal you want to execute:
    
 1. Initialize your ingestion files: ``mvn skynet:init``.
 2. Initialize only your schema files: ``mvn skynet:initSchemas``.
 3. Initialize all your schema files: ``skynet:initAllSchemas``.
 4. Deploy your ingestion files and create DataProc jobs: ``mvn skynet:deploy``.
 5. Deploy your schema files in Nexus/Artifactory: ``mvn skynet:deploySchemas``.
 6. Deploy all your schema files in Nexus/Artifactory: ``mvn skynet:deployAllSchemas``.
 7. Create a Spark job in DataProc: ``mvn skynet:createSparkJob``.
 8. Run local Kirby jobs: ``mvn skynet:runKirby``.
 9. Run local Feature jobs: ``mvn skynet:runFeature``.
 10. Run local Spark jobs: ``mvn skynet:runJob``.
 11. Read a path containing Avro or Parquet files: ``mvn skynet:readPath``.
 12. Run ingesion DataProc jobs: ``mvn skynet:ingest``.
 13. Ingestion validation through the Spark validation job: ``mvn skynet:validate``.
 14. Verify conf and JSON files: ``mvn skynet:verify``.
 15. Verify schema files: ``mvn skynet:verifySchemas``.
 16. Use admin options (see help Maven command) ``mvn skynet:admin-<option>``.
 17. Get **skynet-maven-plugin** help and usage: ``mvn skynet:help``.
