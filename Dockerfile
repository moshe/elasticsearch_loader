ARG python
from ${python}
RUN apk add --no-cache gcc musl-dev
COPY . /app
RUN cd /app && \
        pip install -e .[tests] && \
        cd inputs/redis/ && \
        pip install -e . && \
        cd ../s3/ && \
        pip install -e .
