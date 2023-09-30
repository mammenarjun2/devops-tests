# Base perl image used to run phash.pl file and set into a build stage
# so it can be used when running python image
FROM perl:latest as perl_build_stage
RUN cpanm Image::PHash
WORKDIR /app

FROM python:latest

# Used to copy perl files across to the second stage of the build in python
COPY --from=perl_build_stage /usr/local /usr/local
WORKDIR /app
COPY main.py /app/
COPY phash.pl /app/
COPY images/ /app/images
ADD images/ /app/images

CMD ["python", "/app/main.py"]
