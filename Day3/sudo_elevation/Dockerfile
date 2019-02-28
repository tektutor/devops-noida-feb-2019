FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

RUN apt-get update && apt-get install -y openssh-server python-minimal
RUN mkdir -p /var/run/sshd
RUN useradd oracle
RUN echo 'oracle:oracle' | chpasswd oracle
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN mkdir -p /home/oracle/.ssh
RUN chown oracle:oracle -R /home/oracle

COPY authorized_keys /home/oracle/.ssh/authorized_keys

EXPOSE 22
EXPOSE 80 
CMD ["/usr/sbin/sshd", "-D"]
