# Random Number Generator

A simple Flask application that generates a random number up to a specified upper limit. The upper limit is provided as a URL parameter (e.g., `/<int:value>`).

## Overview

This Flask application exposes a single endpoint that generates a random integer between 0 and a specified upper limit. The upper limit is passed as an integer in the URL. For example, accessing `/10` will return a random integer between 0 and 10.


