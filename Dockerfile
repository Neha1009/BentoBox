FROM centos:latest
RUN yum install httpd -y
COPY index.html /var/www/html
ENTRYPOINT ["httpd"]
CMD ["-DFOREGROUND"]
