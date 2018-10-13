ARG python
from ${python}
COPY . /app
RUN apk add --no-cache gcc musl-dev
RUN cd /app && pip install -e .[tests]
