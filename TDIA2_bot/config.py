#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv

class DefaultConfig:
    """ Bot Configuration """
    load_dotenv()

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0488e8f7-2831-4bdc-8b40-8de92217dc6b")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword")
    
