FROM nginx:1
MAINTAINER CHO

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80

CMD ["service" "nginx" "start"]