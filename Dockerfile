FROM docker.elastic.co/logstash/logstash:7.9.0

USER root
ADD https://jdbc.postgresql.org/download/postgresql-42.2.5.jar /usr/share/logstash/logstash-core/lib/jars/postgresql-42.2.5.jar
RUN chmod 777 /usr/share/logstash/logstash-core/lib/jars
RUN chown -R logstash /usr/share/logstash/vendor/

ADD logstash.conf /usr/share/logstash/pipeline/logstash.conf