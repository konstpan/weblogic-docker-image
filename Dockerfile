FROM store/oracle/weblogic:12.2.1.3-dev-190111

COPY properties/* /u01/oracle/properties/
COPY scripts/* /u01/oracle/container-scripts/

USER root

RUN chmod +xw /u01/oracle/container-scripts/*.sh && \
    chmod +xw /u01/oracle/container-scripts/*.py

USER oracle

WORKDIR /u01/oracle

CMD /u01/oracle/container-scripts/createDeployAndStartDomain.sh
