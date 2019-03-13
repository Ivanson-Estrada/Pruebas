# Base python-debian configuration
FROM globaldevtools.bbva.com:5000/datio-spark/engine/global/fjwam/dataproc-spark:1
ARG PYPI_INDEX_URL="https://pypi.python.org/simple"
ARG ARTIFACTORY_USER_PROFILE
ARG ARTIFACTORY_API_KEY
# Install required packages
RUN apt-get update && apt-get install -y g++ make
# Install custom packages
RUN apt-get update && apt-get install -y git
COPY . /opt/app/
WORKDIR /opt/app
# Install pip packages in requirements.txt
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir --extra-index-url ${PYPI_INDEX_URL} -r requirements.txt || /bin/true
# Install dumb-init
RUN pip3 install dumb-init
# Run custom commands
RUN pip uninstall --yes pyspark py4j && find `python -c "import sys; print(sys.prefix)"` -name "*.jar" -exec cp {} ${SPARK_HOME}/jars \; && apt-get -y autoremove
# Remove custom packages
RUN apt-get purge -y git
# Remove apt cache
RUN apt-get -y autoremove && apt-get clean
