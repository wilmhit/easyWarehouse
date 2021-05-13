FROM docker.elastic.co/logstash/logstash:7.12.0

RUN rm -f /usr/share/logstash/pipeline/logstash.yaml
ADD logstash-pipeline/ /usr/share/logstash/pipeline/
ADD https://jdbc.postgresql.org/download/postgresql-42.2.5.jar /usr/share/logstash/logstash-core/lib/jars
